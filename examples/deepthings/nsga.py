import random
import array
import json
import numpy
import pprint
import deap
import multiprocessing
import time

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from deap import benchmarks
from deap.benchmarks.tools import diversity, convergence

import dse

creator.create("FitnessMulti", base.Fitness, weights=(-1.0, -1.0, -1.0))
creator.create("Individual", list, fitness=creator.FitnessMulti)

toolbox = base.Toolbox()

#[protocol, FTP, node number, edge_1, edge_2, edge_3, edge_4, edge_5, edge_6]
knobs_low = [0,    3,    1,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
knobs_up =  [6,    5,    12,    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]

for i in range(len(knobs_low)):
   toolbox.register("attr_int"+str(i), random.randint, knobs_low[i], knobs_up[i])   

toolbox.register("individual", tools.initCycle, creator.Individual,
                 (toolbox.attr_int0, toolbox.attr_int1, toolbox.attr_int2, 
                  toolbox.attr_int3, toolbox.attr_int4, toolbox.attr_int5, 
                  toolbox.attr_int6, toolbox.attr_int7, toolbox.attr_int8,
                  toolbox.attr_int9, toolbox.attr_int10, toolbox.attr_int11,
                  toolbox.attr_int12, toolbox.attr_int13, toolbox.attr_int14, toolbox.attr_int15), 
		 n=1)

toolbox.register("population", tools.initRepeat, list, toolbox.individual)

result_cache = {}

def get_key_string(individual):
    effect_ind = [individual[0], individual[1], individual[2], "_"]
    for i in range(individual[2]):
       effect_ind.append(individual[3+i])
    effect_ind.append(individual[-1])
    return ''.join(map(str, effect_ind)) 

def evalOneMax(individual):

        layers_config_list ={
            0 : 4,
            1 : 8,
            2 : 12,
            3 : 16,
        }
        mem_table = {'3x3_12': 19.06433, 
                 '3x3_16': 29.068236000000002, 
                 '5x5_4': 9.159058000000002, 
                 '5x5_8': 9.753784000000001, 
                 '5x5_12': 12.130737000000002, 
                 '4x4_12': 14.669799000000001, 
                 '4x4_16': 24.673704999999998, 
                 '3x3_8': 16.687377, 
                 '4x4_4': 11.698120000000001, 
                 '4x4_8': 12.292846, 
                 '5x5_16': 22.134643, 
                 '3x3_4': 16.092651}

        log_file_name = ""
        path = ""
        if "PoolWorker-1" == multiprocessing.current_process().name:
           log_file_name = "evaluated_inds1.log"
           path = "../OMNeT_DeepThings_HCSim_1/"
        if "PoolWorker-2" == multiprocessing.current_process().name:
           log_file_name = "evaluated_inds2.log"
           path = "../OMNeT_DeepThings_HCSim_2/"
        if "PoolWorker-3" == multiprocessing.current_process().name:
           log_file_name = "evaluated_inds3.log"
           path = "../OMNeT_DeepThings_HCSim_3/"
        if "PoolWorker-4" == multiprocessing.current_process().name:
           log_file_name = "evaluated_inds4.log"
           path = "../OMNeT_DeepThings_HCSim_4/"
        if "PoolWorker-5" == multiprocessing.current_process().name:
           log_file_name = "evaluated_inds5.log"
           path = "../OMNeT_DeepThings_HCSim_5/"
        if "PoolWorker-6" == multiprocessing.current_process().name:
           log_file_name = "evaluated_inds6.log"
           path = "../OMNeT_DeepThings_HCSim_6/"

        with open(log_file_name, "a") as myfile:
           myfile.write(''.join(map(str, individual))+"  ")

        if get_key_string(individual) in result_cache:
           result = result_cache[get_key_string(individual)]
           print "individual is: ", individual, " get_effect individual is: ", get_key_string(individual)
        else:
           latency_energy = dse.evaluate_one(top_workspace = path,  genome = individual)
           result = latency_energy[0], mem_table[str(individual[1]) + "x" + str(individual[1]) + "_" + str(layers_config_list[individual[15]])], latency_energy[1]
           #print individual, "   ", 
           #print str(individual[1]) + "x" + str(individual[1]) + "_" + str(layers_config_list[individual[15]]), ", ", 
           #print mem_table[str(individual[1]) + "x" + str(individual[1]) + "_" + str(layers_config_list[individual[15]])]
   	   #result = -sum(individual[0:6])-individual[1], individual[1], sum(individual[3:16])-individual[1]

        with open(log_file_name, "a") as myfile:
           myfile.write(str(result[0]) + "," + str(result[1]) + "," + str(result[2]) + "\n")

        result_cache[get_key_string(individual)] = result
	return result

def mainNSGA(seed=None):
    with open("evaluated_inds1.log", "w") as myfile:
        myfile.write("===Evaluated genomes===:\n")
    with open("evaluated_inds2.log", "w") as myfile:
        myfile.write("===Evaluated genomes===:\n")
    with open("evaluated_inds3.log", "w") as myfile:
        myfile.write("===Evaluated genomes===:\n")
    with open("evaluated_inds4.log", "w") as myfile:
        myfile.write("===Evaluated genomes===:\n")
    with open("evaluated_inds5.log", "w") as myfile:
        myfile.write("===Evaluated genomes===:\n")
    with open("evaluated_inds6.log", "w") as myfile:
        myfile.write("===Evaluated genomes===:\n")

    with open("runtime_pareto.log", "w") as myfile:
        myfile.write("===runtime_pareto===:\n")

    with open("runtime_time.log", "w") as myfile:
        myfile.write("===runtime_time===:\n")

    ga_data = {}

    pool = multiprocessing.Pool(6)
    toolbox.register("map", pool.map)

    toolbox.register("evaluate", evalOneMax)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutUniformInt, low=knobs_low, up=knobs_up, indpb=0.05)
    toolbox.register("select", tools.selNSGA2)
    random.seed(seed)
    #MU = 40
    #CXPB = 0.8
    #MUTPB = 0.8
    #NGEN = 30

    MU = 80
    CXPB = 0.8
    MUTPB = 0.8
    NGEN = 40


    pop = toolbox.population(n=MU)

    # Evaluate the individuals with an invalid fitness
    invalid_ind = [ind for ind in pop if not ind.fitness.valid]
    fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit

    # This is just to assign the crowding distance to the individuals
    # no actual selection is done
    pop = toolbox.select(pop, len(pop))

    # Begin the generational process
    for gen in range(1, NGEN):
        start = time.time()
        # Vary the population
        print(" ======Beginning %i th generation======: " % gen)
        offspring = tools.selTournamentDCD(pop, len(pop))
        offspring = [toolbox.clone(ind) for ind in offspring]
        
        for ind1, ind2 in zip(offspring[::2], offspring[1::2]):
            if random.random() <= CXPB:
                toolbox.mate(ind1, ind2)
            	del ind1.fitness.values, ind2.fitness.values
            if random.random() <= MUTPB:
                toolbox.mutate(ind1)
                toolbox.mutate(ind2)
            	del ind1.fitness.values, ind2.fitness.values
        
        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        # Select the next generation population
        pop = toolbox.select(pop + offspring, MU)

	fitness_list = []
    	fronts_lists = tools.sortNondominated(pop, len(pop), first_front_only=True)[0]	
	fronts=[]

	for i in range(len(fronts_lists)):
	   if fronts_lists[i] not in fronts:
		fronts.append(fronts_lists[i])
		fitness_list.append(fronts_lists[i].fitness.values)
        print " Pareto front is:"
	ga_data[gen]={"fitness":fitness_list,"front":fronts}
        with open("runtime_pareto.log", "a") as myfile:
            myfile.write(str(ga_data[gen])+"\n")
        end = time.time()
        with open("runtime_time.log", "a") as myfile:
            myfile.write(str(end-start)+"\n")
	pprint.pprint( fitness_list )
	pprint.pprint( fronts )

        print("  Evaluated %i individuals\n" % len(invalid_ind))


    jsonConfigFile="./ga_data.json"
    with open(jsonConfigFile,"w") as jFile:
       json.dump(ga_data, jFile, indent=4, separators=(',', ': '))


    #with open(jsonConfigFile) as jFile:
    #   ga_data = json.load(jFile) 
    #   pprint.pprint(ga_data)

    print("-- End of (successful) evolution --")
    
    return pop



if __name__ == "__main__":

    pop = mainNSGA()
    #dse.get_result(2, [1,2,3])


