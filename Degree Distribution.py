#!/usr/bin/env python
"""
Random graph from given degree sequence.
Draw degree rank plot and graph with matplotlib.
"""
__author__ = """Aric Hagberg <aric.hagberg@gmail.com>"""
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#G = nx.gnp_random_graph(100,0.02)
G1 = nx.scale_free_graph(100,alpha=0.05,beta=0.9,gamma=0.05)
G2= nx.scale_free_graph(100,alpha=0.9,beta=0.05,gamma=0.05)


nx.draw_circular(G1,node_color=range(100),cmap=plt.cm.Blues)
nx.draw_circular(G2,node_color=range(100),cmap=plt.cm.Blues)
        
ax=plt.subplot(111)


degree_sequence1=sorted(nx.degree(G1).values(),reverse=True) #degree sequence
degree_sequence2=sorted(nx.degree(G2).values(),reverse=True) #degree sequence
print degree_sequence1
print degree_sequence2

#print "Degree sequence", degree_sequence


ax.loglog(degree_sequence1,'bs',marker='o',label="aglomerado")
ax.loglog(degree_sequence2,'g^',marker='o',label="pouco-aglomerado")
ax.legend()

plt.title("Arranjo do grau por nodo")
plt.ylabel("Grau")
plt.xlabel("Nodo")

#plt.savefig("degree_histogram.png")
plt.show()