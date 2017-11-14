#!/usr/bin/env python
"""
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
|DESCRIPTION: This code is intended to implement the input application to List Scheduling algorithm.                                     |
|CREATED BY: uglaybe                                                                                                                                                                  |
|CREATION DATE: 01/set/2017                                                                                                                                                      |
|MODIFIED IN: 07/out/2017                                                                                                                                                            |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""


import networkx as nx

"""
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
|DESCRIPTION: This function is intended to implement a Bhaskara application in a graph to be processed by List Scheduling |
|algorithm.                                                                                                                                                                                    |
|INPUTS: N/A                                                                                                                                                                                 |
|OUTPUTS: N/A                                                                                                                                                                             |
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
def bhaskara_example():
    #Operations latency
    MULT_OPERATION_TIME=0.02
    SUM_OPERATION_TIME=0.02
    SUB_OPERATION_TIME=0.02
    SQRT_OPERATION_TIME=0.02
    DIV_OPERATION_TIME=0.02
    INITIAL_OPERATION_TIME=0

    #Operations reconfigurable area requirements
    AREA_MULT=6
    AREA_SOMA=4
    AREA_SUB=4
    AREA_RAIZ=12
    AREA_DIVISAO=6

    AREA_MULT=1
    AREA_SOMA=1
    AREA_SUB=1
    AREA_RAIZ=1
    AREA_DIVISAO=1
    #input nodes
    a="a"
    b="b"
    c="c"

    input_List=[a,b,c]

    #operand Nnodes
    operand1="-1"#-1
    operand2="2"#2
    operand3="4"#4

    operand_List=[operand1,operand2,operand3]


    #output nodes
    x1="x1"
    x2="x2"

    output_List=[x1,x2]

    #operation nodes
    op1="op1 x"
    op2="op2 x"
    op3="op3 x"
    op4="op4 -"
    op5="op5 sqrt"
    op6="op6 x"
    op7="op7 x"
    op8="op8 +"
    op9="op9 /"
    op10="op10 -"
    op11="op11 /"

    #define operation area requirements
    area_Dictionary = {}
    area_Dictionary["op1 x"] = AREA_MULT
    area_Dictionary["op2 x"] = AREA_MULT
    area_Dictionary["op3 x"] = AREA_MULT
    area_Dictionary["op4 -"] = AREA_SUB
    area_Dictionary["op5 sqrt"] = AREA_RAIZ
    area_Dictionary["op6 x"] = AREA_MULT
    area_Dictionary["op7 x"] = AREA_MULT
    area_Dictionary["op8 +"] = AREA_SOMA
    area_Dictionary["op9 /"] = AREA_DIVISAO
    area_Dictionary["op10 -"] = AREA_DIVISAO
    area_Dictionary["op11 /"] = AREA_SUB

    G=nx.DiGraph()

    #Add edges and nodes in graph
    G.add_edge(b,op2,weight=INITIAL_OPERATION_TIME)
    G.add_edge(b,op6,weight=INITIAL_OPERATION_TIME)
    G.add_edge(operand1,op6,weight=INITIAL_OPERATION_TIME)
    G.add_edge(operand2,op7,weight=INITIAL_OPERATION_TIME)
    G.add_edge(a,op7,weight=INITIAL_OPERATION_TIME)
    G.add_edge(a,op1,weight=INITIAL_OPERATION_TIME)
    G.add_edge(operand3,op1,weight=INITIAL_OPERATION_TIME)
    G.add_edge(c,op3,weight=INITIAL_OPERATION_TIME)
    G.add_edge(op1,op3,weight=MULT_OPERATION_TIME)
    G.add_edge(op3,op4,weight=MULT_OPERATION_TIME)
    G.add_edge(op2,op4,weight=MULT_OPERATION_TIME)
    G.add_edge(op4,op5,weight=SUB_OPERATION_TIME)
    G.add_edge(op5,op8,weight=SQRT_OPERATION_TIME)
    G.add_edge(op6,op8,weight=MULT_OPERATION_TIME)
    G.add_edge(op8,op9,weight=SUM_OPERATION_TIME)
    G.add_edge(op7,op9,weight=MULT_OPERATION_TIME)
    G.add_edge(op9,x1,weight=DIV_OPERATION_TIME)
    G.add_edge(op6,op10,weight=MULT_OPERATION_TIME)
    G.add_edge(op5,op10,weight=SQRT_OPERATION_TIME)
    G.add_edge(op10,op11,weight=SUB_OPERATION_TIME)
    G.add_edge(op7,op11,weight=MULT_OPERATION_TIME)
    G.add_edge(op11,x2,weight=DIV_OPERATION_TIME)


    return G, input_List, operand_List, output_List, area_Dictionary

def bhaskara_example2():
    #Operations latency
    MULT_OPERATION_TIME=2
    SUM_OPERATION_TIME=1
    SUB_OPERATION_TIME=1
    SQRT_OPERATION_TIME=10
    DIV_OPERATION_TIME=3
    INITIAL_OPERATION_TIME=0

    #Operations reconfigurable area requirements
    AREA_MULT=6
    AREA_SOMA=4
    AREA_SUB=4
    AREA_RAIZ=12
    AREA_DIVISAO=6


    #input nodes
    a="a1"
    b="b1"
    c="c1"

    input_List=[a,b,c]

    #operand Nnodes
    operand1="-1"#-1
    operand2="2"#2
    operand3="4"#4

    operand_List=[operand1,operand2,operand3]


    #output nodes
    x1="y1"
    x2="y2"

    output_List=[x1,x2]

    #operation nodes
    op1="1 op1 x"
    op2="1 op2 x"
    op3="1 op3 x"
    op4="1 op4 -"
    op5="1 op5 sqrt"
    op6="1 op6 x"
    op7="1 op7 x"
    op8="1 op8 +"
    op9="1 op9 /"
    op10="1 op10 -"
    op11="1 op11 /"

    #define operation area requirements
    area_Dictionary = {}
    area_Dictionary["1 op1 x"] = AREA_MULT
    area_Dictionary["1 op2 x"] = AREA_MULT
    area_Dictionary["1 op3 x"] = AREA_MULT
    area_Dictionary["1 op4 -"] = AREA_SUB
    area_Dictionary["1 op5 sqrt"] = AREA_RAIZ
    area_Dictionary["1 op6 x"] = AREA_MULT
    area_Dictionary["1 op7 x"] = AREA_MULT
    area_Dictionary["1 op8 +"] = AREA_SOMA
    area_Dictionary["1 op9 /"] = AREA_DIVISAO
    area_Dictionary["1 op10 -"] = AREA_DIVISAO
    area_Dictionary["1 op11 /"] = AREA_SUB

    G=nx.DiGraph()

    #Add edges and nodes in graph
    G.add_edge(b,op2,weight=INITIAL_OPERATION_TIME)
    G.add_edge(b,op6,weight=INITIAL_OPERATION_TIME)
    G.add_edge(operand1,op6,weight=INITIAL_OPERATION_TIME)
    G.add_edge(operand2,op7,weight=INITIAL_OPERATION_TIME)
    G.add_edge(a,op7,weight=INITIAL_OPERATION_TIME)
    G.add_edge(a,op1,weight=INITIAL_OPERATION_TIME)
    G.add_edge(operand3,op1,weight=INITIAL_OPERATION_TIME)
    G.add_edge(c,op3,weight=INITIAL_OPERATION_TIME)
    G.add_edge(op1,op3,weight=MULT_OPERATION_TIME)
    G.add_edge(op3,op4,weight=MULT_OPERATION_TIME)
    G.add_edge(op2,op4,weight=MULT_OPERATION_TIME)
    G.add_edge(op4,op5,weight=SUB_OPERATION_TIME)
    G.add_edge(op5,op8,weight=SQRT_OPERATION_TIME)
    G.add_edge(op6,op8,weight=MULT_OPERATION_TIME)
    G.add_edge(op8,op9,weight=SUM_OPERATION_TIME)
    G.add_edge(op7,op9,weight=MULT_OPERATION_TIME)
    G.add_edge(op9,x1,weight=DIV_OPERATION_TIME)
    G.add_edge(op6,op10,weight=MULT_OPERATION_TIME)
    G.add_edge(op5,op10,weight=SQRT_OPERATION_TIME)
    G.add_edge(op10,op11,weight=SUB_OPERATION_TIME)
    G.add_edge(op7,op11,weight=MULT_OPERATION_TIME)
    G.add_edge(op11,x2,weight=DIV_OPERATION_TIME)


    return G, input_List, operand_List, output_List, area_Dictionary


def bhaskara():


    #Reconfiguation time
    MULT_RECONFIGURATION_TIME=0.5
    SUM_RECONFIGURATION_TIME=0.5
    SUB_RECONFIGURATION_TIME=0.5
    SQRT_RECONFIGURATION_TIME=0.5
    DIV_RECONFIGURATION_TIME=0.5

    #Operations latency
    MULT_OPERATION_TIME=2
    SUM_OPERATION_TIME=1
    SUB_OPERATION_TIME=1
    SQRT_OPERATION_TIME=10
    DIV_OPERATION_TIME=3
    INITIAL_OPERATION_TIME=0

    #Operations reconfigurable area requirements
    AREA_MULT=6
    AREA_SOMA=4
    AREA_SUB=4
    AREA_RAIZ=12
    AREA_DIVISAO=6

    AREA_MULT=1
    AREA_SOMA=1
    AREA_SUB=1
    AREA_RAIZ=1
    AREA_DIVISAO=1
    #input nodes
    a="a"
    b="b"
    c="c"

    input_List=[a,b,c]

    #operand Nnodes
    operand1="-1"#-1
    operand2="2"#2
    operand3="4"#4

    operand_List=[operand1,operand2,operand3]


    #output nodes
    x1="x1"
    x2="x2"

    output_List=[x1,x2]

    #operation nodes
    op1="op1 x"
    op1r="op1r"
    op2="op2 x"
    op2r="op2r"
    op3="op3 x"
    op3r="op3r"
    op4="op4 -"
    op4r="op4r"
    op5="op5 sqrt"
    op5r="op5r"
    op6="op6 x"
    op6r="op6r"
    op7="op7 x"
    op7r="op7r"
    op8="op8 +"
    op8r="op8r"
    op9="op9 /"
    op9r="op9r"
    op10="op10 -"
    op10r="op10r"
    op11="op11 /"
    op11r="op11r"

    #define operation area requirements
    area_Dictionary = {}
    area_Dictionary["op1 x"] = AREA_MULT
    area_Dictionary["op1r"] = AREA_MULT
    area_Dictionary["op2 x"] = AREA_MULT
    area_Dictionary["op2r"] = AREA_MULT
    area_Dictionary["op3 x"] = AREA_MULT
    area_Dictionary["op3r"] = AREA_MULT
    area_Dictionary["op4 -"] = AREA_SUB
    area_Dictionary["op4r"] = AREA_SUB
    area_Dictionary["op5 sqrt"] = AREA_RAIZ
    area_Dictionary["op5r"] = AREA_RAIZ
    area_Dictionary["op6 x"] = AREA_MULT
    area_Dictionary["op6r"] = AREA_MULT
    area_Dictionary["op7 x"] = AREA_MULT
    area_Dictionary["op7r"] = AREA_MULT
    area_Dictionary["op8 +"] = AREA_SOMA
    area_Dictionary["op8r"] = AREA_SOMA
    area_Dictionary["op9 /"] = AREA_DIVISAO
    area_Dictionary["op9r"] = AREA_DIVISAO
    area_Dictionary["op10 -"] = AREA_DIVISAO
    area_Dictionary["op10r"] = AREA_DIVISAO
    area_Dictionary["op11 /"] = AREA_SUB
    area_Dictionary["op11r"] = AREA_SUB

    G=nx.DiGraph()

    #Add edges and nodes in graph
    G.add_edge(b,op2,weight=INITIAL_OPERATION_TIME)
    G.add_edge(b,op6,weight=INITIAL_OPERATION_TIME)
    G.add_edge(operand1,op6,weight=INITIAL_OPERATION_TIME)
    G.add_edge(operand2,op7,weight=INITIAL_OPERATION_TIME)
    G.add_edge(a,op7,weight=INITIAL_OPERATION_TIME)
    G.add_edge(a,op1,weight=INITIAL_OPERATION_TIME)
    G.add_edge(operand3,op1,weight=INITIAL_OPERATION_TIME)
    G.add_edge(c,op3,weight=INITIAL_OPERATION_TIME)
    G.add_edge(op1,op3,weight=MULT_OPERATION_TIME)
    G.add_edge(op3,op4,weight=MULT_OPERATION_TIME)
    G.add_edge(op2,op4,weight=MULT_OPERATION_TIME)
    G.add_edge(op4,op5,weight=SUB_OPERATION_TIME)
    G.add_edge(op5,op8,weight=SQRT_OPERATION_TIME)
    G.add_edge(op6,op8,weight=MULT_OPERATION_TIME)
    G.add_edge(op8,op9,weight=SUM_OPERATION_TIME)
    G.add_edge(op7,op9,weight=MULT_OPERATION_TIME)
    G.add_edge(op9,x1,weight=DIV_OPERATION_TIME)
    G.add_edge(op6,op10,weight=MULT_OPERATION_TIME)
    G.add_edge(op5,op10,weight=SQRT_OPERATION_TIME)
    G.add_edge(op10,op11,weight=SUB_OPERATION_TIME)
    G.add_edge(op7,op11,weight=MULT_OPERATION_TIME)
    G.add_edge(op11,x2,weight=DIV_OPERATION_TIME)

    G.add_edge(op1r,op1,weight=MULT_RECONFIGURATION_TIME)
    G.add_edge(op2r,op2,weight=MULT_RECONFIGURATION_TIME)
    G.add_edge(op3r,op3,weight=MULT_RECONFIGURATION_TIME)
    G.add_edge(op4r,op4,weight=SUB_RECONFIGURATION_TIME)
    G.add_edge(op5r,op5,weight=SQRT_RECONFIGURATION_TIME)
    G.add_edge(op6r,op6,weight=MULT_RECONFIGURATION_TIME)
    G.add_edge(op7r,op7,weight=MULT_RECONFIGURATION_TIME)
    G.add_edge(op8r,op8,weight=SUM_RECONFIGURATION_TIME)
    G.add_edge(op9r,op9,weight=DIV_RECONFIGURATION_TIME)
    G.add_edge(op10r,op10,weight=SUB_RECONFIGURATION_TIME)
    G.add_edge(op11r,op11,weight=DIV_RECONFIGURATION_TIME)



    return G, input_List, operand_List, output_List, area_Dictionary

"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
|DESCRIPTION: This function is intended to implement an application in a graph to be processed by List Scheduling algorithm|
|INPUTS: N/A                                                                                                                                                                                   |
|OUTPUTS: N/A                                                                                                                                                                               |
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
def input_application():
    [graph, input_List, operand_List, output_List, area_Dictionary] = bhaskara_example()
    #[graph, input_List, operand_List, output_List, area_Dictionary] = bhaskara()
    #[graph1, input_List1, operand_List, output_List1, area_Dictionary1] = bhaskara_example()
    #[graph2, input_List2, operand_List, output_List2, area_Dictionary2] = bhaskara_example2()

    #graph = nx.compose(graph1, graph2)
    #input_List = input_List1 + input_List2
    #output_List = output_List1 + output_List2
    #area_Dictionary2.update(area_Dictionary1)
    #area_Dictionary = area_Dictionary2

    return graph, input_List, operand_List, output_List, area_Dictionary