# NoSDSE
Network-of-Systems Design Space Exploration
============================

NoSDSE [2] is a network-level design space exploration framework resource-constrained 
Networks-of-Systems (NoS). It relies on NoSSim [1], a fast and accurate NoS simulation 
framework, for design point evaluation. NoSDSE further includes NoSSim model generators 
and a multi-objective genetic algorithm to allow automated NoS design space exploration. 

NoSDSE is demonstrated with three IoT/mobile application scenarios. 

IoT scenarios:
------------------
```
  examples/vision_graph       -- Vision graph discovery, where the relative position and 
		                 orientation among a network of smart cameras are estimated
		      
  examples/ecg_diagnosis      -- ECG monitoring, where raw ECG signals are used to 
		                 detect heart arrhythmia

  examples/deepthings         -- DeepThings is a framework for locally distributed and adaptive CNN 
                                 inference in resource-constrained IoT edge clusters [3]
```

Directories:
------------
```
  tools/                     -- JSON lib and configuration file template
  NoSSim/                    -- NoSSim, a network/system co-simulation framework
  examples/vision_graph/     -- The vision graph discovery example
     ezSIFT/                     - The SIFT (scale-invariant feature transform) algorithm library
     networking_api/             - Networking APIs and runtime libraries (based on lwip and HCSim) 
     src/                        - Source code for application, system and network models
     dse.py                      - Model generators (From genome to NoSSim simulation instance)
     nsga.py                     - Design space explorer based on NSGA-II

  examples/ecg_diagnosis/    -- The ECG monitoring example
     ecg/     	                 - ECG diagnosis library
     networking_api/             - Networking APIs and runtime libraries (based on lwip and HCSim) 
     src/                        - Source code for application, system and network models
     dse.py                      - Model generators (From genome to NoSSim simulation instance)
     nsga.py                     - Design space explorer based on NSGA-II

  examples/deepthings/    -- The DeepThings example
     application/     	         - DeepThings source code and Darknet library
     networking_api/             - Distributed work stealing runtime (based on lwip and HCSim) 
     src/                        - Source code for application, system and network models
     dse.py                      - Model generators (From genome to NoSSim simulation instance)
     nsga.py                     - Design space explorer based on NSGA-II
```

Building and installing:
------------------------
Build requirements:
  - SystemC version 2.3.1 http://www.accellera.org/
  - OMNEST version 5.0  http://www.omnest.com/
    (alternatively OMNeT++ version 5.0 with SystemC integration http://www.omnetpp.org)
  - INET framework version 3.4.0 http://inet.omnetpp.org/

Preparation before build:
  - For setting up HCSim (included as a submodule), please see [here](https://github.com/SLAM-Lab/HCSim)
  - Apply the INET patch (inet_extra) and rebuild INET framework

Preparation before running the example:
  - Set the OMNeT++ path:
```bash
  pushd /home/slam/OMNET/omnetpp-5.0; . setenv; popd
```
  - Set the INET path by changing the INET_DIR in [Makefile](https://github.com/SLAM-Lab/NoSSim/blob/master/examples/ecg_diagnosis/Makefile) for each application


Running:
--------
In general, you should perform a function-level profiling and back-annotation 
for the lwIP, ECG and ezSIFT library with the provided LLVM pass and 
helper functions in InstrumentLLVM directory. For the case studies included in 
this repository, we include [profile data for different platforms](https://github.com/SLAM-Lab/NoSSim/tree/master/examples/ecg_diagnosis/src/profile) so that you can directly try them out of box. 

For DeepThings, you need to download the [weight file for YOLOv2](https://pjreddie.com/media/files/yolo.weights) and put it in [examples/deepthings/src/models](https://github.com/zoranzhao/NoSDSE/tree/master/examples/deepthings/src/models).

To build an example, change into the corresponding example
directory and run:
```bash
   cd examples/vision_graph
   make dependency
   make makefiles
   make
```
To perform exploration for an example:
```bash
   cd examples/ecg_diagnosis
   python nsga.py
```


References:
-----------
- [1] Z. Zhao, V. Tsoutsouras, D. Soudris and A. Gerstlauer, "Network/System 
    Co-Simulation for Design Space Exploration of IoT Applications," SAMOS, July 2017.
- [2] Z. Zhao, K. Mirzazad, A. Gerstlauer, "Network-level Design Space Exploration for
    Resource-Constrained Networks-of-Systems," ACM Transactions on Embedded
    Computer Systems (TECS), under review.
- [3] Z. Zhao, K. Mirzazad, A. Gerstlauer, "DeepThings: Distributed Adaptive Deep 
    Learning Inference on Resource-Constrained IoT Edge Clusters," CODES+ISSS, special 
    issue of IEEE Transactions on Computer-Aided Design of Integrated Circuits and 
    Systems (TCAD), 2018


Contact: 
--------
     Zhuoran Zhao <zhuoran@utexas.edu>
     Kamyar Mirzazad <kammirzazad@utexas.edu> 

