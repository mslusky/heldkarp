import random
from time import time

# A small graph 
g1 = {(0,1):1,
	  (0,2):1,
	  (0,3):10,
	  (1,2):1,
	  (1,3):3}

# The graph in the original Held-Karp paper
g2 = {(1,2):1,
	  (1,3):1,
	  (1,6):0,
	  (2,3):1,
	  (2,5):0,
	  (3,4):0,
	  (4,5):1,
	  (4,6):1,
	  (5,6):1}	  

def get_random_connected_graph(n, p, max_w, seed=None):
	"""
	returns a random graph.

	The graph is created in two phases. In phase I, each edge is iid added to
	the graph. In phase II, we randomly add edges between components to connect
	the graph.

	n = the number of vertices
	p = the probability of any given edge being added to the graph in phase I
	max_w = The maximum edge weight. Weights will be integers from 1 to max_w. 
	seed = optional random seed
	"""
	if seed == None:
		seed = time()
	random.seed(seed)

	min_vertex_in_component = {v:v for v in range(n)}
	graph = dict()

	# Phase I
	for x in range(n):
		for y in range(x+1, n):
			if random.random() < p: # whether to include the edge in the graph
				graph[(x,y)] = random.randint(1,max_w)
				new_min = min(min_vertex_in_component[x], min_vertex_in_component[y])
				min_vertex_in_component[x] = new_min
				min_vertex_in_component[y] = new_min

	# Phase II
	while len(set(min_vertex_in_component.values())) > 1:
		connecting_edges = [(x,y) for x in range(n) for y in range(x+1,n) \
							if min_vertex_in_component[x] != min_vertex_in_component[y]]

		x,y = random.sample(connecting_edges,1)[0]
		graph[(x,y)] = random.randint(1,max_w)
		new_min = min(min_vertex_in_component[x], min_vertex_in_component[y])
		old_min = max(min_vertex_in_component[x], min_vertex_in_component[y])
		for v in range(old_min,n):
			if min_vertex_in_component[v] == old_min:
				min_vertex_in_component[v] = new_min

	return graph

def bayg29(filename="bayg29.tsp"):
	"""
	return the graph for the bayg29 data set from the TSPLIB.
	Optimal tour is [0, 27, 5, 11, 8, 25, 2, 28, 4, 20, 1, 19, 9, 3, 14, 17, 13, 16, 21, 10, 18, 24, 6, 22, 7, 26, 15, 12, 23]
	with a weight of 1610
	"""
	graph = dict()
	with open(filename) as f:
		for x, line in enumerate(f):
			for y, w in enumerate(line.split()):
				graph[(x,y+1+x)] = int(w)
	return graph

