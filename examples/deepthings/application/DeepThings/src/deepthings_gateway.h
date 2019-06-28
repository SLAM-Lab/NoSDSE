#ifndef DEEPTHINGS_GATEWAY_H
#define DEEPTHINGS_GATEWAY_H
#include "darkiot.h"
#include "configure.h"
void deepthings_collect_result_thread(void *arg);
void deepthings_merge_result_thread(void *arg);
void* deepthings_result_gateway(void* srv_conn, void* arg);
void deepthings_work_stealing_thread(void *arg);
device_ctxt* deepthings_gateway_init(uint32_t N, uint32_t M, uint32_t fused_layers, char* network, char* weights, uint32_t total_edge_number, const char** addr_list);
void deepthings_gateway(uint32_t N, uint32_t M, uint32_t fused_layers, char* network, char* weights, uint32_t total_edge_number, const char** addr_list);
#endif
