#
# OMNeT++/OMNEST Makefile for INET
#
# This file was generated with the command:
#  opp_makemake -f --deep -o INET -O out --no-deep-includes -I. -I.. -I./NoS/applications -I./NoS/applications/OSNode -I/include -I./src/OSNode -I../../../tools/json -I/home/slam/OMNET/HCSim/include -I/home/slam/OMNET/lwip-hcsim/src/include -I/home/slam/OMNET/lwip-hcsim/ports/port/include -I/home/slam/OMNET/lwip-hcsim/src/include/ipv4 -I/home/slam/OMNET/lwip-hcsim/lwip/src -I/home/slam/OMNET/lwip-hcsim/ports/hcsim -I/home/slam/OMNET/lwip-hcsim/ports/hcsim/context -L/home/slam/OMNET/lwip-hcsim/ports -L/home/slam/OMNET/lwip-hcsim/ports/hcsim/context -L/home/slam/OMNET/HCSim/lib -I../runtime/include -I../runtime/src -I../runtime/hcsim -I../runtime/lwip -I../application/DeepThings/include -I../application/DeepThings/src -I../application/darknet-nnpack/include -I../application/darknet-nnpack/src -L../runtime -L../application -L../application/darknet-nnpack -I$(INET_PROJ)/src/inet/applications/ethernet -I$(INET_PROJ)/src/inet/common -I$(INET_PROJ)/src/inet/common/lifecycle -I$(INET_PROJ)/src/ -I$(INET_PROJ)/src/inet/linklayer/common -I$(INET_PROJ)/src/inet/linklayer/contract -I$(INET_PROJ)/src/inet/networklayer/common -I$(INET_PROJ)/src/inet/networklayer/contract -I$(INET_PROJ)/src/inet/networklayer/contract/ipv4 -I$(INET_PROJ)/src/inet/networklayer/contract/ipv6 -L$(INET_PROJ)/out/clang-debug/src -lINET -DSC_INCLUDE_DYNAMIC_PROCESSES -DINET_IMPORT -KINET_PROJ=/home/slam/OMNET/inet -DWITH_ETHERNET
#

# Name of target to be created (-o option)
TARGET = INET$(EXE_SUFFIX)

# User interface (uncomment one) (-u option)
USERIF_LIBS = $(ALL_ENV_LIBS) # that is, $(TKENV_LIBS) $(QTENV_LIBS) $(CMDENV_LIBS)
#USERIF_LIBS = $(CMDENV_LIBS)
#USERIF_LIBS = $(TKENV_LIBS)
#USERIF_LIBS = $(QTENV_LIBS)

# C++ include paths (with -I)
INCLUDE_PATH = \
    -I. \
    -I.. \
    -I./NoS/applications \
    -I./NoS/applications/OSNode \
    -I/include \
    -I./src/OSNode \
    -I../../../tools/json \
    -I/home/slam/OMNET/HCSim/include \
    -I/home/slam/OMNET/lwip-hcsim/src/include \
    -I/home/slam/OMNET/lwip-hcsim/ports/port/include \
    -I/home/slam/OMNET/lwip-hcsim/src/include/ipv4 \
    -I/home/slam/OMNET/lwip-hcsim/lwip/src \
    -I/home/slam/OMNET/lwip-hcsim/ports/hcsim \
    -I/home/slam/OMNET/lwip-hcsim/ports/hcsim/context \
    -I../runtime/include \
    -I../runtime/src \
    -I../runtime/hcsim \
    -I../runtime/lwip \
    -I../application/DeepThings/include \
    -I../application/DeepThings/src \
    -I../application/darknet-nnpack/include \
    -I../application/darknet-nnpack/src \
    -I$(INET_PROJ)/src/inet/applications/ethernet \
    -I$(INET_PROJ)/src/inet/common \
    -I$(INET_PROJ)/src/inet/common/lifecycle \
    -I$(INET_PROJ)/src/ \
    -I$(INET_PROJ)/src/inet/linklayer/common \
    -I$(INET_PROJ)/src/inet/linklayer/contract \
    -I$(INET_PROJ)/src/inet/networklayer/common \
    -I$(INET_PROJ)/src/inet/networklayer/contract \
    -I$(INET_PROJ)/src/inet/networklayer/contract/ipv4 \
    -I$(INET_PROJ)/src/inet/networklayer/contract/ipv6

# Additional object and library files to link with
EXTRA_OBJS =

# Additional libraries (-L, -l options)
LIBS = -L/home/slam/OMNET/lwip-hcsim/ports -L/home/slam/OMNET/lwip-hcsim/ports/hcsim/context -L/home/slam/OMNET/HCSim/lib -L../runtime -L../application -L../application/darknet-nnpack -L$(INET_PROJ)/out/clang-debug/src  -lINET
LIBS += -Wl,-rpath,`abspath /home/slam/OMNET/lwip-hcsim/ports` -Wl,-rpath,`abspath /home/slam/OMNET/lwip-hcsim/ports/hcsim/context` -Wl,-rpath,`abspath /home/slam/OMNET/HCSim/lib` -Wl,-rpath,`abspath ../runtime` -Wl,-rpath,`abspath ../application` -Wl,-rpath,`abspath ../application/darknet-nnpack` -Wl,-rpath,`abspath $(INET_PROJ)/out/clang-debug/src`

# Output directory
PROJECT_OUTPUT_DIR = out
PROJECTRELATIVE_PATH =
O = $(PROJECT_OUTPUT_DIR)/$(CONFIGNAME)/$(PROJECTRELATIVE_PATH)

# Object files for local .cc, .msg and .sm files
OBJS = \
    $O/NoS/applications/ethernet/CliWrapper.o \
    $O/NoS/applications/ethernet/SmartAP.o \
    $O/NoS/applications/ethernet/SrvWrapper.o \
    $O/NoS/applications/OSNode/global.o \
    $O/NoS/applications/OSNode/json_config.o \
    $O/NoS/applications/OSNode/OmnetIf_pkt.o \
    $O/NoS/applications/OSNode/work_stealing_runtime.o \
    $O/NoS/applications/ethernet/EtherWrapper_m.o

# Message files
MSGFILES = \
    NoS/applications/ethernet/EtherWrapper.msg

# SM files
SMFILES =

# Other makefile variables (-K)
INET_PROJ=/home/slam/OMNET/inet

#------------------------------------------------------------------------------

# Pull in OMNeT++ configuration (Makefile.inc or configuser.vc)

ifneq ("$(OMNETPP_CONFIGFILE)","")
CONFIGFILE = $(OMNETPP_CONFIGFILE)
else
ifneq ("$(OMNETPP_ROOT)","")
CONFIGFILE = $(OMNETPP_ROOT)/Makefile.inc
else
CONFIGFILE = $(shell opp_configfilepath)
endif
endif

ifeq ("$(wildcard $(CONFIGFILE))","")
$(error Config file '$(CONFIGFILE)' does not exist -- add the OMNeT++ bin directory to the path so that opp_configfilepath can be found, or set the OMNETPP_CONFIGFILE variable to point to Makefile.inc)
endif

include $(CONFIGFILE)

# Simulation kernel and user interface libraries
OMNETPP_LIB_SUBDIR = $(OMNETPP_LIB_DIR)/$(TOOLCHAIN_NAME)
OMNETPP_LIBS = -L"$(OMNETPP_LIB_SUBDIR)" -L"$(OMNETPP_LIB_DIR)" -loppmain$D $(USERIF_LIBS) $(KERNEL_LIBS) $(SYS_LIBS)

COPTS = $(CFLAGS) -DSC_INCLUDE_DYNAMIC_PROCESSES -DINET_IMPORT -DWITH_ETHERNET $(INCLUDE_PATH) -I$(OMNETPP_INCL_DIR)
MSGCOPTS = $(INCLUDE_PATH)
SMCOPTS =

# we want to recompile everything if COPTS changes,
# so we store COPTS into $COPTS_FILE and have object
# files depend on it (except when "make depend" was called)
COPTS_FILE = $O/.last-copts
ifneq ($(MAKECMDGOALS),depend)
ifneq ("$(COPTS)","$(shell cat $(COPTS_FILE) 2>/dev/null || echo '')")
$(shell $(MKPATH) "$O" && echo "$(COPTS)" >$(COPTS_FILE))
endif
endif

#------------------------------------------------------------------------------
# User-supplied makefile fragment(s)
# >>>
# inserted from file 'makefrag':
#
# pkg-config:
#
HAVE_PKGCFG := $(shell pkg-config --version 2>/dev/null)
ifeq ($(strip $(HAVE_PKGCFG)),)
  HAVE_PKGCFG := no
else
  HAVE_PKGCFG := yes
  PKGCFG := $(shell which pkg-config)
endif

# uncomment this if you want to run the NS3 vs INET 802.11 cross validation tests in the 'tests/misc/ns3' folder.
# CFLAGS += -DNS3_VALIDATION

# disable anoying "... hides overloaded virtual function" warning
CFLAGS += -Wno-overloaded-virtual

LIBS += -ldeepthings -ldarknet -ldistriot -llwipapps -llwip4 -loppsystemc$D -lhcsim -lrt

# <<<
#------------------------------------------------------------------------------

# Main target
all: $O/$(TARGET)
	$(Q)$(LN) $O/$(TARGET) .

$O/$(TARGET): $(OBJS)  $(wildcard $(EXTRA_OBJS)) Makefile
	@$(MKPATH) $O
	@echo Creating executable: $@
	$(Q)$(CXX) $(LDFLAGS) -o $O/$(TARGET)  $(OBJS) $(EXTRA_OBJS) $(AS_NEEDED_OFF) $(WHOLE_ARCHIVE_ON) $(LIBS) $(WHOLE_ARCHIVE_OFF) $(OMNETPP_LIBS)

.PHONY: all clean cleanall depend msgheaders smheaders

.SUFFIXES: .cc

$O/%.o: %.cc $(COPTS_FILE)
	@$(MKPATH) $(dir $@)
	$(qecho) "$<"
	$(Q)$(CXX) -c $(CXXFLAGS) $(COPTS) -o $@ $<

%_m.cc %_m.h: %.msg
	$(qecho) MSGC: $<
	$(Q)$(MSGC) -s _m.cc $(MSGCOPTS) $?

%_sm.cc %_sm.h: %.sm
	$(qecho) SMC: $<
	$(Q)$(SMC) -c++ -suffix cc $(SMCOPTS) $?

msgheaders: $(MSGFILES:.msg=_m.h)

smheaders: $(SMFILES:.sm=_sm.h)

clean:
	$(qecho) Cleaning...
	$(Q)-rm -rf $O
	$(Q)-rm -f INET INET.exe libINET.so libINET.a libINET.dll libINET.dylib
	$(Q)-rm -f ./*_m.cc ./*_m.h ./*_sm.cc ./*_sm.h
	$(Q)-rm -f data/*_m.cc data/*_m.h data/*_sm.cc data/*_sm.h
	$(Q)-rm -f data/input/*_m.cc data/input/*_m.h data/input/*_sm.cc data/input/*_sm.h
	$(Q)-rm -f data/labels/*_m.cc data/labels/*_m.h data/labels/*_sm.cc data/labels/*_sm.h
	$(Q)-rm -f models/*_m.cc models/*_m.h models/*_sm.cc models/*_sm.h
	$(Q)-rm -f NoS/*_m.cc NoS/*_m.h NoS/*_sm.cc NoS/*_sm.h
	$(Q)-rm -f NoS/applications/*_m.cc NoS/applications/*_m.h NoS/applications/*_sm.cc NoS/applications/*_sm.h
	$(Q)-rm -f NoS/applications/ethernet/*_m.cc NoS/applications/ethernet/*_m.h NoS/applications/ethernet/*_sm.cc NoS/applications/ethernet/*_sm.h
	$(Q)-rm -f NoS/applications/OSNode/*_m.cc NoS/applications/OSNode/*_m.h NoS/applications/OSNode/*_sm.cc NoS/applications/OSNode/*_sm.h
	$(Q)-rm -f profile/*_m.cc profile/*_m.h profile/*_sm.cc profile/*_sm.h
	$(Q)-rm -f profile/1_core/*_m.cc profile/1_core/*_m.h profile/1_core/*_sm.cc profile/1_core/*_sm.h
	$(Q)-rm -f profile/2_core/*_m.cc profile/2_core/*_m.h profile/2_core/*_sm.cc profile/2_core/*_sm.h
	$(Q)-rm -f profile/4_core/*_m.cc profile/4_core/*_m.h profile/4_core/*_sm.cc profile/4_core/*_sm.h

cleanall: clean
	$(Q)-rm -rf $(PROJECT_OUTPUT_DIR)

depend:
	$(qecho) Creating dependencies...
	$(Q)$(MAKEDEPEND) $(INCLUDE_PATH) -f Makefile -P\$$O/ -- $(MSG_CC_FILES) $(SM_CC_FILES)  ./*.cc data/*.cc data/input/*.cc data/labels/*.cc models/*.cc NoS/*.cc NoS/applications/*.cc NoS/applications/ethernet/*.cc NoS/applications/OSNode/*.cc profile/*.cc profile/1_core/*.cc profile/2_core/*.cc profile/4_core/*.cc

# DO NOT DELETE THIS LINE -- make depend depends on it.
$O/NoS/applications/ethernet/CliWrapper.o: NoS/applications/ethernet/CliWrapper.cc \
  ../../../tools/json/rapidjson/allocators.h \
  ../../../tools/json/rapidjson/document.h \
  ../../../tools/json/rapidjson/encodedstream.h \
  ../../../tools/json/rapidjson/encodings.h \
  ../../../tools/json/rapidjson/error/../msinttypes/inttypes.h \
  ../../../tools/json/rapidjson/error/../msinttypes/stdint.h \
  ../../../tools/json/rapidjson/error/../rapidjson.h \
  ../../../tools/json/rapidjson/error/en.h \
  ../../../tools/json/rapidjson/error/error.h \
  ../../../tools/json/rapidjson/filereadstream.h \
  ../../../tools/json/rapidjson/filewritestream.h \
  ../../../tools/json/rapidjson/internal/../allocators.h \
  ../../../tools/json/rapidjson/internal/../encodings.h \
  ../../../tools/json/rapidjson/internal/../msinttypes/inttypes.h \
  ../../../tools/json/rapidjson/internal/../msinttypes/stdint.h \
  ../../../tools/json/rapidjson/internal/../rapidjson.h \
  ../../../tools/json/rapidjson/internal/../stream.h \
  ../../../tools/json/rapidjson/internal/biginteger.h \
  ../../../tools/json/rapidjson/internal/diyfp.h \
  ../../../tools/json/rapidjson/internal/dtoa.h \
  ../../../tools/json/rapidjson/internal/ieee754.h \
  ../../../tools/json/rapidjson/internal/itoa.h \
  ../../../tools/json/rapidjson/internal/meta.h \
  ../../../tools/json/rapidjson/internal/pow10.h \
  ../../../tools/json/rapidjson/internal/stack.h \
  ../../../tools/json/rapidjson/internal/strfunc.h \
  ../../../tools/json/rapidjson/internal/strtod.h \
  ../../../tools/json/rapidjson/internal/swap.h \
  ../../../tools/json/rapidjson/memorystream.h \
  ../../../tools/json/rapidjson/msinttypes/inttypes.h \
  ../../../tools/json/rapidjson/msinttypes/stdint.h \
  ../../../tools/json/rapidjson/prettywriter.h \
  ../../../tools/json/rapidjson/rapidjson.h \
  ../../../tools/json/rapidjson/reader.h \
  ../../../tools/json/rapidjson/stream.h \
  ../../../tools/json/rapidjson/stringbuffer.h \
  ../../../tools/json/rapidjson/writer.h \
  ../application/DeepThings/include/configure.h \
  ../application/DeepThings/src/cmd_line_parser.h \
  ../application/DeepThings/src/deepthings_edge.h \
  ../application/DeepThings/src/deepthings_gateway.h \
  ../application/DeepThings/src/frame_partitioner.h \
  ../application/DeepThings/src/ftp.h \
  ../application/DeepThings/src/inference_engine_helper.h \
  ../application/darknet-nnpack/include/darknet.h \
  ../application/darknet-nnpack/src/activation_layer.h \
  ../application/darknet-nnpack/src/activations.h \
  ../application/darknet-nnpack/src/avgpool_layer.h \
  ../application/darknet-nnpack/src/batchnorm_layer.h \
  ../application/darknet-nnpack/src/blas.h \
  ../application/darknet-nnpack/src/box.h \
  ../application/darknet-nnpack/src/connected_layer.h \
  ../application/darknet-nnpack/src/convolutional_layer.h \
  ../application/darknet-nnpack/src/cost_layer.h \
  ../application/darknet-nnpack/src/crnn_layer.h \
  ../application/darknet-nnpack/src/crop_layer.h \
  ../application/darknet-nnpack/src/cuda.h \
  ../application/darknet-nnpack/src/data.h \
  ../application/darknet-nnpack/src/detection_layer.h \
  ../application/darknet-nnpack/src/dropout_layer.h \
  ../application/darknet-nnpack/src/gru_layer.h \
  ../application/darknet-nnpack/src/image.h \
  ../application/darknet-nnpack/src/layer.h \
  ../application/darknet-nnpack/src/list.h \
  ../application/darknet-nnpack/src/local_layer.h \
  ../application/darknet-nnpack/src/matrix.h \
  ../application/darknet-nnpack/src/maxpool_layer.h \
  ../application/darknet-nnpack/src/network.h \
  ../application/darknet-nnpack/src/normalization_layer.h \
  ../application/darknet-nnpack/src/option_list.h \
  ../application/darknet-nnpack/src/parser.h \
  ../application/darknet-nnpack/src/region_layer.h \
  ../application/darknet-nnpack/src/reorg_layer.h \
  ../application/darknet-nnpack/src/rnn_layer.h \
  ../application/darknet-nnpack/src/route_layer.h \
  ../application/darknet-nnpack/src/shortcut_layer.h \
  ../application/darknet-nnpack/src/softmax_layer.h \
  ../application/darknet-nnpack/src/tree.h \
  ../application/darknet-nnpack/src/utils.h \
  ../runtime/hcsim/thread_util.h \
  ../runtime/include/darkiot.h \
  ../runtime/lwip/lwip_ctxt.h \
  ../runtime/lwip/network_util.h \
  ../runtime/src/client.h \
  ../runtime/src/data_blob.h \
  ../runtime/src/exec_ctrl.h \
  ../runtime/src/gateway.h \
  ../runtime/src/global_context.h \
  ../runtime/src/thread_safe_queue.h \
  ./NoS/applications/OSNode/AppTasks.h \
  ./NoS/applications/OSNode/MCProcessor.h \
  ./NoS/applications/OSNode/Nic.h \
  ./NoS/applications/OSNode/NicDriver.h \
  ./NoS/applications/OSNode/OmnetIf_pkt.h \
  ./NoS/applications/OSNode/config.h \
  ./NoS/applications/OSNode/json_config.h \
  ./NoS/applications/OSNode/top_module.h \
  ./NoS/applications/OSNode/work_stealing_runtime.h \
  /home/slam/OMNET/HCSim/include/Channels/adapters_TLM.h \
  /home/slam/OMNET/HCSim/include/Channels/ambaAhb.h \
  /home/slam/OMNET/HCSim/include/Channels/ambaAhb_if.h \
  /home/slam/OMNET/HCSim/include/Channels/global_ambaAhb.h \
  /home/slam/OMNET/HCSim/include/Channels/handshake_ch.h \
  /home/slam/OMNET/HCSim/include/Channels/handshake_os_ch.h \
  /home/slam/OMNET/HCSim/include/Channels/receive_if.h \
  /home/slam/OMNET/HCSim/include/Channels/receive_os_if.h \
  /home/slam/OMNET/HCSim/include/Channels/sc_mutex_os.h \
  /home/slam/OMNET/HCSim/include/Channels/sc_mutex_os_if.h \
  /home/slam/OMNET/HCSim/include/Channels/send_if.h \
  /home/slam/OMNET/HCSim/include/Channels/send_os_if.h \
  /home/slam/OMNET/HCSim/include/Channels/simpleBus_TLM.h \
  /home/slam/OMNET/HCSim/include/HCSim.h \
  /home/slam/OMNET/HCSim/include/OS/OSAPI.h \
  /home/slam/OMNET/HCSim/include/OS/PRTOS.h \
  /home/slam/OMNET/HCSim/include/OS/global_os.h \
  /home/slam/OMNET/HCSim/include/Processor/GenericIntrController.h \
  /home/slam/OMNET/HCSim/include/Processor/GenericIntrController_TLM.h \
  /home/slam/OMNET/HCSim/include/Processor/MCProcessor_FM.h \
  /home/slam/OMNET/HCSim/include/Processor/global_gic.h \
  /home/slam/OMNET/HCSim/include/Processor/interrupt_if.h \
  /home/slam/OMNET/HCSim/include/sim_config.h \
  /home/slam/OMNET/inet/src//inet/common/Compat.h \
  /home/slam/OMNET/inet/src//inet/common/INETDefs.h \
  /home/slam/OMNET/inet/src//inet/common/InitStages.h \
  /home/slam/OMNET/inet/src//inet/common/ModuleAccess.h \
  /home/slam/OMNET/inet/src//inet/common/NotifierConsts.h \
  /home/slam/OMNET/inet/src//inet/common/lifecycle/ILifecycle.h \
  /home/slam/OMNET/inet/src//inet/common/lifecycle/LifecycleOperation.h \
  /home/slam/OMNET/inet/src//inet/common/lifecycle/NodeOperations.h \
  /home/slam/OMNET/inet/src//inet/common/lifecycle/NodeStatus.h \
  /home/slam/OMNET/inet/src//inet/features.h \
  /home/slam/OMNET/inet/src//inet/linklayer/common/Ieee802Ctrl.h \
  /home/slam/OMNET/inet/src//inet/linklayer/common/Ieee802Ctrl_m.h \
  /home/slam/OMNET/inet/src//inet/linklayer/common/MACAddress.h \
  /home/slam/OMNET/inet/src//inet/linklayer/contract/IMACProtocolControlInfo.h \
  /home/slam/OMNET/inet/src//inet/networklayer/common/InterfaceEntry.h \
  /home/slam/OMNET/inet/src//inet/networklayer/common/InterfaceToken.h \
  /home/slam/OMNET/inet/src//inet/networklayer/common/L3Address.h \
  /home/slam/OMNET/inet/src//inet/networklayer/common/ModuleIdAddress.h \
  /home/slam/OMNET/inet/src//inet/networklayer/common/ModulePathAddress.h \
  /home/slam/OMNET/inet/src//inet/networklayer/contract/IInterfaceTable.h \
  /home/slam/OMNET/inet/src//inet/networklayer/contract/ipv4/IPv4Address.h \
  /home/slam/OMNET/inet/src//inet/networklayer/contract/ipv6/IPv6Address.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/app_utils.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/annotation.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/cluster_config.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/os_ctxt.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/profile_data.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/sim_results.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/lwip_ctxt.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/lwipopts.h \
  /home/slam/OMNET/lwip-hcsim/ports/port/include/arch/cc.h \
  /home/slam/OMNET/lwip-hcsim/ports/port/include/arch/perf.h \
  /home/slam/OMNET/lwip-hcsim/ports/port/include/arch/sys_arch.h \
  /home/slam/OMNET/lwip-hcsim/ports/port/include/netif/hcsim_if.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/arch.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/debug.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/def.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/err.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/errno.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/etharp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/icmp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/icmp6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/inet.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/init.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip4.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip4_addr.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip4_frag.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip6_addr.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip6_frag.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip_addr.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/mem.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/memp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/nd6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/netif.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/opt.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/pbuf.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/memp_priv.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/memp_std.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/nd6_priv.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/tcp_priv.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/tcpip_priv.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/etharp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/ethernet.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/icmp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/icmp6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/ip.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/ip4.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/ip6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/nd6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/tcp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/udp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/raw.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/sockets.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/stats.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/sys.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/tcp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/tcpip.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/timeouts.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/udp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/etharp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/ethernet.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/lowpan6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/lowpan6_common.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/lowpan6_opts.h \
  NoS/applications/ethernet/CliWrapper.h \
  NoS/applications/ethernet/EtherWrapper_m.h
$O/NoS/applications/ethernet/SmartAP.o: NoS/applications/ethernet/SmartAP.cc \
  ../../../tools/json/rapidjson/allocators.h \
  ../../../tools/json/rapidjson/document.h \
  ../../../tools/json/rapidjson/encodedstream.h \
  ../../../tools/json/rapidjson/encodings.h \
  ../../../tools/json/rapidjson/error/../msinttypes/inttypes.h \
  ../../../tools/json/rapidjson/error/../msinttypes/stdint.h \
  ../../../tools/json/rapidjson/error/../rapidjson.h \
  ../../../tools/json/rapidjson/error/en.h \
  ../../../tools/json/rapidjson/error/error.h \
  ../../../tools/json/rapidjson/filereadstream.h \
  ../../../tools/json/rapidjson/filewritestream.h \
  ../../../tools/json/rapidjson/internal/../allocators.h \
  ../../../tools/json/rapidjson/internal/../encodings.h \
  ../../../tools/json/rapidjson/internal/../msinttypes/inttypes.h \
  ../../../tools/json/rapidjson/internal/../msinttypes/stdint.h \
  ../../../tools/json/rapidjson/internal/../rapidjson.h \
  ../../../tools/json/rapidjson/internal/../stream.h \
  ../../../tools/json/rapidjson/internal/biginteger.h \
  ../../../tools/json/rapidjson/internal/diyfp.h \
  ../../../tools/json/rapidjson/internal/dtoa.h \
  ../../../tools/json/rapidjson/internal/ieee754.h \
  ../../../tools/json/rapidjson/internal/itoa.h \
  ../../../tools/json/rapidjson/internal/meta.h \
  ../../../tools/json/rapidjson/internal/pow10.h \
  ../../../tools/json/rapidjson/internal/stack.h \
  ../../../tools/json/rapidjson/internal/strfunc.h \
  ../../../tools/json/rapidjson/internal/strtod.h \
  ../../../tools/json/rapidjson/internal/swap.h \
  ../../../tools/json/rapidjson/memorystream.h \
  ../../../tools/json/rapidjson/msinttypes/inttypes.h \
  ../../../tools/json/rapidjson/msinttypes/stdint.h \
  ../../../tools/json/rapidjson/prettywriter.h \
  ../../../tools/json/rapidjson/rapidjson.h \
  ../../../tools/json/rapidjson/reader.h \
  ../../../tools/json/rapidjson/stream.h \
  ../../../tools/json/rapidjson/stringbuffer.h \
  ../../../tools/json/rapidjson/writer.h \
  ../application/DeepThings/include/configure.h \
  ../application/DeepThings/src/cmd_line_parser.h \
  ../application/DeepThings/src/deepthings_edge.h \
  ../application/DeepThings/src/deepthings_gateway.h \
  ../application/DeepThings/src/frame_partitioner.h \
  ../application/DeepThings/src/ftp.h \
  ../application/DeepThings/src/inference_engine_helper.h \
  ../application/darknet-nnpack/include/darknet.h \
  ../application/darknet-nnpack/src/activation_layer.h \
  ../application/darknet-nnpack/src/activations.h \
  ../application/darknet-nnpack/src/avgpool_layer.h \
  ../application/darknet-nnpack/src/batchnorm_layer.h \
  ../application/darknet-nnpack/src/blas.h \
  ../application/darknet-nnpack/src/box.h \
  ../application/darknet-nnpack/src/connected_layer.h \
  ../application/darknet-nnpack/src/convolutional_layer.h \
  ../application/darknet-nnpack/src/cost_layer.h \
  ../application/darknet-nnpack/src/crnn_layer.h \
  ../application/darknet-nnpack/src/crop_layer.h \
  ../application/darknet-nnpack/src/cuda.h \
  ../application/darknet-nnpack/src/data.h \
  ../application/darknet-nnpack/src/detection_layer.h \
  ../application/darknet-nnpack/src/dropout_layer.h \
  ../application/darknet-nnpack/src/gru_layer.h \
  ../application/darknet-nnpack/src/image.h \
  ../application/darknet-nnpack/src/layer.h \
  ../application/darknet-nnpack/src/list.h \
  ../application/darknet-nnpack/src/local_layer.h \
  ../application/darknet-nnpack/src/matrix.h \
  ../application/darknet-nnpack/src/maxpool_layer.h \
  ../application/darknet-nnpack/src/network.h \
  ../application/darknet-nnpack/src/normalization_layer.h \
  ../application/darknet-nnpack/src/option_list.h \
  ../application/darknet-nnpack/src/parser.h \
  ../application/darknet-nnpack/src/region_layer.h \
  ../application/darknet-nnpack/src/reorg_layer.h \
  ../application/darknet-nnpack/src/rnn_layer.h \
  ../application/darknet-nnpack/src/route_layer.h \
  ../application/darknet-nnpack/src/shortcut_layer.h \
  ../application/darknet-nnpack/src/softmax_layer.h \
  ../application/darknet-nnpack/src/tree.h \
  ../application/darknet-nnpack/src/utils.h \
  ../runtime/hcsim/thread_util.h \
  ../runtime/include/darkiot.h \
  ../runtime/lwip/lwip_ctxt.h \
  ../runtime/lwip/network_util.h \
  ../runtime/src/client.h \
  ../runtime/src/data_blob.h \
  ../runtime/src/exec_ctrl.h \
  ../runtime/src/gateway.h \
  ../runtime/src/global_context.h \
  ../runtime/src/thread_safe_queue.h \
  ./NoS/applications/OSNode/AppTasks.h \
  ./NoS/applications/OSNode/MCProcessor.h \
  ./NoS/applications/OSNode/Nic.h \
  ./NoS/applications/OSNode/NicDriver.h \
  ./NoS/applications/OSNode/OmnetIf_pkt.h \
  ./NoS/applications/OSNode/config.h \
  ./NoS/applications/OSNode/json_config.h \
  ./NoS/applications/OSNode/top_module.h \
  ./NoS/applications/OSNode/work_stealing_runtime.h \
  /home/slam/OMNET/HCSim/include/Channels/adapters_TLM.h \
  /home/slam/OMNET/HCSim/include/Channels/ambaAhb.h \
  /home/slam/OMNET/HCSim/include/Channels/ambaAhb_if.h \
  /home/slam/OMNET/HCSim/include/Channels/global_ambaAhb.h \
  /home/slam/OMNET/HCSim/include/Channels/handshake_ch.h \
  /home/slam/OMNET/HCSim/include/Channels/handshake_os_ch.h \
  /home/slam/OMNET/HCSim/include/Channels/receive_if.h \
  /home/slam/OMNET/HCSim/include/Channels/receive_os_if.h \
  /home/slam/OMNET/HCSim/include/Channels/sc_mutex_os.h \
  /home/slam/OMNET/HCSim/include/Channels/sc_mutex_os_if.h \
  /home/slam/OMNET/HCSim/include/Channels/send_if.h \
  /home/slam/OMNET/HCSim/include/Channels/send_os_if.h \
  /home/slam/OMNET/HCSim/include/Channels/simpleBus_TLM.h \
  /home/slam/OMNET/HCSim/include/HCSim.h \
  /home/slam/OMNET/HCSim/include/OS/OSAPI.h \
  /home/slam/OMNET/HCSim/include/OS/PRTOS.h \
  /home/slam/OMNET/HCSim/include/OS/global_os.h \
  /home/slam/OMNET/HCSim/include/Processor/GenericIntrController.h \
  /home/slam/OMNET/HCSim/include/Processor/GenericIntrController_TLM.h \
  /home/slam/OMNET/HCSim/include/Processor/MCProcessor_FM.h \
  /home/slam/OMNET/HCSim/include/Processor/global_gic.h \
  /home/slam/OMNET/HCSim/include/Processor/interrupt_if.h \
  /home/slam/OMNET/HCSim/include/sim_config.h \
  /home/slam/OMNET/inet/src//inet/common/Compat.h \
  /home/slam/OMNET/inet/src//inet/common/INETDefs.h \
  /home/slam/OMNET/inet/src//inet/common/InitStages.h \
  /home/slam/OMNET/inet/src//inet/common/LayeredProtocolBase.h \
  /home/slam/OMNET/inet/src//inet/common/ModuleAccess.h \
  /home/slam/OMNET/inet/src//inet/common/NotifierConsts.h \
  /home/slam/OMNET/inet/src//inet/common/lifecycle/ILifecycle.h \
  /home/slam/OMNET/inet/src//inet/common/lifecycle/LifecycleOperation.h \
  /home/slam/OMNET/inet/src//inet/common/lifecycle/NodeOperations.h \
  /home/slam/OMNET/inet/src//inet/common/lifecycle/NodeStatus.h \
  /home/slam/OMNET/inet/src//inet/common/lifecycle/OperationalBase.h \
  /home/slam/OMNET/inet/src//inet/features.h \
  /home/slam/OMNET/inet/src//inet/linklayer/common/Ieee802Ctrl.h \
  /home/slam/OMNET/inet/src//inet/linklayer/common/Ieee802Ctrl_m.h \
  /home/slam/OMNET/inet/src//inet/linklayer/common/MACAddress.h \
  /home/slam/OMNET/inet/src//inet/linklayer/configurator/Ieee8021dInterfaceData.h \
  /home/slam/OMNET/inet/src//inet/linklayer/contract/IMACProtocolControlInfo.h \
  /home/slam/OMNET/inet/src//inet/linklayer/ethernet/EtherFrame_m.h \
  /home/slam/OMNET/inet/src//inet/linklayer/ethernet/Ethernet.h \
  /home/slam/OMNET/inet/src//inet/linklayer/ethernet/switch/IMACAddressTable.h \
  /home/slam/OMNET/inet/src//inet/networklayer/common/InterfaceEntry.h \
  /home/slam/OMNET/inet/src//inet/networklayer/common/InterfaceTable.h \
  /home/slam/OMNET/inet/src//inet/networklayer/common/InterfaceToken.h \
  /home/slam/OMNET/inet/src//inet/networklayer/common/L3Address.h \
  /home/slam/OMNET/inet/src//inet/networklayer/common/ModuleIdAddress.h \
  /home/slam/OMNET/inet/src//inet/networklayer/common/ModulePathAddress.h \
  /home/slam/OMNET/inet/src//inet/networklayer/contract/IInterfaceTable.h \
  /home/slam/OMNET/inet/src//inet/networklayer/contract/ipv4/IPv4Address.h \
  /home/slam/OMNET/inet/src//inet/networklayer/contract/ipv6/IPv6Address.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/app_utils.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/annotation.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/cluster_config.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/os_ctxt.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/profile_data.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/sim_results.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/lwip_ctxt.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/lwipopts.h \
  /home/slam/OMNET/lwip-hcsim/ports/port/include/arch/cc.h \
  /home/slam/OMNET/lwip-hcsim/ports/port/include/arch/perf.h \
  /home/slam/OMNET/lwip-hcsim/ports/port/include/arch/sys_arch.h \
  /home/slam/OMNET/lwip-hcsim/ports/port/include/netif/hcsim_if.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/arch.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/debug.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/def.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/err.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/errno.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/etharp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/icmp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/icmp6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/inet.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/init.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip4.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip4_addr.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip4_frag.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip6_addr.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip6_frag.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip_addr.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/mem.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/memp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/nd6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/netif.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/opt.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/pbuf.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/memp_priv.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/memp_std.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/nd6_priv.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/tcp_priv.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/tcpip_priv.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/etharp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/ethernet.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/icmp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/icmp6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/ip.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/ip4.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/ip6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/nd6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/tcp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/udp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/raw.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/sockets.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/stats.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/sys.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/tcp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/tcpip.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/timeouts.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/udp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/etharp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/ethernet.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/lowpan6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/lowpan6_common.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/lowpan6_opts.h \
  NoS/applications/ethernet/EtherWrapper_m.h \
  NoS/applications/ethernet/SmartAP.h
$O/NoS/applications/ethernet/SrvWrapper.o: NoS/applications/ethernet/SrvWrapper.cc \
  ../../../tools/json/rapidjson/allocators.h \
  ../../../tools/json/rapidjson/document.h \
  ../../../tools/json/rapidjson/encodedstream.h \
  ../../../tools/json/rapidjson/encodings.h \
  ../../../tools/json/rapidjson/error/../msinttypes/inttypes.h \
  ../../../tools/json/rapidjson/error/../msinttypes/stdint.h \
  ../../../tools/json/rapidjson/error/../rapidjson.h \
  ../../../tools/json/rapidjson/error/en.h \
  ../../../tools/json/rapidjson/error/error.h \
  ../../../tools/json/rapidjson/filereadstream.h \
  ../../../tools/json/rapidjson/filewritestream.h \
  ../../../tools/json/rapidjson/internal/../allocators.h \
  ../../../tools/json/rapidjson/internal/../encodings.h \
  ../../../tools/json/rapidjson/internal/../msinttypes/inttypes.h \
  ../../../tools/json/rapidjson/internal/../msinttypes/stdint.h \
  ../../../tools/json/rapidjson/internal/../rapidjson.h \
  ../../../tools/json/rapidjson/internal/../stream.h \
  ../../../tools/json/rapidjson/internal/biginteger.h \
  ../../../tools/json/rapidjson/internal/diyfp.h \
  ../../../tools/json/rapidjson/internal/dtoa.h \
  ../../../tools/json/rapidjson/internal/ieee754.h \
  ../../../tools/json/rapidjson/internal/itoa.h \
  ../../../tools/json/rapidjson/internal/meta.h \
  ../../../tools/json/rapidjson/internal/pow10.h \
  ../../../tools/json/rapidjson/internal/stack.h \
  ../../../tools/json/rapidjson/internal/strfunc.h \
  ../../../tools/json/rapidjson/internal/strtod.h \
  ../../../tools/json/rapidjson/internal/swap.h \
  ../../../tools/json/rapidjson/memorystream.h \
  ../../../tools/json/rapidjson/msinttypes/inttypes.h \
  ../../../tools/json/rapidjson/msinttypes/stdint.h \
  ../../../tools/json/rapidjson/prettywriter.h \
  ../../../tools/json/rapidjson/rapidjson.h \
  ../../../tools/json/rapidjson/reader.h \
  ../../../tools/json/rapidjson/stream.h \
  ../../../tools/json/rapidjson/stringbuffer.h \
  ../../../tools/json/rapidjson/writer.h \
  ../application/DeepThings/include/configure.h \
  ../application/DeepThings/src/cmd_line_parser.h \
  ../application/DeepThings/src/deepthings_edge.h \
  ../application/DeepThings/src/deepthings_gateway.h \
  ../application/DeepThings/src/frame_partitioner.h \
  ../application/DeepThings/src/ftp.h \
  ../application/DeepThings/src/inference_engine_helper.h \
  ../application/darknet-nnpack/include/darknet.h \
  ../application/darknet-nnpack/src/activation_layer.h \
  ../application/darknet-nnpack/src/activations.h \
  ../application/darknet-nnpack/src/avgpool_layer.h \
  ../application/darknet-nnpack/src/batchnorm_layer.h \
  ../application/darknet-nnpack/src/blas.h \
  ../application/darknet-nnpack/src/box.h \
  ../application/darknet-nnpack/src/connected_layer.h \
  ../application/darknet-nnpack/src/convolutional_layer.h \
  ../application/darknet-nnpack/src/cost_layer.h \
  ../application/darknet-nnpack/src/crnn_layer.h \
  ../application/darknet-nnpack/src/crop_layer.h \
  ../application/darknet-nnpack/src/cuda.h \
  ../application/darknet-nnpack/src/data.h \
  ../application/darknet-nnpack/src/detection_layer.h \
  ../application/darknet-nnpack/src/dropout_layer.h \
  ../application/darknet-nnpack/src/gru_layer.h \
  ../application/darknet-nnpack/src/image.h \
  ../application/darknet-nnpack/src/layer.h \
  ../application/darknet-nnpack/src/list.h \
  ../application/darknet-nnpack/src/local_layer.h \
  ../application/darknet-nnpack/src/matrix.h \
  ../application/darknet-nnpack/src/maxpool_layer.h \
  ../application/darknet-nnpack/src/network.h \
  ../application/darknet-nnpack/src/normalization_layer.h \
  ../application/darknet-nnpack/src/option_list.h \
  ../application/darknet-nnpack/src/parser.h \
  ../application/darknet-nnpack/src/region_layer.h \
  ../application/darknet-nnpack/src/reorg_layer.h \
  ../application/darknet-nnpack/src/rnn_layer.h \
  ../application/darknet-nnpack/src/route_layer.h \
  ../application/darknet-nnpack/src/shortcut_layer.h \
  ../application/darknet-nnpack/src/softmax_layer.h \
  ../application/darknet-nnpack/src/tree.h \
  ../application/darknet-nnpack/src/utils.h \
  ../runtime/hcsim/thread_util.h \
  ../runtime/include/darkiot.h \
  ../runtime/lwip/lwip_ctxt.h \
  ../runtime/lwip/network_util.h \
  ../runtime/src/client.h \
  ../runtime/src/data_blob.h \
  ../runtime/src/exec_ctrl.h \
  ../runtime/src/gateway.h \
  ../runtime/src/global_context.h \
  ../runtime/src/thread_safe_queue.h \
  ./NoS/applications/OSNode/AppTasks.h \
  ./NoS/applications/OSNode/MCProcessor.h \
  ./NoS/applications/OSNode/Nic.h \
  ./NoS/applications/OSNode/NicDriver.h \
  ./NoS/applications/OSNode/OmnetIf_pkt.h \
  ./NoS/applications/OSNode/config.h \
  ./NoS/applications/OSNode/json_config.h \
  ./NoS/applications/OSNode/top_module.h \
  ./NoS/applications/OSNode/work_stealing_runtime.h \
  /home/slam/OMNET/HCSim/include/Channels/adapters_TLM.h \
  /home/slam/OMNET/HCSim/include/Channels/ambaAhb.h \
  /home/slam/OMNET/HCSim/include/Channels/ambaAhb_if.h \
  /home/slam/OMNET/HCSim/include/Channels/global_ambaAhb.h \
  /home/slam/OMNET/HCSim/include/Channels/handshake_ch.h \
  /home/slam/OMNET/HCSim/include/Channels/handshake_os_ch.h \
  /home/slam/OMNET/HCSim/include/Channels/receive_if.h \
  /home/slam/OMNET/HCSim/include/Channels/receive_os_if.h \
  /home/slam/OMNET/HCSim/include/Channels/sc_mutex_os.h \
  /home/slam/OMNET/HCSim/include/Channels/sc_mutex_os_if.h \
  /home/slam/OMNET/HCSim/include/Channels/send_if.h \
  /home/slam/OMNET/HCSim/include/Channels/send_os_if.h \
  /home/slam/OMNET/HCSim/include/Channels/simpleBus_TLM.h \
  /home/slam/OMNET/HCSim/include/HCSim.h \
  /home/slam/OMNET/HCSim/include/OS/OSAPI.h \
  /home/slam/OMNET/HCSim/include/OS/PRTOS.h \
  /home/slam/OMNET/HCSim/include/OS/global_os.h \
  /home/slam/OMNET/HCSim/include/Processor/GenericIntrController.h \
  /home/slam/OMNET/HCSim/include/Processor/GenericIntrController_TLM.h \
  /home/slam/OMNET/HCSim/include/Processor/MCProcessor_FM.h \
  /home/slam/OMNET/HCSim/include/Processor/global_gic.h \
  /home/slam/OMNET/HCSim/include/Processor/interrupt_if.h \
  /home/slam/OMNET/HCSim/include/sim_config.h \
  /home/slam/OMNET/inet/src//inet/common/Compat.h \
  /home/slam/OMNET/inet/src//inet/common/INETDefs.h \
  /home/slam/OMNET/inet/src//inet/common/InitStages.h \
  /home/slam/OMNET/inet/src//inet/common/LayeredProtocolBase.h \
  /home/slam/OMNET/inet/src//inet/common/ModuleAccess.h \
  /home/slam/OMNET/inet/src//inet/common/NotifierConsts.h \
  /home/slam/OMNET/inet/src//inet/common/lifecycle/ILifecycle.h \
  /home/slam/OMNET/inet/src//inet/common/lifecycle/LifecycleOperation.h \
  /home/slam/OMNET/inet/src//inet/common/lifecycle/NodeOperations.h \
  /home/slam/OMNET/inet/src//inet/common/lifecycle/NodeStatus.h \
  /home/slam/OMNET/inet/src//inet/common/lifecycle/OperationalBase.h \
  /home/slam/OMNET/inet/src//inet/features.h \
  /home/slam/OMNET/inet/src//inet/linklayer/common/Ieee802Ctrl.h \
  /home/slam/OMNET/inet/src//inet/linklayer/common/Ieee802Ctrl_m.h \
  /home/slam/OMNET/inet/src//inet/linklayer/common/MACAddress.h \
  /home/slam/OMNET/inet/src//inet/linklayer/configurator/Ieee8021dInterfaceData.h \
  /home/slam/OMNET/inet/src//inet/linklayer/contract/IMACProtocolControlInfo.h \
  /home/slam/OMNET/inet/src//inet/linklayer/ethernet/EtherFrame_m.h \
  /home/slam/OMNET/inet/src//inet/linklayer/ethernet/Ethernet.h \
  /home/slam/OMNET/inet/src//inet/linklayer/ethernet/switch/IMACAddressTable.h \
  /home/slam/OMNET/inet/src//inet/linklayer/ieee8021d/common/Ieee8021dBPDU_m.h \
  /home/slam/OMNET/inet/src//inet/linklayer/ieee8021d/relay/Ieee8021dRelay.h \
  /home/slam/OMNET/inet/src//inet/networklayer/common/InterfaceEntry.h \
  /home/slam/OMNET/inet/src//inet/networklayer/common/InterfaceTable.h \
  /home/slam/OMNET/inet/src//inet/networklayer/common/InterfaceToken.h \
  /home/slam/OMNET/inet/src//inet/networklayer/common/L3Address.h \
  /home/slam/OMNET/inet/src//inet/networklayer/common/ModuleIdAddress.h \
  /home/slam/OMNET/inet/src//inet/networklayer/common/ModulePathAddress.h \
  /home/slam/OMNET/inet/src//inet/networklayer/contract/IInterfaceTable.h \
  /home/slam/OMNET/inet/src//inet/networklayer/contract/ipv4/IPv4Address.h \
  /home/slam/OMNET/inet/src//inet/networklayer/contract/ipv6/IPv6Address.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/app_utils.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/annotation.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/cluster_config.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/os_ctxt.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/profile_data.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/sim_results.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/lwip_ctxt.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/lwipopts.h \
  /home/slam/OMNET/lwip-hcsim/ports/port/include/arch/cc.h \
  /home/slam/OMNET/lwip-hcsim/ports/port/include/arch/perf.h \
  /home/slam/OMNET/lwip-hcsim/ports/port/include/arch/sys_arch.h \
  /home/slam/OMNET/lwip-hcsim/ports/port/include/netif/hcsim_if.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/arch.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/debug.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/def.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/err.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/errno.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/etharp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/icmp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/icmp6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/inet.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/init.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip4.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip4_addr.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip4_frag.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip6_addr.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip6_frag.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip_addr.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/mem.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/memp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/nd6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/netif.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/opt.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/pbuf.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/memp_priv.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/memp_std.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/nd6_priv.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/tcp_priv.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/tcpip_priv.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/etharp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/ethernet.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/icmp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/icmp6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/ip.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/ip4.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/ip6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/nd6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/tcp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/udp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/raw.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/sockets.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/stats.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/sys.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/tcp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/tcpip.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/timeouts.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/udp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/etharp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/ethernet.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/lowpan6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/lowpan6_common.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/lowpan6_opts.h \
  NoS/applications/ethernet/EtherWrapper_m.h \
  NoS/applications/ethernet/SrvWrapper.h
$O/NoS/applications/OSNode/OmnetIf_pkt.o: NoS/applications/OSNode/OmnetIf_pkt.cc \
  NoS/applications/OSNode/OmnetIf_pkt.h
$O/NoS/applications/OSNode/global.o: NoS/applications/OSNode/global.cc \
  /home/slam/OMNET/HCSim/include/Channels/adapters_TLM.h \
  /home/slam/OMNET/HCSim/include/Channels/ambaAhb.h \
  /home/slam/OMNET/HCSim/include/Channels/ambaAhb_if.h \
  /home/slam/OMNET/HCSim/include/Channels/global_ambaAhb.h \
  /home/slam/OMNET/HCSim/include/Channels/handshake_ch.h \
  /home/slam/OMNET/HCSim/include/Channels/handshake_os_ch.h \
  /home/slam/OMNET/HCSim/include/Channels/receive_if.h \
  /home/slam/OMNET/HCSim/include/Channels/receive_os_if.h \
  /home/slam/OMNET/HCSim/include/Channels/sc_mutex_os.h \
  /home/slam/OMNET/HCSim/include/Channels/sc_mutex_os_if.h \
  /home/slam/OMNET/HCSim/include/Channels/send_if.h \
  /home/slam/OMNET/HCSim/include/Channels/send_os_if.h \
  /home/slam/OMNET/HCSim/include/Channels/simpleBus_TLM.h \
  /home/slam/OMNET/HCSim/include/HCSim.h \
  /home/slam/OMNET/HCSim/include/OS/OSAPI.h \
  /home/slam/OMNET/HCSim/include/OS/PRTOS.h \
  /home/slam/OMNET/HCSim/include/OS/global_os.h \
  /home/slam/OMNET/HCSim/include/Processor/GenericIntrController.h \
  /home/slam/OMNET/HCSim/include/Processor/GenericIntrController_TLM.h \
  /home/slam/OMNET/HCSim/include/Processor/MCProcessor_FM.h \
  /home/slam/OMNET/HCSim/include/Processor/global_gic.h \
  /home/slam/OMNET/HCSim/include/Processor/interrupt_if.h \
  /home/slam/OMNET/HCSim/include/sim_config.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/cluster_config.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/os_ctxt.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/profile_data.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/sim_results.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/lwip_ctxt.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/lwipopts.h \
  /home/slam/OMNET/lwip-hcsim/ports/port/include/arch/cc.h \
  /home/slam/OMNET/lwip-hcsim/ports/port/include/arch/perf.h \
  /home/slam/OMNET/lwip-hcsim/ports/port/include/arch/sys_arch.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/arch.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/debug.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/def.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/err.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/errno.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/etharp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/icmp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/icmp6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/inet.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/init.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip4.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip4_addr.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip4_frag.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip6_addr.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip6_frag.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip_addr.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/mem.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/memp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/nd6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/netif.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/opt.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/pbuf.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/memp_priv.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/memp_std.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/nd6_priv.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/tcp_priv.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/tcpip_priv.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/etharp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/ethernet.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/icmp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/icmp6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/ip.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/ip4.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/ip6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/nd6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/tcp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/udp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/raw.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/sockets.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/stats.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/sys.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/tcp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/tcpip.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/timeouts.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/udp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/etharp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/ethernet.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/lowpan6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/lowpan6_common.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/lowpan6_opts.h
$O/NoS/applications/OSNode/json_config.o: NoS/applications/OSNode/json_config.cc \
  ../../../tools/json/rapidjson/allocators.h \
  ../../../tools/json/rapidjson/document.h \
  ../../../tools/json/rapidjson/encodedstream.h \
  ../../../tools/json/rapidjson/encodings.h \
  ../../../tools/json/rapidjson/error/../msinttypes/inttypes.h \
  ../../../tools/json/rapidjson/error/../msinttypes/stdint.h \
  ../../../tools/json/rapidjson/error/../rapidjson.h \
  ../../../tools/json/rapidjson/error/en.h \
  ../../../tools/json/rapidjson/error/error.h \
  ../../../tools/json/rapidjson/filereadstream.h \
  ../../../tools/json/rapidjson/filewritestream.h \
  ../../../tools/json/rapidjson/internal/../allocators.h \
  ../../../tools/json/rapidjson/internal/../encodings.h \
  ../../../tools/json/rapidjson/internal/../msinttypes/inttypes.h \
  ../../../tools/json/rapidjson/internal/../msinttypes/stdint.h \
  ../../../tools/json/rapidjson/internal/../rapidjson.h \
  ../../../tools/json/rapidjson/internal/../stream.h \
  ../../../tools/json/rapidjson/internal/biginteger.h \
  ../../../tools/json/rapidjson/internal/diyfp.h \
  ../../../tools/json/rapidjson/internal/dtoa.h \
  ../../../tools/json/rapidjson/internal/ieee754.h \
  ../../../tools/json/rapidjson/internal/itoa.h \
  ../../../tools/json/rapidjson/internal/meta.h \
  ../../../tools/json/rapidjson/internal/pow10.h \
  ../../../tools/json/rapidjson/internal/stack.h \
  ../../../tools/json/rapidjson/internal/strfunc.h \
  ../../../tools/json/rapidjson/internal/strtod.h \
  ../../../tools/json/rapidjson/internal/swap.h \
  ../../../tools/json/rapidjson/memorystream.h \
  ../../../tools/json/rapidjson/msinttypes/inttypes.h \
  ../../../tools/json/rapidjson/msinttypes/stdint.h \
  ../../../tools/json/rapidjson/prettywriter.h \
  ../../../tools/json/rapidjson/rapidjson.h \
  ../../../tools/json/rapidjson/reader.h \
  ../../../tools/json/rapidjson/stream.h \
  ../../../tools/json/rapidjson/stringbuffer.h \
  ../../../tools/json/rapidjson/writer.h \
  /home/slam/OMNET/HCSim/include/Channels/adapters_TLM.h \
  /home/slam/OMNET/HCSim/include/Channels/ambaAhb.h \
  /home/slam/OMNET/HCSim/include/Channels/ambaAhb_if.h \
  /home/slam/OMNET/HCSim/include/Channels/global_ambaAhb.h \
  /home/slam/OMNET/HCSim/include/Channels/handshake_ch.h \
  /home/slam/OMNET/HCSim/include/Channels/handshake_os_ch.h \
  /home/slam/OMNET/HCSim/include/Channels/receive_if.h \
  /home/slam/OMNET/HCSim/include/Channels/receive_os_if.h \
  /home/slam/OMNET/HCSim/include/Channels/sc_mutex_os.h \
  /home/slam/OMNET/HCSim/include/Channels/sc_mutex_os_if.h \
  /home/slam/OMNET/HCSim/include/Channels/send_if.h \
  /home/slam/OMNET/HCSim/include/Channels/send_os_if.h \
  /home/slam/OMNET/HCSim/include/Channels/simpleBus_TLM.h \
  /home/slam/OMNET/HCSim/include/HCSim.h \
  /home/slam/OMNET/HCSim/include/OS/OSAPI.h \
  /home/slam/OMNET/HCSim/include/OS/PRTOS.h \
  /home/slam/OMNET/HCSim/include/OS/global_os.h \
  /home/slam/OMNET/HCSim/include/Processor/GenericIntrController.h \
  /home/slam/OMNET/HCSim/include/Processor/GenericIntrController_TLM.h \
  /home/slam/OMNET/HCSim/include/Processor/MCProcessor_FM.h \
  /home/slam/OMNET/HCSim/include/Processor/global_gic.h \
  /home/slam/OMNET/HCSim/include/Processor/interrupt_if.h \
  /home/slam/OMNET/HCSim/include/sim_config.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/cluster_config.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/os_ctxt.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/profile_data.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/sim_results.h \
  NoS/applications/OSNode/json_config.h
$O/NoS/applications/OSNode/work_stealing_runtime.o: NoS/applications/OSNode/work_stealing_runtime.cc \
  ../../../tools/json/rapidjson/allocators.h \
  ../../../tools/json/rapidjson/document.h \
  ../../../tools/json/rapidjson/encodedstream.h \
  ../../../tools/json/rapidjson/encodings.h \
  ../../../tools/json/rapidjson/error/../msinttypes/inttypes.h \
  ../../../tools/json/rapidjson/error/../msinttypes/stdint.h \
  ../../../tools/json/rapidjson/error/../rapidjson.h \
  ../../../tools/json/rapidjson/error/en.h \
  ../../../tools/json/rapidjson/error/error.h \
  ../../../tools/json/rapidjson/filereadstream.h \
  ../../../tools/json/rapidjson/filewritestream.h \
  ../../../tools/json/rapidjson/internal/../allocators.h \
  ../../../tools/json/rapidjson/internal/../encodings.h \
  ../../../tools/json/rapidjson/internal/../msinttypes/inttypes.h \
  ../../../tools/json/rapidjson/internal/../msinttypes/stdint.h \
  ../../../tools/json/rapidjson/internal/../rapidjson.h \
  ../../../tools/json/rapidjson/internal/../stream.h \
  ../../../tools/json/rapidjson/internal/biginteger.h \
  ../../../tools/json/rapidjson/internal/diyfp.h \
  ../../../tools/json/rapidjson/internal/dtoa.h \
  ../../../tools/json/rapidjson/internal/ieee754.h \
  ../../../tools/json/rapidjson/internal/itoa.h \
  ../../../tools/json/rapidjson/internal/meta.h \
  ../../../tools/json/rapidjson/internal/pow10.h \
  ../../../tools/json/rapidjson/internal/stack.h \
  ../../../tools/json/rapidjson/internal/strfunc.h \
  ../../../tools/json/rapidjson/internal/strtod.h \
  ../../../tools/json/rapidjson/internal/swap.h \
  ../../../tools/json/rapidjson/memorystream.h \
  ../../../tools/json/rapidjson/msinttypes/inttypes.h \
  ../../../tools/json/rapidjson/msinttypes/stdint.h \
  ../../../tools/json/rapidjson/prettywriter.h \
  ../../../tools/json/rapidjson/rapidjson.h \
  ../../../tools/json/rapidjson/reader.h \
  ../../../tools/json/rapidjson/stream.h \
  ../../../tools/json/rapidjson/stringbuffer.h \
  ../../../tools/json/rapidjson/writer.h \
  ../application/DeepThings/include/configure.h \
  ../application/DeepThings/src/cmd_line_parser.h \
  ../application/DeepThings/src/deepthings_edge.h \
  ../application/DeepThings/src/deepthings_gateway.h \
  ../application/DeepThings/src/frame_partitioner.h \
  ../application/DeepThings/src/ftp.h \
  ../application/DeepThings/src/inference_engine_helper.h \
  ../application/darknet-nnpack/include/darknet.h \
  ../application/darknet-nnpack/src/activation_layer.h \
  ../application/darknet-nnpack/src/activations.h \
  ../application/darknet-nnpack/src/avgpool_layer.h \
  ../application/darknet-nnpack/src/batchnorm_layer.h \
  ../application/darknet-nnpack/src/blas.h \
  ../application/darknet-nnpack/src/box.h \
  ../application/darknet-nnpack/src/connected_layer.h \
  ../application/darknet-nnpack/src/convolutional_layer.h \
  ../application/darknet-nnpack/src/cost_layer.h \
  ../application/darknet-nnpack/src/crnn_layer.h \
  ../application/darknet-nnpack/src/crop_layer.h \
  ../application/darknet-nnpack/src/cuda.h \
  ../application/darknet-nnpack/src/data.h \
  ../application/darknet-nnpack/src/detection_layer.h \
  ../application/darknet-nnpack/src/dropout_layer.h \
  ../application/darknet-nnpack/src/gru_layer.h \
  ../application/darknet-nnpack/src/image.h \
  ../application/darknet-nnpack/src/layer.h \
  ../application/darknet-nnpack/src/list.h \
  ../application/darknet-nnpack/src/local_layer.h \
  ../application/darknet-nnpack/src/matrix.h \
  ../application/darknet-nnpack/src/maxpool_layer.h \
  ../application/darknet-nnpack/src/network.h \
  ../application/darknet-nnpack/src/normalization_layer.h \
  ../application/darknet-nnpack/src/option_list.h \
  ../application/darknet-nnpack/src/parser.h \
  ../application/darknet-nnpack/src/region_layer.h \
  ../application/darknet-nnpack/src/reorg_layer.h \
  ../application/darknet-nnpack/src/rnn_layer.h \
  ../application/darknet-nnpack/src/route_layer.h \
  ../application/darknet-nnpack/src/shortcut_layer.h \
  ../application/darknet-nnpack/src/softmax_layer.h \
  ../application/darknet-nnpack/src/tree.h \
  ../application/darknet-nnpack/src/utils.h \
  ../runtime/hcsim/thread_util.h \
  ../runtime/include/darkiot.h \
  ../runtime/lwip/lwip_ctxt.h \
  ../runtime/lwip/network_util.h \
  ../runtime/src/client.h \
  ../runtime/src/data_blob.h \
  ../runtime/src/exec_ctrl.h \
  ../runtime/src/gateway.h \
  ../runtime/src/global_context.h \
  ../runtime/src/thread_safe_queue.h \
  /home/slam/OMNET/HCSim/include/Channels/adapters_TLM.h \
  /home/slam/OMNET/HCSim/include/Channels/ambaAhb.h \
  /home/slam/OMNET/HCSim/include/Channels/ambaAhb_if.h \
  /home/slam/OMNET/HCSim/include/Channels/global_ambaAhb.h \
  /home/slam/OMNET/HCSim/include/Channels/handshake_ch.h \
  /home/slam/OMNET/HCSim/include/Channels/handshake_os_ch.h \
  /home/slam/OMNET/HCSim/include/Channels/receive_if.h \
  /home/slam/OMNET/HCSim/include/Channels/receive_os_if.h \
  /home/slam/OMNET/HCSim/include/Channels/sc_mutex_os.h \
  /home/slam/OMNET/HCSim/include/Channels/sc_mutex_os_if.h \
  /home/slam/OMNET/HCSim/include/Channels/send_if.h \
  /home/slam/OMNET/HCSim/include/Channels/send_os_if.h \
  /home/slam/OMNET/HCSim/include/Channels/simpleBus_TLM.h \
  /home/slam/OMNET/HCSim/include/HCSim.h \
  /home/slam/OMNET/HCSim/include/OS/OSAPI.h \
  /home/slam/OMNET/HCSim/include/OS/PRTOS.h \
  /home/slam/OMNET/HCSim/include/OS/global_os.h \
  /home/slam/OMNET/HCSim/include/Processor/GenericIntrController.h \
  /home/slam/OMNET/HCSim/include/Processor/GenericIntrController_TLM.h \
  /home/slam/OMNET/HCSim/include/Processor/MCProcessor_FM.h \
  /home/slam/OMNET/HCSim/include/Processor/global_gic.h \
  /home/slam/OMNET/HCSim/include/Processor/interrupt_if.h \
  /home/slam/OMNET/HCSim/include/sim_config.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/cluster_config.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/os_ctxt.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/profile_data.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/context/sim_results.h \
  /home/slam/OMNET/lwip-hcsim/ports/hcsim/lwipopts.h \
  /home/slam/OMNET/lwip-hcsim/ports/port/include/arch/cc.h \
  /home/slam/OMNET/lwip-hcsim/ports/port/include/arch/perf.h \
  /home/slam/OMNET/lwip-hcsim/ports/port/include/arch/sys_arch.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/arch.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/debug.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/def.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/err.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/errno.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/etharp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/icmp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/icmp6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/inet.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/init.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip4.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip4_addr.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip4_frag.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip6_addr.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip6_frag.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/ip_addr.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/mem.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/memp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/nd6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/netif.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/opt.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/pbuf.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/memp_priv.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/memp_std.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/nd6_priv.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/tcp_priv.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/priv/tcpip_priv.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/etharp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/ethernet.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/icmp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/icmp6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/ip.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/ip4.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/ip6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/nd6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/tcp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/prot/udp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/raw.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/sockets.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/stats.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/sys.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/tcp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/tcpip.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/timeouts.h \
  /home/slam/OMNET/lwip-hcsim/src/include/lwip/udp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/etharp.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/ethernet.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/lowpan6.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/lowpan6_common.h \
  /home/slam/OMNET/lwip-hcsim/src/include/netif/lowpan6_opts.h \
  NoS/applications/OSNode/json_config.h \
  NoS/applications/OSNode/work_stealing_runtime.h
