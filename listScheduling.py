#!/usr/bin/env python
"""
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
|DESCRIPTION: This code is intended to implement the List scheduling to a given graph application, ALAP and ASAP results. |
| The schedule time result of this algorithm does not consider reconfiguration time                                                                 |
|CREATED BY: uglaybe                                                                                                                                                                  |
|CREATION DATE: 01/set/2017                                                                                                                                                      |
|MODIFIED IN: 07/out/2017                                                                                                                                                            |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

import networkx as nx


class Operation_Struct:
    def __init__(self):
        self.node = ""
        self.ASAP_Time = 0.0
        self.ALAP_Time = 0.0
        self.Mobility_Priority = 0.0
        self.Priority = 0.0
        self.areaOcupied = 0

class Partition_Struct:
    def __init__(self):
        self.operation_List = []
        self.init_ExecutionTime = 0
        self.latency = 0
        self.areaOcupied = 0


"""
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
|DESCRIPTION: This function returns if the node is ready to be assigned in a partition accordingly to ALAP algorithm.            |
|CREATED BY: uglaybe                                                                                                                                                                  |
|INPUTS: graph = application graph; nodesToAdd_List = node list to be added yet; node = node to be checked                      |
|OUTPUTS: eligible_Bool = True if is eligible, False if not                                                                                                              |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
def isEligible(graph, insertNode_List, node):
    eligible_Bool = True

    for predecessor_node in graph.predecessors(node):
        if predecessor_node in insertNode_List:
            eligible_Bool = False
            break
    return eligible_Bool


def updateEligibleList(graph, insertNode_List, inserted_node, eligible_List, operation_List, output_List):
    newEligible_List = eligible_List
    insertedNode_Successors = graph.successors(inserted_node)

    for successor in insertedNode_Successors:
        if isEligible(graph, insertNode_List, successor) & (successor not in output_List):
            #newEligible_List.append(successor)
            newEligible_List.append(getOperationInoperation_List(successor, operation_List))

    return newEligible_List

"""
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
|DESCRIPTION: This function create an Operation in Operation_Struct.                                                                                      |
|CREATED BY: uglaybe                                                                                                                                                                  |
|INPUTS: node = operation node; ASAP_Time = ASAP algorithm time; ALAP_Time = ALAP algorithm time;                              |
|areaOcupied = hardware implementation areaOcupied                                                                                                            |
|OUTPUTS: operation = operation node                                                                                                                                       |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
def createoperation_List (node, ASAP_Time, ALAP_Time, areaOcupied):
    operation = Operation_Struct()
    operation.node = node
    operation.ASAP_Time = ASAP_Time
    operation.ALAP_Time = ALAP_Time
    operation.areaOcupied = areaOcupied
    operation.Mobility_Priority = 1.0/(ALAP_Time - ASAP_Time + 1.0)
    return operation

"""
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
|DESCRIPTION: This function returns an operation struct in an operation list related to specified node                                     |
|CREATED BY: uglaybe                                                                                                                                                                  |
|INPUTS: node = operation node; operation_List = operation struct list                                                                                      |
|OUTPUTS: operation = operation node                                                                                                                                       |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
def getOperationInoperation_List (node, operation_List):
    for operation in operation_List:
        if operation.node == node:
            return operation

    return None


"""
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
|DESCRIPTION: This function returns the max operation latency for predecessor list inside partition                                        |
|CREATED BY: uglaybe                                                                                                                                                                  |
|INPUTS: predecessorList = predecessor list; graph = application graph; partitionNodeList = partition node list;                     |
|operationLatencyList = operation latency list                                                                                                                             |
|OUTPUTS: maxLatency = maximum operation latency                                                                                                             |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
def getMaxOperationLatency(predecessorList, graph, partitionNodeList, operationLatencyList):
    maxLatency = 0.0
    currentLatency = 0.0

    partitionSet = set(partitionNodeList)

    for node in predecessorList:
        if node in partitionNodeList:
            if len(set(graph.predecessors(node)).intersection(partitionSet)) == 0:
                currentLatency = operationLatencyList[partitionNodeList.index(node)]
            else:
                currentLatency = operationLatencyList[partitionNodeList.index(node)] + getMaxOperationLatency(graph.predecessors(node), graph, partitionNodeList, operationLatencyList)
            if maxLatency < currentLatency:
                maxLatency = currentLatency

    return maxLatency


"""
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
|DESCRIPTION: This function returns the node operation latency                                                                                                |
|CREATED BY: uglaybe                                                                                                                                                                  |
|INPUTS: node = node to get latency; graph = application graph; partitionNodeList = partition node list                                  |
| operationLatencyList= operation latency list                                                                                                                             |
|OUTPUTS: latency = maximum operation latency                                                                                                                      |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
def getLatencyRecursive(node, graph, partitionNodeList, operationLatencyList):
    partitionSet = set(partitionNodeList)

    for predecessor in graph.predecessors(node):
        if len(set(graph.predecessors(node)).intersection(partitionSet)) == 0:
            latency = operationLatencyList[partitionNodeList.index(node)]
        else:
            latency = operationLatencyList[partitionNodeList.index(node)] + getMaxOperationLatency(graph.predecessors(node), graph, partitionNodeList, operationLatencyList)

    return latency



"""
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
|DESCRIPTION: This function returns the Partition latency.                                                                                                          |
|CREATED BY: uglaybe                                                                                                                                                                  |
|INPUTS: graph = application graph; operation_List = operation struct list                                                                                 |
|OUTPUTS: maxLatency = maximum operation latency                                                                                                              |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
def getPartitionLatency (graph, operation_List):

    maxLatency = 0.0
    currentLatency = 0.0
    operationLatency = 0.0
    operationNodeList = []
    operationLatencyList = []
    successorList = []


    for operation in operation_List:
        operationNodeList.append(operation.node)
        successorList = graph.successors(operation.node)
        operationLatency = graph[operation.node][successorList[0]]['weight']
        operationLatencyList.append(operationLatency)

    for operation in operation_List:
        currentLatency = getLatencyRecursive(operation.node, graph, operationNodeList, operationLatencyList)
        if currentLatency > maxLatency:
            maxLatency = currentLatency

    return maxLatency


"""
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
|DESCRIPTION: This function sorts an operation list by its Priority in decreasing order                                                               |
|CREATED BY: uglaybe                                                                                                                                                                  |
|INPUTS: operation_List = operation struct list                                                                                                                             |
|OUTPUTS: sorted_List = operation_List properly sorted                                                                                                              |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
def sortOperation_ListByPriority(operation_List):
    sorted_List = sorted(operation_List, key=lambda x: x.Priority, reverse = True)
    return sorted_List


"""
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
|DESCRIPTION: This function implement List Scheduling algorithm                                                                                             |
|CREATED BY: uglaybe                                                                                                                                                                  |
|INPUTS: graph = application graph; input_List = list of input nodes; operand_List = list of operand nodes;                              |
|output_List = list of output nodes; area_Dictionary = dictionary that relate area requirements and each operation;               |
|ASAP_dictionaryByNode = dictionary relating each operation and the ASAP schedule time;                                                     |
|ALAP_dictionaryByNode = dictionary relating each operation and the ALAP schedule time;                                                     |
|partitionArea = Hardware area constraint                                                                                                                                  |
|OUTPUTS: partitionList = partition struct list result of List Scheduling Algorithm                                                                       |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
def definePartitions(graph, input_List, operand_List, output_List, area_Dictionary, ASAP_dictionaryByNode, ALAP_dictionaryByNode, partitionArea):

    all_input_List = input_List + operand_List

    #OPERATION NODE LIST
    insertNode_List = list(set(graph.nodes()) - set(all_input_List) - set(output_List))

    #OPERATION STRUCTURE NODE LIST
    operation_List = []
    partition_List = []
    #Iteration number
    n = 1

    #eligible_List
    eligible_List = []


    #Create Operation_Struct list for all operations
    for node in insertNode_List:
        newOperation = createoperation_List(node, ASAP_dictionaryByNode[node], ALAP_dictionaryByNode[node],  area_Dictionary[node])
        operation_List.append(newOperation)

    #Create partition list
    while len(insertNode_List) > 0:
        #Create eligible_List
        for node in insertNode_List:
            if isEligible(graph, insertNode_List, node):
                nodeOperation = getOperationInoperation_List(node, operation_List)
                #CHECK IF AN ERROR OCCURRED
                if nodeOperation == None:
                    continue
                nodeOperation.Priority = n - nodeOperation.ALAP_Time + nodeOperation.Mobility_Priority
                eligible_List.append(nodeOperation)

        eligible_List = sortOperation_ListByPriority(eligible_List)
        newPartition = Partition_Struct()


        i = 0
        while (len(eligible_List) != 0) & (len(eligible_List) > i):

            operation = eligible_List[i]
            if newPartition.areaOcupied + operation.areaOcupied <= partitionArea:
                newPartition.operation_List.append(operation)
                newPartition.areaOcupied = newPartition.areaOcupied + operation.areaOcupied
                insertNode_List.remove(operation.node)
                eligible_List.remove(getOperationInoperation_List (operation.node, operation_List))
                eligible_List = updateEligibleList(graph, insertNode_List, operation.node, eligible_List, operation_List, output_List)
                eligible_List = sortOperation_ListByPriority(eligible_List)
                i = 0
            else:
                i = i + 1


        newPartition.latency = getPartitionLatency (graph, newPartition.operation_List)
        if n == 1:
            newPartition.init_ExecutionTime = 0
        else:
            newPartition.init_ExecutionTime = partition_List[-1].init_ExecutionTime + partition_List[-1].latency

        partition_List.append(newPartition)
        newPartition = None
        eligible_List = []
        n += 1

    #print result
    n=0
    for partition in partition_List:
        print "Partition:"
        print n
        print "Operations:"
        for operation in partition.operation_List:
            print operation.node
        print "Schedule Time:"
        print partition.latency
        print "######################"
        n+=1

    return partition_List



