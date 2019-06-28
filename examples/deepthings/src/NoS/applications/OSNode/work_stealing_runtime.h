#ifndef WORK_STEALING_RUNTIME_H
#define WORK_STEALING_RUNTIME_H

#include "darkiot.h"
#include "configure.h"
#include "cmd_line_parser.h"
#include "frame_partitioner.h"
#include "deepthings_edge.h"
#include "deepthings_gateway.h"
#include "json_config.h"
#include <string.h>

void test_deepthings_stealer_edge(uint32_t N, uint32_t M, uint32_t fused_layers, uint32_t edge_id);
void test_deepthings_victim_edge(uint32_t N, uint32_t M, uint32_t fused_layers, uint32_t edge_id);


/*------------------------------------------------------*/
/*---Test functions for distributed work stealing runtime system---*/
static void process_task(blob* temp, device_ctxt* ctxt);
void test_deepthings_gateway(uint32_t N, uint32_t M, uint32_t fused_layers, uint32_t total_edge_number);


#endif /*WORK_STEALING_RUNTIME_H*/

