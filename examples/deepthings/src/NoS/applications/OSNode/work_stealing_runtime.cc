#include "work_stealing_runtime.h"

//#if IPV4_TASK
//char* addr_list[MAX_EDGE_NUM] = EDGE_ADDR_LIST;
//#elif IPV6_TASK/*IPV4_TASK*/
//char* addr_list[MAX_EDGE_NUM] = {"100:0:200:0:300:0:400:", "100:0:200:0:300:0:500:", "100:0:200:0:300:0:600:", "100:0:200:0:300:0:700:", "100:0:200:0:300:0:800:", "100:0:200:0:300:0:900:"};
//#endif/*IPV4_TASK*/   


void test_deepthings_stealer_edge(uint32_t N, uint32_t M, uint32_t fused_layers, uint32_t edge_id){
   char network[30] = "models/yolo.cfg";
   char weights[30] = "models/yolo.weights";

   device_ctxt* ctxt = deepthings_edge_init(N, M, fused_layers, network, weights, edge_id);

   sys_thread_t t1 = sys_thread_new("steal_partition_and_perform_inference_thread", 
                                    steal_partition_and_perform_inference_thread, ctxt, 101, 0);
   sys_thread_t t2 = sys_thread_new("send_result_thread", send_result_thread, ctxt, 102, 0);

   sys_thread_join(t1);
   sys_thread_join(t2);
}

void test_deepthings_victim_edge(uint32_t N, uint32_t M, uint32_t fused_layers, uint32_t edge_id){//edge_id == 0;
   char network[30] = "models/yolo.cfg";
   char weights[30] = "models/yolo.weights";
   //Load configuration here
   device_ctxt* ctxt = deepthings_edge_init(N, M, fused_layers, network, weights, edge_id);

   sys_thread_t t1 = sys_thread_new("partition_frame_and_perform_inference_thread", 
                                    partition_frame_and_perform_inference_thread, ctxt, 102, 0);
   sys_thread_t t2 = sys_thread_new("send_result_thread", send_result_thread, ctxt, 101, 0);
   sys_thread_t t3 = sys_thread_new("deepthings_serve_stealing_thread", deepthings_serve_stealing_thread, ctxt, 101, 0);

   sys_thread_join(t1);
   sys_thread_join(t2);
   sys_thread_join(t3);
}

void* test_deepthings_result_gateway(void* srv_conn, void* arg){
   device_ctxt* ctxt = (device_ctxt*)arg;
   service_conn *conn = (service_conn *)srv_conn;
   int32_t cli_id;
   int32_t frame_seq;
   blob* temp = recv_data(conn);

   cli_id = get_blob_cli_id(temp);
   frame_seq = get_blob_frame_seq(temp);

/*DEBUG*/
   char ip_addr[100];
   get_dest_ip_string(ip_addr, conn);
   std::cout << "Getting client " << cli_id << "'s result of partition " << get_blob_task_id(temp) << ",  frame " << frame_seq 
             << " from: " << ip_addr << ", at time: " << sc_core::sc_time_stamp().to_seconds()  << std::endl;
/*DEBUG*/

   enqueue(ctxt->results_pool[cli_id], temp);
   free_blob(temp);
   ctxt->results_counter[cli_id]++;
   if(ctxt->results_counter[cli_id] == ctxt->batch_size){
      temp = new_empty_blob(cli_id);
      enqueue(ctxt->ready_pool, temp);
      free_blob(temp);
      ctxt->results_counter[cli_id] = 0;
   }

   return NULL;
}

void test_deepthings_collect_result_thread(void *arg){
   const char* request_types[]={"result_gateway"};
   void* (*handlers[])(void*, void*) = {deepthings_result_gateway};
   int result_service = service_init(RESULT_COLLECT_PORT, TCP);
   start_service(result_service, TCP, request_types, 1, handlers, arg);
   close_service(result_service);
}

void test_deepthings_merge_result_thread(void *arg){
   cnn_model* model = (cnn_model*)(((device_ctxt*)(arg))->model);
   blob* temp;
   int32_t cli_id = 0;
   int32_t frame_seq = 0;
   int32_t total_frames = 0;
   double all_frame_latency[MAX_EDGE_NUM]; 
   
   while(1){
      temp = dequeue_and_merge((device_ctxt*)arg);
      cli_id = get_blob_cli_id(temp);
      frame_seq = get_blob_frame_seq(temp);
      printf("Client %d, frame sequence number %d, all partitions are merged in deepthings_merge_result_thread at time %f\n", 
             cli_id, frame_seq,  sc_core::sc_time_stamp().to_seconds());


      float* fused_output = (float*)(temp->data);
      image_holder img = load_image_as_model_input(model, get_blob_frame_seq(temp));
      set_model_input(model, fused_output);
      forward_all(model, model->ftp_para->fused_layers);   
      draw_object_boxes(model, get_blob_frame_seq(temp));
      free_image_holder(model, img);

      //std::cout << "================0 Time is: " << sc_core::sc_time_stamp().to_seconds() << std::endl;
      //os_model_context* os_model = sim_ctxt.get_os_ctxt( sc_core::sc_get_current_process_handle() );
      //os_model->os_port->timeWait(2000000000000, sim_ctxt.get_task_id(sc_core::sc_get_current_process_handle()));
      //os_model->os_port->syncGlobalTime(sim_ctxt.get_task_id(sc_core::sc_get_current_process_handle()));
      //std::cout << "================1 Time is: " << sc_core::sc_time_stamp().to_seconds() << std::endl;
      double t0 = sc_core::sc_time_stamp().to_seconds();
      std::cout << "================ 0 Time is ================: " << sc_core::sc_time_stamp().to_seconds() << std::endl;
      if((simulation_config.deepthings_para)->getFusedLayers() < 16){
         std::string input = std::to_string(get_blob_frame_seq(temp)) + "_" + std::to_string( (simulation_config.deepthings_para)->getFusedLayers() ) + "_0";
         record_static("forward_until", (char*)input.c_str(), "application");
         sys_time_wait("forward_until", (char*)input.c_str());
      }
      std::cout << "================ 1 Time is ================:: " << sc_core::sc_time_stamp().to_seconds() << std::endl;
      std::cout << "================ Duration is ================:: " << sc_core::sc_time_stamp().to_seconds() - t0 << std::endl;

      if (frame_seq == 0) all_frame_latency[cli_id] = 0;
      all_frame_latency[cli_id] = all_frame_latency[cli_id] + sc_core::sc_time_stamp().to_seconds() - frame_start_time[cli_id][frame_seq];
      (simulation_config.result)->set_edge_result(cli_id, "latency" ,all_frame_latency[cli_id]/(frame_seq+1));

      (simulation_config.result)->set_gateway_result("total_latency", sc_core::sc_time_stamp().to_seconds());

      free_blob(temp);
      printf("Client %d, frame sequence number %d, finish processing at time %f\n", cli_id, frame_seq, sc_core::sc_time_stamp().to_seconds());
      total_frames++;
      if(total_frames == ((simulation_config.data_source)*FRAME_NUM)){
         os_model_context* os_model = sim_ctxt.get_os_ctxt( sc_core::sc_get_current_process_handle() );
         os_model -> ctrl_out1->write(0);
      }
   }
   
}

void test_deepthings_gateway(uint32_t N, uint32_t M, uint32_t fused_layers, uint32_t total_edge_number){
   char network[30] = "models/yolo.cfg";
   char weights[30] = "models/yolo.weights";
   char* addr_list[MAX_EDGE_NUM];

   for(int edge_num = 0; edge_num < (simulation_config.cluster)->total_number; edge_num++){
      #if IPV4_TASK
      std::string ipv_address = (simulation_config.cluster)->edge_ipv4_address[edge_num];
      #elif IPV6_TASK/*IPV4_TASK*/
      std::string ipv_address = (simulation_config.cluster)->edge_ipv6_address[edge_num];
      #endif/*IPV4_TASK*/   
      addr_list[edge_num] = new char[ipv_address.length() + 1];
      strcpy(addr_list[edge_num], ipv_address.c_str());
   }

   device_ctxt* ctxt = deepthings_gateway_init(N, M, fused_layers, network, weights, total_edge_number, (const char **)addr_list);
   sys_thread_t t1 = sys_thread_new("deepthings_collect_result_thread", deepthings_collect_result_thread, ctxt, 102, 0);
   sys_thread_t t2 = sys_thread_new("deepthings_merge_result_thread", test_deepthings_merge_result_thread, ctxt, 102, 0);
   sys_thread_t t3 = sys_thread_new("deepthings_work_stealing_thread", deepthings_work_stealing_thread, ctxt, 101, 0);

   sys_thread_join(t1);
   sys_thread_join(t2);
   sys_thread_join(t3);

   for(int edge_num = 0; edge_num < (simulation_config.cluster)->total_number; edge_num++){
      delete [] addr_list[edge_num];
   }

}























