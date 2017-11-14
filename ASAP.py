#!/usr/bin/env python
"""
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
|DESCRIPTION: This code is intended to implement the ASAP algorithm result for a given input graph.                                      |
|CREATED BY: uglaybe                                                                                                                                                                  |
|CREATION DATE: 01/set/2017                                                                                                                                                      |
|MODIFIED IN: 07/out/2017                                                                                                                                                            |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

import networkx as nx


"""
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
|DESCRIPTION: This function returns if the node is ready to define the schedule time accordingly to ASAP algorithm.             |
|CREATED BY: uglaybe                                                                                                                                                                  |
|INPUTS: graph = application graph; nodesToAdd_List = node list to be added yet; node = node to be checked                      |
|OUTPUTS: eligible_Bool = True if is eligible, False if not                                                                                                              |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
def isEligible(graph, nodesToAdd_List, node):
    eligible_Bool = True

    for predecessor_node in graph.predecessors(node):
        if predecessor_node in nodesToAdd_List:
            eligible_Bool = False
            break

    return eligible_Bool


"""
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
|DESCRIPTION: This function calculate the schedule time of an operation node, accordingly to ASAP algorithm.                      |
|CREATED BY: uglaybe                                                                                                                                                                  |
|INPUTS: node = node to be checked; graph = application graph; nodesToAdd_List = node list to be added yet;                     |
|dictionaryByNode = Dictionary that indexes schedule time by node for the ones already defined                                               |
|OUTPUTS: scheduleTime = schedule time for node operation                                                                                                   |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
def getScheduleTime (node, graph, input_List, dictionaryByNode):
    scheduleTime = 0
    for predecessor in graph.predecessors(node):
        if predecessor in input_List:
            continue
        candidateScheduleTime = dictionaryByNode[predecessor] + graph[predecessor][node]['weight']
        if scheduleTime < candidateScheduleTime:
            scheduleTime = candidateScheduleTime

    return scheduleTime


"""
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
|DESCRIPTION: This function implement ASAP algorithm.                                                                                                            |
|CREATED BY: uglaybe                                                                                                                                                                  |
|INPUTS: graph = application graph; input_List = list of input nodes; operand_List = list of operand nodes                               |
|OUTPUTS: time_List = list of schedule times defined; dictionaryByNode = Dictionary that indexes schedule time by node;    |
|dictionaryByTime = Dictionary that indexes nodes by schedule Time                                                                                        |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
def ASAP_algorithm(graph, input_List, operand_List):

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
            scheduleTime = getScheduleTime(node,graph,all_input_List,dictionaryByNode)
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