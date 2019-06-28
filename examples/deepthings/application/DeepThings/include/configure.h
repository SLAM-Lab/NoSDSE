#ifndef CONFIGURE_H
#define CONFIGURE_H

/*Partitioning paramters*/
#define FUSED_LAYERS_MAX 16
#define PARTITIONS_W_MAX 6
#define PARTITIONS_H_MAX 6
#define PARTITIONS_MAX 36
#define THREAD_NUM 1
#define DATA_REUSE 1

/*Generate debugging information in log file*/
#define DEBUG_LOG 1

/*Debugging information for different components*/
#define DEBUG_INFERENCE 0
#define DEBUG_FTP 0
#define DEBUG_SERIALIZATION 0
#define DEBUG_DEEP_GATEWAY 0
#define DEBUG_DEEP_EDGE 0

/*Print timing and communication size information*/
#define DEBUG_TIMING 1
#define DEBUG_COMMU_SIZE 1

/*Configuration parameters for DistrIoT*/
#define GATEWAY_PUBLIC_ADDR "10.157.89.51"
#define GATEWAY_LOCAL_ADDR "192.168.4.1"
#define EDGE_ADDR_LIST    {"192.168.4.9", "192.168.4.8", "192.168.4.4", "192.168.4.14", "192.168.4.15", "192.168.4.16", "192.168.4.6", "192.168.4.17", "192.168.4.18", "192.168.4.19", "192.168.4.20", "192.168.4.21"}
#define MAX_EDGE_NUM 12
#define FRAME_NUM 4

/*Computation-less implementation for timing simulation*/
#define NO_COMP 1

#endif
