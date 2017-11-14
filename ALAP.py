#!/usr/bin/env python
"""
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
|DESCRIPTION: This code is intended to implement the ALAP algorithm result for a given input graph.                                      |
|CREATED BY: uglaybe                                                                                                                                                                  |
|CREATION DATE: 01/set/2017                                                                                                                                                      |
|MODIFIED IN: 07/out/2017                                                                                                                                                            |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
import networkx as nx


"""
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
|DESCRIPTION: This function returns if the node is ready to define the schedule time accordingly to ALAP algorithm.             |
|CREATED BY: uglaybe                                                                                                                                                                  |
|INPUTS: graph = application graph; nodesToAdd_List = node list to be added yet; node = node to be checked                      |
|OUTPUTS: eligible_Bool = True if is eligible, False if not                                                                                                              |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
def isEligible(graph, nodesToAdd_List, node):
    eligible_Bool = True

    for successor_node in graph.successors(node):
        if successor_node in nodesToAdd_List:
            eligible_Bool = False
            break

    return eligible_Bool


"""
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
|DESCRIPTION: This function calculate the schedule time of an operation node, accordingly to ALAP algorithm.                      |
|CREATED BY: uglaybe                                                                                                                                                                  |
|INPUTS: node = node to be checked; graph = application graph; nodesToAdd_List = node list to be added yet;                     |
|dictionaryByNode = Dictionary that indexes schedule time by node for the ones already defined;                                           |
|maxScheduleTime = max schedule time from ASAP algorithm                                                                                                  |
|OUTPUTS: scheduleTime = schedule time for node operation                                                                                                   |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
def getScheduleTime (node,graph,input_List, dictionaryByNode, maxScheduleTime):
    scheduleTime = maxScheduleTime
    for successor in graph.successors(node):
        if successor in input_List:
            continue
        candidateScheduleTime = dictionaryByNode[successor] - graph[node][successor]['weight']
        if scheduleTime > candidateScheduleTime:
            scheduleTime = candidateScheduleTime

    return scheduleTime


"""
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
|DESCRIPTION: This function implement ALAP algorithm.                                                                                                            |
|CREATED BY: uglaybe                                                                                                                                                                  |
|INPUTS: graph = application graph; input_List = list of input nodes; operand_List = list of operand nodes;                              |
|output_List = list of output nodes ;maxScheduleTime = max schedule time from ASAP algorithm                                           |
|OUTPUTS: time_List = list of schedule times defined; dictionaryByNode = Dictionary that indexes schedule time by node;    |
|dictionaryByTime = Dictionary that indexes nodes by schedule Time                                                                                        |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
def ALAP_algorithm(graph, input_List, operand_List, output_List, maxScheduleTime):

    all_input_List = input_List + operand_List

    #original graph node list
    nodesGraph_List = graph.nodes()


    dictionaryByNode = {}
    dictionaryByTime = {}

    eligible_List = []
    time_List = []

    #Subtract lists to obtain nodes to be added
    nodesToAdd_List = list(set(nodesGraph_List) - set(list(all_input_List)))



    while len(nodesToAdd_List) > 0:
        #update eligible list
        for candidateNode in nodesToAdd_List:
            if isEligible(graph, nodesToAdd_List, candidateNode):
                eligible_List.append(candidateNode)

        for node in eligible_List:
            scheduleTime = getScheduleTime(node,graph,all_input_List,dictionaryByNode, maxScheduleTime)
            dictionaryByNode[node] = scheduleTime
            time_List.append(scheduleTime)
            nodesToAdd_List.remove(node)
        eligible_List = []

    #Create new dictionary indexing by schedule time
    for key, value in dictionaryByNode.iteritems():
        dictionaryByTime[value] = dictionaryByTime.get(value, [])
        dictionaryByTime[value].append(key)

    time_List = list(set(time_List))
    #sort time list
    time_List.sort()

    return time_List, dictionaryByNode, dictionaryByTime