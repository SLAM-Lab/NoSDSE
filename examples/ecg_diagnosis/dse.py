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
      "edge_type": ["0", "0", "0", "0", "0", "0"],
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
      "busy": 4.25 #0.85A * 5V   
   }
}

energy_table = {
   1:{
      "idle": 0.5, #0.1A * 5V
      "busy": 1.15 #0.23A * 5V
   },
   4:{
      "idle": 1.5, #0.3A * 5V
      "busy": 4.25 #0.85A * 5V   
   }
}

def sim_config(total_number = 6, 
                      data_source_number = 1, 
                      edge_type = ["2", "2", "2", "2", "2", "2"],
                      edge_core_number = [1, 1, 1, 1, 1, 1],
                      edge_ipv4_address = ["192.168.4.9", "192.168.4.8", "192.168.4.4",
                                           "192.168.4.14", "192.168.4.15", "192.168.4.16"],
                      edge_ipv6_address = ["100:0:200:0:300:0:400:", "100:0:200:0:300:0:500:", "100:0:200:0:300:0:600:",
                                           "100:0:200:0:300:0:700:", "100:0:200:0:300:0:800:", "100:0:200:0:300:0:900:"],
                      edge_mac_address = ["00:01:00:00:00:00", "00:02:00:00:00:00", "00:03:00:00:00:00", 
                                          "00:04:00:00:00:00", "00:05:00:00:00:00", "00:06:00:00:00:00"],
                      gateway_core_number = 1, 
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
    edge_type = edge_type[:total_number]
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
    with open("src/sim_config.json", "w") as jfile:
        json.dump(sim_config_json, jfile, sort_keys=False, indent=4, separators=(',', ': ')) 

    app_config_json = {
      "N": N,
      "M": M,
      "FusedLayers": FusedLayers,
      "runtime": runtime 
    }

    with open("src/app_config.json", "w") as jfile:
        json.dump(app_config_json, jfile, sort_keys=False, indent=4, separators=(',', ': ')) 


def omnetpp_ini():
    with open("src/sim_config.json") as jfile:
        sim_config_json = json.load(jfile) 
    with open("src/omnetpp.ini.template", "r") as f_in, open("src/omnetpp.ini", "w") as f_out:
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

def cluster_ned():
    with open("src/sim_config.json") as jfile:
        sim_config_json = json.load(jfile) 
    if sim_config_json["network"]["type"] == "802.11":
        call(["cp", "src/Cluster.ned.wifi", "src/Cluster.ned"])        
    if sim_config_json["network"]["type"] == "802.15.4":
        call(["cp", "src/Cluster.ned.6lowpan", "src/Cluster.ned"])        

def remake_lwip():
    with open("src/sim_config.json") as jfile:
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

def remake_runtime():
    call(["make", "-C", "./networking_api", "clean"])
    call(["make", "-C", "./networking_api"])

def remake_app():
    #call(["make", "cleanall"])
    call(["make", "makefiles"])
    call(["make", "clean"])
    call(["make", "-j", "8"])

def store_result(edge_number, network_type, network_mode, offload, edge_core_number, gateway_core_number):
   with open("src/result.json") as jfile:
      result_json = json.load(jfile) 

   result_file = "./results"
   if network_type == "802.11":
      if network_mode == "g":
         result_file = result_file + "/802_11_g"
      if network_mode == "b":
         result_file = result_file + "/802_11_b"
   if network_type == "802.15.4":
      result_file = result_file + "/802_15_4"

   if edge_core_number == 1:
      result_file = result_file+"/pi0_"
   else:
      result_file = result_file+"/pi3_"

   if gateway_core_number == 1:
      result_file = result_file+"pi0"
   else:
      result_file = result_file+"pi3"

   result_file = result_file + "/" + str(edge_number) + "_edge_" + "offload_" + offload + ".json"

   for edge_id in range(edge_number):
      with open("src/nic_energy_device_"+str(edge_id)+".json") as jfile:
         nic_json = json.load(jfile) 
      result_json["edge_"+str(edge_id)]["nic_energy"] = nic_json["energy"]
   with open("src/nic_energy_device_"+str(edge_number)+".json") as jfile:
      nic_json = json.load(jfile) 
   result_json["gateway"]["nic_energy"] = nic_json["energy"]  

   with open(result_file, "w") as jfile:
      json.dump(result_json, jfile, sort_keys=False, indent=4, separators=(',', ': ')) 







def get_latency_and_energy(edge_number, edge_core_config):
   FRAME_NUM=20.0
   with open("src/result.json") as jfile:
      result_json = json.load(jfile)    
   for edge_id in range(edge_number):
      with open("src/nic_energy_device_"+str(edge_id)+".json") as jfile:
         nic_json = json.load(jfile) 
      result_json["edge_"+str(edge_id)]["nic_energy"] = nic_json["energy"]
   with open("src/nic_energy_device_"+str(edge_number)+".json") as jfile:
      nic_json = json.load(jfile) 
   result_json["gateway"]["nic_energy"] = nic_json["energy"]  
   o2o_latency = result_json["gateway"]["latency"]
   avg_energy = 0.0
   total_energy = 0.0
   total_time = 0.0

   for cli in range(edge_number):
      print "Client"+str(cli)
      print "busy_power is: ", energy_table[edge_core_config[cli]]["busy"]
      print "idle_power is: ", energy_table[edge_core_config[cli]]["idle"]
      busy_power = energy_table[edge_core_config[cli]]["busy"]
      idle_power = energy_table[edge_core_config[cli]]["idle"]
      busy_time = 0.0
      idle_time = 0.0
      if "application" not in result_json["edge_"+str(cli)]:
          busy_time = result_json["edge_"+str(cli)]["lwip"] 
      else:
          busy_time = result_json["edge_"+str(cli)]["application"] + result_json["edge_"+str(cli)]["lwip"] 
      idle_time = result_json["gateway"]["latency"] * FRAME_NUM - busy_time
      total_time = total_time + busy_time
      print "busy_time is:", busy_time
      print "idle_time is:", idle_time
      total_energy = total_energy + (idle_time*idle_power + busy_power*busy_time + result_json["edge_"+str(cli)]["nic_energy"])/FRAME_NUM
   avg_energy = total_energy/edge_number
   print "avg_energy:", avg_energy
   print "avg_energy:", total_time*busy_power/edge_number/FRAME_NUM + idle_power*( result_json["gateway"]["latency"] - total_time/edge_number/FRAME_NUM) 
 
   return o2o_latency, avg_energy

def evaluate_one(genome = [2,   3, 3, 3, 3, 3, 3,    1, 1, 1, 1, 1, 1]):
    #return sum(genome[0:9]), -sum(genome[6:13]) 
    network_type = genome[0] 
    offload = genome[1:7]
    edge_core = genome[7:13]
    #network_type [0, 1, 2]
    #offload ["0", "1", "2", "3"]
    #edge_core [1, 4]
    core_config_list ={
      0 : 1,
      1 : 4
    }

    offload_config_list ={
      0 : "0",
      1 : "1",
      2 : "2",
      3 : "3"
    }

    network_config_list ={
      0 : {
        "type": "802.11",
        "mode": "b", 
        "bitrate": "1Mbps"
      },
      1 : {
        "type": "802.11",
        "mode": "g", 
        "bitrate": "6Mbps"
      },
      2 : {
        "type": "802.15.4",
        "mode": "", 
        "bitrate": ""
      }
    }
    #[0,   0, 0, 0, 0, 0, 0,    0, 0, 0, 0, 0, 0]
    #[2,   3, 3, 3, 3, 3, 3,    1, 1, 1, 1, 1, 1]
    #o_level = 2
    #o_level_list = [o_level, o_level, o_level, o_level, o_level, o_level]
    #device_level = 0
    #device_list = [device_level, device_level, device_level, device_level, device_level, device_level]
    
    #edge_core_config = [core_config_list[device_list[0]], core_config_list[device_list[1]], core_config_list[device_list[2]], 
                        #core_config_list[device_list[3]], core_config_list[device_list[4]], core_config_list[device_list[5]]]
    #offload_config = [offload_config_list[o_level_list[0]], offload_config_list[o_level_list[1]], offload_config_list[o_level_list[2]], 
                      #offload_config_list[o_level_list[3]], offload_config_list[o_level_list[4]], offload_config_list[o_level_list[5]]]
    
    offload_config   = [offload_config_list[offload[0]], offload_config_list[offload[1]], offload_config_list[offload[2]], 
                        offload_config_list[offload[3]], offload_config_list[offload[4]], offload_config_list[offload[5]]]
    edge_core_config = [core_config_list[edge_core[0]], core_config_list[edge_core[1]], core_config_list[edge_core[2]], 
                        core_config_list[edge_core[3]], core_config_list[edge_core[4]], core_config_list[edge_core[5]]]
    network_config = network_config_list[network_type]
    print network_config
    

    sim_config(
                       total_number = 6, 
                       edge_type = offload_config,
                       edge_core_number = edge_core_config,
                       gateway_core_number = 4, 
                       network = network_config
                    )
    omnetpp_ini()
    cluster_ned()

    #recompile = 1
    remake_lwip()
    remake_runtime()
    remake_app()
    #recompile = 1

    call(["make", "test"])
    print "Simulation is finished"

    return get_latency_and_energy(6, edge_core_config)

    #store_result(6, network_config["type"], network_config["mode"], offload, edge_core, 4)


if __name__ == "__main__":
   evaluate_one()
   """   
   modulation = ["802.11", "802.15.4"]
   op_mode_list = [("g", "6Mbps"), ("b", "1Mbps")]
   edge_number_list = [2,4,6]
   offloading_options = ["0", "1", "2", "3"]
   device_type_list = [(1,1), (1,4), (4,4)]

   recompile = 1

   for network_type in modulation:
      for op_mode in op_mode_list:
         network_mode = op_mode[0] 
         bitrate = op_mode[1]
         for edge_number in edge_number_list:
            for offload in offloading_options:
               for device_type in device_type_list:
                  edge_core = device_type[0]
                  gateway_core = device_type[1]
                  print "==============recompile===============", recompile
                  print "network_type:", network_type
                  print "network_mode:", network_mode
                  print "bitrate:", bitrate
                  print "edge_number:", edge_number
                  print "offload:", offload
                  print "edge_core:", edge_core
                  print "gateway_core:", gateway_core
                  sim_config(
                       total_number = edge_number, 
                       edge_type = [offload, offload, offload, offload, offload, offload],
                       edge_core_number = [edge_core, edge_core, edge_core, edge_core, edge_core, edge_core],
                       gateway_core_number = gateway_core, 
                       network = {
                         "type": network_type,
                         "mode": network_mode, 
                         "bitrate": bitrate
                       }
                    )

                  omnetpp_ini()
                  cluster_ned()

                  if recompile == 1:
                     remake_lwip()
                     remake_runtime()
                     remake_app()

                  call(["make", "test"])
                  store_result(edge_number, network_type, network_mode, offload, edge_core, gateway_core)
                  recompile = 0

         if network_type == "802.15.4":
            break
      recompile = 1
   """
   """
   network_type = "802.15.4" #modulation = ["802.11", "802.15.4"]

   ##Only if network type is 802.11
   network_mode = "" #op_mode_list = [("g", "6Mbps"), ("b", "1Mbps")]
   bitrate = ""

   edge_number = 6 #edge_number_list = [2,4,6]
   offload = "3" #offloading_options["0", "1", "2", "3"]
   edge_core = 1 #device_type_list = [(1,1), (1,4), (4,4)]
   gateway_core = 4 

   sim_config(
                       total_number = edge_number, 
                       edge_type = [offload, offload, offload, offload, offload, offload],
                       edge_core_number = [edge_core, edge_core, edge_core, edge_core, edge_core, edge_core],
                       gateway_core_number = gateway_core, 
                       network = {
                         "type": network_type,
                         "mode": network_mode, 
                         "bitrate": bitrate
                       }
                    )
   omnetpp_ini()
   cluster_ned()
   remake_lwip()
   remake_runtime()
   remake_app()

   call(["make", "test"])
   store_result(edge_number, network_type, network_mode, offload, edge_core, gateway_core)
   """

   
   #evaluate_one()


