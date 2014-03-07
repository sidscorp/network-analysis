# This file, apart from implementing a network formation model, also demonstrates the use of a Black Box optimization technique 
# implemented via Pybrain (pybrain.org)


from  __future__ import division
import module
import math
import networkx as nx
from numpy import mean
from numpy import std
from pybrain.optimization import CMAES
import time
start_time = time.time()

zac = nx.karate_club_graph()
#print module.rec_number(zac,0), module.rec_number(zac,1), module.rec_number(zac,2)

er = nx.florentine_families_graph()
countess = 0
def graph_function(p):
	if(p[0]<0): p[0] = p[0]*(-1)
	if(p[1]<0): p[1] = p[1]*(-1)
	if(p[2]<0): p[2] = p[2]*(-1)

	q = p[0] + p[1] + p[2]
	p[3] = p[4] = p[5] = p[6] = 0
	p[0] = p[0]/q
	p[1] = p[1]/q
	p[2] = p[2]/q

	nodes = 20
	edges = 50
	simulations = 10
#	tri_count = [module.rec_number(er,0), module.rec_number(er,1), module.rec_number(er,2)]
	tri_count = [5.6,8.36,13.96]
	tri_0 = []
	tri_1 = []
	tri_2 = []
	count = 0

	while(count<simulations):
		main = nx.Graph()

		for i in range(1,nodes+1):
			main.add_node(i)

		while(len(main.edges())<edges):
			string, n = module.place_edge(main, p)
			if(string == 'stop'): break

		tri_0.append(module.rec_number(main,0))
		tri_1.append(module.rec_number(main,1))
		tri_2.append(module.rec_number(main,2))
		count = count + 1
		print count

	return pow((mean(tri_0) - tri_count[0]),2) + pow((mean(tri_1) - tri_count[1]),2) + pow((mean(tri_2) - tri_count[2]),2)

def objF(p) : return graph_function(p)

p0 = [0.333,0.3333,0.3333,0,0,0,0]
#p0 = [1/7,1/7,1/7,1/7,1/7,1/7,1/7]


l = CMAES(objF, p0)
l.verbose = True
l.minimize = True
l._notify()
l.desiredEvaluation = 3



g = l.learn()
if(g[0][0]<0): g[0][0] = g[0][0]*(-1)
if(g[0][1]<0): g[0][1] = g[0][1]*(-1)
if(g[0][2]<0): g[0][2] = g[0][2]*(-1)
summ = g[0][0] + g[0][1] + g[0][2]
print g[0][0]/summ, g[0][1]/summ, g[0][2]/summ
print g[1]
end_time = time.time()
print "The optimization took ", end_time - start_time, " seconds"
