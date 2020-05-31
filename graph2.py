"""Оставные деревья и поиск кратчайшего пути"""
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

graph = {'A': {'B':2, 'C':3},
         'B': {'C':2, 'D':2},
         'C': {'D':3, 'E':2},
         'D': {'F':3},
         'E': {'D':1,'F':1},
         'F': {}}

Graph = nx.DiGraph()
for node in graph:
    Graph.add_nodes_from(node)
    for edge, weight in graph[node].items():
        Graph.add_edge(node,edge, weight=weight)

pos = { 'A': [0.00, 0.50], 'B': [0.25, 0.75],
        'C': [0.25, 0.25], 'D': [0.75, 0.75],
        'E': [0.75, 0.25], 'F': [1.00, 0.50]}

labels = nx.get_edge_attributes(Graph,'weight')
nx.draw(Graph, pos, with_labels=True)
nx.draw_networkx_edge_labels(Graph, pos,
                             edge_labels=labels)
nx.draw_networkx(Graph,pos)
plt.show()

def way(graph,start,end):
    looked_nodes=[]
    way={}
    quie=[start]
    node_end=False
    while not looked_nodes or quie:
        start = quie.pop(0)
        for node_with_edge in graph[start]:
            if node_with_edge  not in looked_nodes and node_with_edge not in quie :
                if node_with_edge is end:
                    node_end=True
                    break
                else:
                    quie.append(node_with_edge)
                    node_end=False

        way.update({start: ([edge for edge in quie ])  if not node_end else [end] })
        looked_nodes.append(start)
    return way



print(way(graph,'A','F'))

w=way(graph,'A','F')

def poping_node(start,end,node,way):
    ways = [node]
    def pop_(node):
        while way[node]:
            edge = way[node][0]
            if edge == end:
                ways.append(edge)
                node = start
                ways.append(node)
            else:
                ways.append(way[node].pop(0))
                node = edge
        ways.pop(-1)
    pop_(node)
    for node in way:
        if way[node] and end not in way[node]:
            for old_node in graph:
                if node in graph[old_node]:
                    ways.extend([old_node, node])
                    pop_(node)

    return ways

ways=poping_node('A','F',list(w.keys())[0],w)

def in_seach(from_,array):
    buffer=[]
    for element in array:
        if element == from_:
            start=[element]
            buffer.append(start)
        else:
            buffer[-1].append(element)

    for array in buffer:
        summ=0
        for el in array[:-1]:
            summ+=graph[el][array[array.index(el)+1]]
        array.append(summ)

    buffer=sorted(buffer,key=lambda x:x[-1])

    return buffer


print(in_seach('A',ways))