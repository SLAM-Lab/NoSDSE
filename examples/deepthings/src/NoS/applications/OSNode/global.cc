#include <systemc.h>
#include "lwip_ctxt.h"
double power_cli[32];
double CliEnergy[32];

unsigned char debug_flags=LWIP_DBG_OFF;
int node_choice=5;

long total_sent_pkts[32];
long total_recvd_pkts[32];

int sc_main(int, char *[]){

    std::cout << "The sc_main should not be called ..." <<std::endl;
    return 0;
}
