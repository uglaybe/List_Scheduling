#!/usr/bin/env python

"""
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
|DESCRIPTION: This code is intended to implement the List Scheduling algorithm, obtaining the partitions and schedule time|
|for a given input application. This code does not consider reconfiguration time.                                                                       |
|CREATED BY: uglaybe                                                                                                                                                                  |
|CREATION DATE: 01/set/2017                                                                                                                                                      |
|MODIFIED IN: 07/out/2017                                                                                                                                                            |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

#graph python library
import networkx as nx
#graph plot python library
import pylab as plt
import pygraphviz
from networkx.drawing.nx_agraph import graphviz_layout

#List Scheduling libraries
from ASAP import ASAP_algorithm
from ALAP import ALAP_algorithm
from listScheduling import definePartitions
import listScheduling

#input application
from input_graph import input_application



def main():

    partitionArea = 3


    [graph, input_List, operand_List, output_List, area_Dictionary] = input_application()

    [ASAP_timeList, ASAP_dictionaryByNode, ASAP_dictionaryByTime] = ASAP_algorithm(graph, input_List, operand_List)

    [ALAP_timeList, ALAP_dictionaryByNode, ALAP_dictionaryByTime] = ALAP_algorithm(graph, input_List, operand_List, output_List, ASAP_timeList[-1])

    partition_List = definePartitions(graph, input_List, operand_List, output_List, area_Dictionary, ASAP_dictionaryByNode, ALAP_dictionaryByNode, partitionArea)


    #GRAPH PLOT IF NECESSARY
    #pos=graphviz_layout(graph)
    #nx.draw(graph, pos, node_color='r', with_labels=True)
    #plt.show()

    return


if __name__ == "__main__":
    main()