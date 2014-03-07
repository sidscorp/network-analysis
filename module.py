from __future__ import division
import networkx as nx
#import matplotlib.pyplot as plt
import time
from collections import Counter
from itertools import permutations
#from openpyxl import load_workbook
from random import randint
#from openpyxl import Workbook
from math import pow
from math import factorial
import random
from random import choice
import module
import matplotlib.pyplot as plt

def het(n):
	if(n==0):
		return 0
	else:
		return 1

ne = 20 #Number of nodes

#This counts the number of stranger opportunities
def str_count(G):
	list_str=[]
	count = 0
	for i in G.nodes():
		for j in range(i, len(G.nodes())+1):
			if(i!=j):
				if(i<ne+1 and j<ne+1):
					add = 0
					if(G.has_edge(i,j)):
						continue
					else:
						for k in G.nodes():
							if(k!=i and k!=j):
								if(G.has_edge(i,k) and G.has_edge(j,k)):
									add = add+1
					if(add<1):
						list_str.append((i,j))
						count = count+1
	return list_str, count

#This counts number of 1_rec opportunities
def rec_1_count(G):
	list_rec_1=[]
	count = 0
	for i in G.nodes():
		for j in range(i, len(G.nodes())+1):
			if(i!=j):
				if(i<ne+1 and j<ne+1):
					add = 0
					if(G.has_edge(i,j)):
						continue
					else:
						for k in G.nodes():
							if(k!=i and k!=j):
								if(G.has_edge(i,k) and G.has_edge(j,k)):
									add = add+1
					if(add==1):
						list_rec_1.append((i,j))
						count = count+1
	return list_rec_1, count

#This counts number of 2_rec opportunities
def rec_2_count(G):
	list_rec_2=[]
	count = 0
	for i in G.nodes():
		for j in range(i, len(G.nodes())+1):
			if(i!=j):
				if(i<ne+1 and j<ne+1):
					add = 0
					if(G.has_edge(i,j)):
						continue
					else:
						for k in G.nodes():
							if(k!=i and k!=j):
								if(G.has_edge(i,k) and G.has_edge(j,k)):
									add = add+1
					if(add==2):
						list_rec_2.append((i,j))
						count = count+1
	return list_rec_2, count

def rec_3_count(G):
	list_rec_3=[]
	count = 0
	for i in G.nodes():
		for j in range(i, len(G.nodes())+1):
			if(i!=j):
				if(i<ne+1 and j<ne+1):
					add = 0
					if(G.has_edge(i,j)):
						continue
					else:
						for k in G.nodes():
							if(k!=i and k!=j):
								if(G.has_edge(i,k) and G.has_edge(j,k)):
									add = add+1
					if(add==3):
						list_rec_3.append((i,j))
						count = count+1
	return list_rec_3, count

def rec_4_count(G):
	list_rec_4=[]
	count = 0
	for i in G.nodes():
		for j in range(i, len(G.nodes())+1):
			if(i!=j):
				if(i<ne+1 and j<ne+1):
					add = 0
					if(G.has_edge(i,j)):
						continue
					else:
						for k in G.nodes():
							if(k!=i and k!=j):
								if(G.has_edge(i,k) and G.has_edge(j,k)):
									add = add+1
					if(add==4):
						list_rec_4.append((i,j))
						count = count+1
	return list_rec_4, count

def rec_5_count(G):
	list_rec_5=[]
	count = 0
	for i in G.nodes():
		for j in range(i, len(G.nodes())+1):
			if(i!=j):
				if(i<ne+1 and j<ne+1):
					add = 0
					if(G.has_edge(i,j)):
						continue
					else:
						for k in G.nodes():
							if(k!=i and k!=j):
								if(G.has_edge(i,k) and G.has_edge(j,k)):
									add = add+1
					if(add==5):
						list_rec_5.append((i,j))
						count = count+1
	return list_rec_5, count

def rec_6_count(G):
	count = 0
	list_rec_6=[]
	for i in G.nodes():
		for j in range(i, len(G.nodes())+1):
			if(i!=j):
				if(i<ne+1 and j<ne+1):
					add = 0
					if(G.has_edge(i,j)):
						continue
					else:
						for k in G.nodes():
							if(k!=i and k!=j):
								if(G.has_edge(i,k) and G.has_edge(j,k)):
									add = add+1
					if(add>6):
						list_rec_6.append((i,j))
						count = count+1
	return list_rec_6, count


def place(G, list_choice):
	if(list_choice):
		a = list_choice.pop(list_choice.index(choice(list_choice)))
		G.add_edge(a[0], a[1])
		return list_choice



def place_edge(G, p):
	q = het(a[0])*p[0] + het(a[1])*p[1] + het(a[2])*p[2] + het(a[3])*p[3] + het(a[4])*p[4] +het(a[5])*p[5] + het(a[6])*p[6]

	rand = random.random()
	sum = 0
	for i in range(0, len(p)):
		sum = sum + het(a[i])*p[i]
		if(q == 0):
			return "stop", i
		if(rand < sum/q):
			list_1[i] = place(G, list_1[i])
			a[i] = a[i] - 1
			return "lo", i
			break

#The following three functions are for the placing of the edge in the network based on the probability values

#This counts the number of n-triangles in the network G. It is the same as the function k_tri_number(G,n) except that I wanted this to return the list of edges part of the n-triangle
def rec_number(G, number):
	list = []
	count = 0
	for i, j in G.edges():
		add = 0
		for k in G.nodes():
			if(k!=i and k!=j):
				if(G.has_edge(i,k) and G.has_edge(j,k)):
					add = add+1
		if(add==number):
			count = count+1
			list.append((i,j))
	return count

#This determines how a particular edge formed. If it returns 1, it formed as a stranger, if it returns 2, it formed as a 1_rec and if it returns 3, it formed as 2_rec
#This is only applicable at the formation stage of a network. i.e, after an edge has been placed, this simply tells if the edge was placed as a stranger, 1rec, or 2rec
def determine_edge(G, i, j):
	add=0
 	for k in G.nodes():
		if(i!=k and j!=k):
			if(G.has_edge(i,k) and G.has_edge(j,k)):
						add = add + 1
	if(add==0):
		num = 1
		return num
	if(add==1):
		num = 2
		return num
	if(add==2):
		num = 3
		return num

#This does the same thing as rec_number(G,n)
def k_tri_number(G, n):
	count = 0
	for i, j, in G.edges():
		add = 0
		for k in G.nodes():
			if(k!=i and k!=j):
				if(G.has_edge(i,k) and G.has_edge(j,k)):
					add = add+1
		if(add==n):
			count = count+1
	return count

#This function simply returns the combinatoric value of n-choose-m
def comb(n,m):
        return (factorial(n)*factorial(1))/(factorial(m)*factorial(n-m))

#The following three functions calculate the probability values for our expectation formula
#rec_0_calc(n) determins the probability that an edge formed as a stranger while being a part of an n-triangle
def rec_0_calc(n):
	summ = 0

	for j in range(1, n+1):
		summ = summ + ((factorial(n))/((factorial(n-j))*factorial(j)))*factorial((2*n)-j)*factorial(j)
	return (factorial(2*n) + 2*summ)/(factorial(2*n+1))

#rec_1_calc(n) determins the probability that an edge formed as a 1_rec while being a part of an n-triangle

def rec_calc(n, k):
	summ = 0
	for j in range(0,n+1-k):
			summ = summ + comb(n,k)*comb((n-k),j)*pow(2,j)*factorial(2*(n- k) - j)*factorial(j+(2*k))
	return summ/(factorial(2*n+1))
	# This has been working fine . I've been using this for weeks. Not sure what happened today
	# what about if n and k are 0? what is the value of factorial(0).. 1
#This function empties a graph. i.e., removes all edges
def empty_graph(G):
	for i in G.nodes():
		for j in G.nodes():
			if G.has_edge(i,j):
				G.remove_edge(i,j)

#This function is useful in selecting permutations based on index
def perm(alist, apermindex):
    alist = alist[:]
    for i in range(len(alist)-1):
        apermindex, j = divmod(apermindex, len(alist)-i)
        alist[i], alist[i+j] = alist[i+j], alist[i]
    return alist

#This defins the heaviside function for lists. (Not really important)
def heaviside_list(a):
	if(len(a)==0):
		return 0
	else: return 1


#This function actually calculates the expression using our analytic formula and returns a list containing [E_str, E_rec1, E_rec2]
def analytic_expectation(l):
	#it is usd here also. all good here
	lists = []
	E_str = 0
	E_rec_1 = 0
	E_rec_2 = 0
	E_rec_3 = 0
	E_rec_4 = 0
	E_rec_5 = 0
	E_rec_6 = 0
	a = []
	for k in range(0,10):
		a.append(rec_number(l, k))
	for k in range(0,10):
		E_str = E_str + a[k]*rec_0_calc(k)
	for k in range(1,10):
		E_rec_1 = E_rec_1 + a[k]*rec_calc(k, 1)
	for k in range(2,10):
		E_rec_2 = E_rec_2 + a[k]*rec_calc(k, 2)
	for k in range(3,10):
		E_rec_3 = E_rec_3 + a[k]*rec_calc(k, 3)
	for k in range(4,10):
		E_rec_4 = E_rec_4 + a[k]*rec_calc(k, 4)
	for k in range(5,10):
		E_rec_5 = E_rec_5 + a[k]*rec_calc(k, 5)
	for k in range(6,10):
		E_rec_6 = E_rec_6 + a[k]*rec_calc(k, 6)

	lists.append(E_str)
	lists.append(E_rec_1)
	lists.append(E_rec_2)
	lists.append(E_rec_3)
	lists.append(E_rec_4)
	lists.append(E_rec_5)
	lists.append(E_rec_6)
	return lists

def true_expectation(l,p):
	lists = []
	E_str = 0
	E_rec_1 = 0
	E_rec_2 = 0
	a = []
	myeps = 0.0
	for k in range(0,10):
		a.append(rec_number(l, k))
	for k in range(0,7):
		q = myeps
		for j in range(0,k+1):
			q = q + rec_calc(k,j)*(p[j])
		E_str = E_str + a[k]*p[0]*rec_calc(k,0)/q
	for k in range(1,7):
		q = myeps
		for j in range(0,k+1):
			q = q + p[j]*rec_calc(k,j)
		E_rec_1 = E_rec_1 + a[k]*(p[1]*rec_calc(k,1))/q
	for k in range(2,7):
		q = myeps
		for j in range(0,k+1):
			q = q + p[j]*rec_calc(k,j)
		E_rec_2 = E_rec_2 + a[k]*(p[2]*rec_calc(k, 2))/q
	lists.append(E_str)
	lists.append(E_rec_1)
	lists.append(E_rec_2)
	return lists

########################################################
############~Starting Main Model~#######################
########################################################

main_graph = nx.Graph()

node_count = 500
edge_count = 1000

p = [1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7]

ave = []

for i in range(1,node_count+1):
    main_graph.add_node(i)

count = 0
while(len(main_graph.edges()) < edge_count):
	if(len(main_graph.edges()) == 0):
		a = [0,0,0,0,0,0,0]
        list_1 = [0,0,0,0,0,0,0]
        list_1[0], a[0] = str_count(main_graph)
        list_1[1], a[1] = rec_1_count(main_graph)
        list_1[2], a[2] = rec_2_count(main_graph)
        list_1[3], a[3] = rec_3_count(main_graph)
        list_1[4], a[4] = rec_4_count(main_graph)
        list_1[5], a[5] = rec_5_count(main_graph)
        list_1[6], a[6] = rec_6_count(main_graph)
	string, n = place_edge(main_graph, p)
	if(string == 'stop'): break
#	print len(main_graph.edges())
  #H, K = main_graph.order(), main_graph.size()
	degree_1 = main_graph.degree(20)
	ave.append(degree_1)
	count = count+1
	print count

plt.plot(ave)
plt.show()
