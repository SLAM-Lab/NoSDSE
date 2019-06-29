import fileinput
import json 
from subprocess import call
import os
"""
# sim_config.json:
{
   "edge": {
      "total_number": 6,
      "edge_id": [0, 1, 2, 3, 4, 5],
      "edge_type": ["victim", "stealer", "stealer", "stealer", "stealer", "stealer"],
      "edge_core_number": [1, 1, 1, 1, 1, 1],
      "edge_ipv4_address": ["192.168.4.9", "192.168.4.8", "192.168.4.4", "192.168.4.14", "192.168.4.15", "192.168.4.16"],
      "edge_ipv6_address": ["100:0:200:0:300:0:400:", "100:0:200:0:300:0:500:", "100:0:200:0:300:0:600:", "100:0:200:0:300:0:700:", "100:0:200:0:300:0:800:", "100:0:200:0:300:0:900:"],
      "edge_mac_address": ["00:01:00:00:00:00", "00:02:00:00:00:00", "00:03:00:00:00:00", "00:04:00:00:00:00", "00:05:00:00:00:00", "00:06:00:00:00:00"]
   },
   "gateway": {
      "total_number": 6,
      "gateway_id": 6,
      "gateway_core_number": 1,
      "gateway_ipv4_address": "192.168.4.1",
      "gateway_ipv6_address": "100:0:200:0:300:0:300:",
      "gateway_mac_address": "00:07:00:00:00:00"
   },
   "ap_mac_address": "00:10:00:00:00:00",
   "network":{
      "type": "802.11",
      "mode": "n",
      "bitrate": "600Mbps"
   }
}

# app_config.json:
{
   "N": 5,
   "M": 5,
   "FusedLayers": 16,
   "runtime": "WST" 
}
"""

power_table = {
   "802.11":{
      "g":{
            "receiverIdlePowerConsumption": "2.484mW",
            "receiverBusyPowerConsumption": "190.8mW",
            "receiverReceivingPowerConsumption": "190.8mW",
            "transmitterIdlePowerConsumption": "2.484mW",
            "transmitterTransmittingPowerConsumption": "892.8mW"
       },
      "b":{
            "receiverIdlePowerConsumption": "2.484mW",
            "receiverBusyPowerConsumption": "190.8mW",
            "receiverReceivingPowerConsumption": "190.8mW",
            "transmitterIdlePowerConsumption": "2.484mW",
            "transmitterTransmittingPowerConsumption": "979.2mW"
       },
      "n":{
            "receiverIdlePowerConsumption": "2.484mW",
            "receiverBusyPowerConsumption": "219.6mW",
            "receiverReceivingPowerConsumption": "219.6mW",
            "transmitterIdlePowerConsumption": "2.484mW",
            "transmitterTransmittingPowerConsumption": "1054.8mW"
       }
   },
   "802.15.4":{
         "receiverIdlePowerConsumption": "0.0015mW",
         "receiverBusyPowerConsumption": "10.44mW",
         "receiverReceivingPowerConsumption": "10.44mW",
         "transmitterIdlePowerConsumption": "0.0015mW",
         "transmitterTransmittingPowerConsumption": "14.4mW"
   },
   "pi0":{
      "idle": 0.5, #0.1A * 5V
      "busy": 1.15 #0.23A * 5V
   },
   "pi3":{
      "idle": 1.5, #0.3A * 5V
      "busy": 4.25, #0.85A * 5V   
      "4-core": 4.25, #  
      "2-core": 2.7, #  
      "1-core": 1.8, #
   }
}


def deepthings_config(workspace = "./",
                      total_number = 6, 
                      data_source_number = 1, 
                      edge_core_number = [1, 1, 1, 1, 1, 1,   1, 1, 1, 1, 1, 1],
                      edge_ipv4_address = ["192.168.4.9", "192.168.4.8", "192.168.4.4", 
                                           "192.168.4.14", "192.168.4.15", "192.168.4.16", 
                                           "192.168.4.6", "192.168.4.17", "192.168.4.18", 
                                           "192.168.4.19", "192.168.4.20", "192.168.4.21"],
                      edge_ipv6_address = ["100:0:200:0:300:0:400:", "100:0:200:0:300:0:500:", "100:0:200:0:300:0:600:",
                                           "100:0:200:0:300:0:700:", "100:0:200:0:300:0:800:", "100:0:200:0:300:0:900:",
                                           "100:0:100:0:300:0:400:", "100:0:100:0:300:0:500:", "100:0:100:0:300:0:600:", 
                                           "100:0:100:0:300:0:700:", "100:0:100:0:300:0:800:", "100:0:100:0:300:0:900:"],
                      edge_mac_address = ["00:00:01:00:00:00", "00:00:02:00:00:00", "00:00:03:00:00:00",
                                          "00:00:04:00:00:00", "00:00:05:00:00:00", "00:00:06:00:00:00",
                                          "00:01:00:00:00:00", "00:02:00:00:00:00", "00:03:00:00:00:00", 
                                          "00:04:00:00:00:00", "00:05:00:00:00:00", "00:06:00:00:00:00"],
                      gateway_core_number = 4, 
                      gateway_ipv4_address = "192.168.4.1",
                      gateway_ipv6_address = "100:0:200:0:300:0:300:",
                      gateway_mac_address = "00:07:00:00:00:00",
                      ap_mac_address = "00:10:00:00:00:00", 
                      network = {
                        "type": "802.11",
                         "mode": "n", 
                         "bitrate": "600Mbps"
                      },
                      N = 5,
                      M = 5,
                      FusedLayers = 16,
                      runtime = "WST"
                     ):
# edge parameters
    #total_number = 6
    #data_source_number = 1
    edge_id = range(total_number)
    edge_type = data_source_number*["victim"] + (total_number-data_source_number)*["stealer"]
    edge_core_number = edge_core_number[:total_number]
    edge_ipv4_address = edge_ipv4_address[:total_number]
    edge_ipv6_address = edge_ipv6_address[:total_number]
    edge_mac_address = edge_mac_address[:total_number]

# gateway parameters
    #gateway_core_number = 1
    #gateway_ipv4_address = "192.168.4.1"
    #gateway_ipv6_address = "100:0:200:0:300:0:300:"
    #gateway_mac_address = "00:07:00:00:00:00"
    
# ap and network parameters
    #ap_mac_address = "00:10:00:00:00:00"
    #network = {
    #  "type": "802.11",
    #  "mode": "n", 
    #  "bitrate": "600Mbps"
    #}
   
    sim_config_json = {
        "edge": {
            "total_number": total_number,
            "edge_id": edge_id,
            "edge_type": edge_type,
            "edge_core_number": edge_core_number,
            "edge_ipv4_address": edge_ipv4_address,
            "edge_ipv6_address": edge_ipv6_address,
            "edge_mac_address": edge_mac_address
         },
        "gateway": {
            "total_number": total_number,
            "gateway_id": total_number,
            "gateway_core_number": gateway_core_number,
            "gateway_ipv4_address": gateway_ipv4_address,
            "gateway_ipv6_address": gateway_ipv6_address,
            "gateway_mac_address": gateway_mac_address
         },
        "ap_mac_address": ap_mac_address,
        "network":network
    }
    with open(workspace + "src/sim_config.json", "w") as jfile:
        json.dump(sim_config_json, jfile, sort_keys=False, indent=4, separators=(',', ': ')) 

    app_config_json = {
      "N": N,
      "M": M,
      "FusedLayers": FusedLayers,
      "runtime": runtime 
    }

    with open(workspace + "src/app_config.json", "w") as jfile:
        json.dump(app_config_json, jfile, sort_keys=False, indent=4, separators=(',', ': ')) 

def remake_lwip(workspace = "./"):
    with open(workspace + "src/sim_config.json") as jfile:
        sim_config_json = json.load(jfile) 

    for line in fileinput.input("../../NoSSim/lwip-hcsim/ports/hcsim/lwipopts.h", inplace=True):
       if "#define LWIP_IPV6 " in line:
           if sim_config_json["network"]["type"] == "802.15.4":
               print "#define LWIP_IPV6          1\n",
           else :
               print "#define LWIP_IPV6          0\n",
       elif "#define LWIP_IPV4 " in line:
           if sim_config_json["network"]["type"] == "802.15.4":
               print "#define LWIP_IPV4          0\n",
           else :
               print "#define LWIP_IPV4          1\n",
       else:
           print "%s" % (line),

    call(["make", "-C", "../../NoSSim/lwip-hcsim/ports", "clean"])
    call(["make", "-C", "../../NoSSim/lwip-hcsim/ports", "-j", "8"])


def remake_app():
    #call(["make", "cleanall"])
    call(["make", "makefiles"])
    call(["make", "clean"])
    call(["make", "-j", "8"])


def omnetpp_ini(workspace = "./"):
    with open(workspace + "src/sim_config.json") as jfile:
        sim_config_json = json.load(jfile) 
    with open(workspace + "src/omnetpp.ini.template", "r") as f_in, open(workspace + "src/omnetpp.ini", "w") as f_out:
        for line in f_in:
            #number of edges
            f_out.write(line)
            if "energy settings" in line:
                consumer_path = "**.cliHost[*].wlan.radio.energyConsumer."
                if sim_config_json["network"]["type"] == "802.11": 
                    power_number = power_table["802.11"][sim_config_json["network"]["mode"]]
                else:
                    power_number = power_table["802.15.4"]
                f_out.write(consumer_path + "receiverIdlePowerConsumption = " + power_number["receiverIdlePowerConsumption"] + os.linesep)
                f_out.write(consumer_path + "receiverBusyPowerConsumption = " + power_number["receiverBusyPowerConsumption"] + os.linesep)
                f_out.write(consumer_path + "receiverReceivingPowerConsumption = " + power_number["receiverReceivingPowerConsumption"] + os.linesep)
                f_out.write(consumer_path + "transmitterIdlePowerConsumption = " + power_number["transmitterIdlePowerConsumption"] + os.linesep)
                f_out.write(consumer_path + "transmitterTransmittingPowerConsumption = " + power_number["transmitterTransmittingPowerConsumption"] + os.linesep)
            if "number of edges" in line:
                f_out.write("Cluster.numCli = " + str(sim_config_json["edge"]["total_number"]+1) + os.linesep)
            if "nic settings" in line:
                for device_id in sim_config_json["edge"]["edge_id"]:
                    f_out.write("**.cliHost[" + str(device_id) + "].wlan.mac.address = " + "\"" + sim_config_json["edge"]["edge_mac_address"][device_id] + "\"" + os.linesep)
                f_out.write("# gateway mac address"+ os.linesep)
                f_out.write("**.cliHost[" + str(sim_config_json["gateway"]["gateway_id"]) + "].wlan.mac.address = " 
                            + "\"" + sim_config_json["gateway"]["gateway_mac_address"] + "\"" + os.linesep)
                #802.11 will be deployed with a Access Point 
                if sim_config_json["network"]["type"] == "802.11":
                   f_out.write("**.ap.wlan[*].mac.address = "+ "\"" + sim_config_json["ap_mac_address"]+ "\"" + os.linesep)
                   f_out.write("**.mgmt.accessPointAddress = "+ "\"" + sim_config_json["ap_mac_address"]+ "\"" + os.linesep)
            if "phy settings" in line:
                if sim_config_json["network"]["type"] == "802.11":
                   f_out.write("**.opMode = " + "\"" + sim_config_json["network"]["mode"] + "\"" + os.linesep)
                   f_out.write("**.bitrate = "+ sim_config_json["network"]["bitrate"] + os.linesep)
                   f_out.write("**.basicBitrate = "+ sim_config_json["network"]["bitrate"] + os.linesep)
                   f_out.write("**.controlBitrate = "+ sim_config_json["network"]["bitrate"] + os.linesep + os.linesep)
                   if sim_config_json["network"]["mode"] == "n": 
                       f_out.write("**.errorModelType = \"\"" + os.linesep)
                       f_out.write("**.numAntennas = 4" + os.linesep)
                   f_out.write("**.mac.EDCA = true" + os.linesep)
                   f_out.write("**.mac.maxQueueSize = 100000" + os.linesep)
                   f_out.write("**.mac.rtsThresholdBytes = 2346B" + os.linesep)
                   f_out.write("**.mac.retryLimit = 7" + os.linesep)
                   f_out.write("**.mac.cwMinData = 31" + os.linesep)
                   f_out.write("**.mac.cwMinBroadcast = 31" + os.linesep)
                   f_out.write("**.radio.transmitter.power = 200mW" + os.linesep)
                   f_out.write("**.radio.transmitter.headerBitLength = 100b" + os.linesep)
                   f_out.write("**.radio.transmitter.carrierFrequency = 2.4GHz" + os.linesep)
                   f_out.write("**.radio.transmitter.bandwidth = 40MHz" + os.linesep)
                   f_out.write("**.radio.receiver.bandwidth = 40MHz" + os.linesep)
                   f_out.write("**.radio.receiver.sensitivity = -85dBm" + os.linesep)
                   f_out.write("**.radio.receiver.snirThreshold = 4dB" + os.linesep)

                if sim_config_json["network"]["type"] == "802.15.4":
                   f_out.write("**.queueLength = 1000" + os.linesep)
                   f_out.write("**.macMaxFrameRetries = 100" + os.linesep)
                   f_out.write("**.macMaxCSMABackoffs = 101" + os.linesep)
                   f_out.write("**.wlan.radio.transmitter.preambleDuration = 0" + os.linesep)

def cluster_ned(workspace = "./"):
    with open(workspace + "src/sim_config.json") as jfile:
        sim_config_json = json.load(jfile) 
    if sim_config_json["network"]["type"] == "802.11":
        call(["cp", workspace + "src/Cluster.ned.wifi", workspace + "src/Cluster.ned"])        
    if sim_config_json["network"]["type"] == "802.15.4":
        call(["cp", workspace + "src/Cluster.ned.6lowpan", workspace + "src/Cluster.ned"])    

def get_result(workspace = "./", edge_number = 1, edge_core_config = [2]):
   frame_num = 4.0
   total_nic_energy = 0.0
   power_table={
      "idle": 1.5, #0.3A * 5V 
      4: 4.25, #  
      2: 2.7, #  
      1: 1.8 #
   }
   for edge_id in range(edge_number):
      with open(workspace + "src/nic_energy_device_"+str(edge_id)+".json") as jfile:
         nic_json = json.load(jfile) 
         total_nic_energy = total_nic_energy + nic_json["energy"]/frame_num
   avg_nic_energy = total_nic_energy/edge_number
   print "Average NIC energy is: " , avg_nic_energy

   with open(workspace + "src/result.json") as jfile:
      result_json = json.load(jfile) 
   total_app_energy = 0.0
   for edge_id in range(edge_number):
      total_edge_time = 0.0
      if "application" in result_json["edge_"+str(edge_id)]:
         total_edge_time = total_edge_time + (result_json["edge_"+str(edge_id)]["application"])/frame_num
      if "lwip" in result_json["edge_"+str(edge_id)]:
         total_edge_time = total_edge_time + result_json["edge_"+str(edge_id)]["lwip"]/frame_num
      print "Edge", edge_id, " Time is:", total_edge_time
      print "Edge", edge_id, " Energy is:", total_edge_time*power_table[edge_core_config[edge_id]]
      total_app_energy = total_app_energy + total_edge_time*power_table[edge_core_config[edge_id]]     

   avg_app_energy = total_app_energy/edge_number
   print "Average App energy is: " , avg_app_energy
   print "Average busy total energy is: " , avg_app_energy + avg_nic_energy
   print "Average latency: " , result_json["edge_0"]["latency"]
   return result_json["edge_0"]["latency"], avg_app_energy + avg_nic_energy


def evaluate_one(top_workspace = "./",
                 genome = [6,  3,  2,   0, 1, 0, 2, 0, 0,    0, 1, 0, 2, 0, 0,  3]):#last one is fusing layers
    core_config_list ={
      0 : 1,
      1 : 2,
      2 : 4
    }
    layers_config_list ={
      0 : 4,
      1 : 8,
      2 : 12,
      3 : 16,
    }

    mode_g = ["6Mbps", "9Mbps", "12Mbps", "18Mbps", "24Mbps", "36Mbps", "48Mbps", "54Mbps"]
    mode_b = ["1Mbps", "2Mbps", "5.5Mbps", "11Mbps"]
    network_config_list ={
      0 : {
        "type": "802.11",
        "mode": "b", 
        "bitrate": "5.5Mbps"
      },
      1 : {
        "type": "802.11",
        "mode": "b", 
        "bitrate": "11Mbps"
      },
      2 : {
        "type": "802.11",
        "mode": "g", 
        "bitrate": "6Mbps"
      },
      3 : {
        "type": "802.11",
        "mode": "g", 
        "bitrate": "18Mbps"
      },
      4 : {
        "type": "802.11",
        "mode": "g", 
        "bitrate": "48Mbps"
      },
      5 : {
        "type": "802.11",
        "mode": "g", 
        "bitrate": "54Mbps"
      },
      6 : {
        "type": "802.11",
        "mode": "n", 
        "bitrate": "600Mbps"
      }
    }
    edge_core_config = [core_config_list[genome[3]], core_config_list[genome[4]], core_config_list[genome[5]], 
                        core_config_list[genome[6]], core_config_list[genome[7]], core_config_list[genome[8]], 
                        core_config_list[genome[9]], core_config_list[genome[10]], core_config_list[genome[11]], 
                        core_config_list[genome[12]], core_config_list[genome[13]], core_config_list[genome[14]]
                       ]
    edge_number = genome[2]
    n =  genome[1]
    network_option = genome[0]
    network_config = network_config_list[network_option]
    print "edge_core_number:", edge_core_config
    print "edge_number:", edge_number
    print "FTP", n
    print network_config
    
    m = n
    data_source = 1
    layers = layers_config_list[genome[15]]
    deepthings_config( workspace = top_workspace,
                       edge_core_number = edge_core_config,
                       total_number = edge_number, 
                       data_source_number = data_source,
                       N = n,
                       M = m,
                       FusedLayers = layers,
                       network = network_config
                      )
    omnetpp_ini(top_workspace)

    #recompile = 1
    #cluster_ned(top_workspace)
    #remake_lwip(top_workspace)
    remake_app()
    #recompile = 1


    call(["make", "-C", top_workspace, "test"])
    print "Simulation is finished"
    print get_result(top_workspace, edge_number, edge_core_config)    
    return get_result(top_workspace, edge_number, edge_core_config)


import time
def runtime_measure():
    for ftp_dim in [3, 4, 5]:
      wall_time_list = []
      sim_time_list = []
      for node_number in range(1, 13):
         start = time.time()
         result = evaluate_one(top_workspace = "../deepthings/", genome = [6,  ftp_dim,  node_number,  0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 3])
         end = time.time()
         print result
         with open("src/result.json") as jfile:
            result_json = json.load(jfile) 
         print "Wall time is: ", (end - start)
         wall_time_list.append(end - start)
         print "Simulated time is:", result_json["gateway"]["total_latency"]
         sim_time_list.append(result_json["gateway"]["total_latency"])
  

      result_dic = {"wall_time_list": wall_time_list, "sim_time_list": sim_time_list}
      with open(str(ftp_dim)+"x"+str(ftp_dim)+"runtime_measure.json", "w") as jfile:
        json.dump(result_dic, jfile, sort_keys=False, indent=4, separators=(',', ': ')) 


def calculate_improvement():
    result = evaluate_one(top_workspace = "../deepthings/", genome = [6,  3,  1,  0, 2, 2, 2, 2, 2,  2, 2, 2, 2, 2, 2, 3])
    latency_ref = result[0]
    energy_ref = result[1]

    #result = evaluate_one(top_workspace = "../deepthings_1/", genome = [6,  3,  5,  2, 1, 2, 1, 2, 2,  2, 2, 2, 2, 2, 2, 2])
    latency_best = 4.77906130968
    
    result = evaluate_one(top_workspace = "../deepthings/", genome = [6,  3,  12,  2, 1, 1, 1, 1, 1,  1, 1, 1, 1, 1, 1, 0])
    energy_best = result[1]
    
    print "latency_ref: ", latency_ref
    print "energy_ref: ", energy_ref

    print "latency_best: ", latency_best
    print "energy_best: ", energy_best

    print "Speed up is: ", latency_ref/latency_best
    print "Energy reduction is: ", (energy_ref-energy_best)/energy_ref


def calculate_manual_improvement():
    result = evaluate_one(top_workspace = "../deepthings/", genome = [6,  3,  6,  0, 0, 0, 0, 0, 0,  2, 2, 2, 2, 2, 2, 3])
    latency_ref = result[0]
    energy_ref = result[1]

    #result = evaluate_one(top_workspace = "../deepthings_1/", genome = [6,  3,  5,  2, 1, 2, 1, 2, 2,  2, 2, 2, 2, 2, 2, 2])
    latency_best = 4.77906130968
    
    result = evaluate_one(top_workspace = "../deepthings/", genome = [6,  3,  12,  2, 1, 1, 1, 1, 1,  1, 1, 1, 1, 1, 1, 0])
    energy_best = result[1]
    
    print "latency_ref: ", latency_ref
    print "energy_ref: ", energy_ref

    print "latency_best: ", latency_best
    print "energy_best: ", energy_best

    #print "Speed up is: ", latency_ref/latency_best
    print "Latency reduction is: ", (latency_ref-latency_best)/latency_ref
    print "Energy reduction is: ", (energy_ref-energy_best)/energy_ref



if __name__ == "__main__":
    #runtime_measure()
    result = evaluate_one(top_workspace = "./", genome = [6,  3,  6,  0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 2])
    print result
    calculate_improvement()
    calculate_manual_improvement()

"""
    edge_number = 6
    data_source = 1
    layers = 16
    n = 5
    m = n
    print "Generating results of: "+ str(n) + "x" + str(m) + "_" + str(layers) + "/"+str(data_source)+"_data_src_"+str(edge_number)+"_edge.json"
    deepthings_config(
                       edge_core_number = [4, 4, 4, 4, 4, 4],
                       total_number = edge_number, 
                       data_source_number = data_source,
                       N = n,
                       M = m,
                       FusedLayers = layers,
                       network = {
                          "type": "802.11",
                          "mode": "n", 
                          "bitrate": "600Mbps"
                       }

                   )
    omnetpp_ini()
    remake_lwip()
    remake_app()
    call(["make","test"])
    print "Simulation is finished"
   
"""


"""    
    ftp=[3, 4, 5]
    cluster_size = [1, 2, 3, 4, 5, 6]   
    layers = 16
#Fix data source
    data_source = 1
    for n in ftp:  
       for edge_number in cluster_size: 
          m = n
          print "Generating results of: "+ str(n) + "x" + str(m) + "_" + str(layers) + "/"+str(data_source)+"_data_src_"+str(edge_number)+"_edge.json"
          deepthings_config(
                       total_number = edge_number, 
                       data_source_number = data_source,
                       N = n,
                       M = m,
                       FusedLayers = layers,
                      )
          omnetpp_ini()
          call(["make","test"])
          print "Simulation is finished"
          call(["cp","src/result.json", "results/"+ str(n) + "x" + str(m) + "_" + str(layers) + "/"+str(data_source)+"_data_src_"+str(edge_number)+"_edge.json"])

    
#Fix edge_number
    edge_number = 6
    for n in ftp:   
       for data_source in cluster_size:

          m = n
          print "Generating results of: "+ str(n) + "x" + str(m) + "_" + str(layers) + "/"+str(data_source)+"_data_src_"+str(edge_number)+"_edge.json"
          deepthings_config(
                       total_number = edge_number, 
                       data_source_number = data_source,
                       N = n,
                       M = m,
                       FusedLayers = layers,
                      )
          omnetpp_ini()
          call(["make","test"])
          print "Simulation is finished"
          call(["cp","src/result.json", "results/"+ str(n) + "x" + str(m) + "_" + str(layers) + "/"+str(data_source)+"_data_src_"+str(edge_number)+"_edge.json"])
"""


