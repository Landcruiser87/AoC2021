# --- Day 15: Chiton ---

#Well we've almost reached the end of the caves!  But the walls are closing in...  Chitons line the cave walls
#and could easily rip a hole in the ship's hull.  

#We're given top down map of the cave with certain risk levels associated with occupyinig that position
#of the cave.  Our goal is to find the safest (lowest risk level) of any path through.  

#!Assumptions
# - Map is a 2D array of integers
# - Map is rectangular
# - Low ceiling is a high value of risk. 
# - Can't move diagonally
# 

#Plan.  Start top left.  
# 1.  Scan the surrounding positions.
# 2.  Ensure the surrounding pos are within the cave map (ie in the grid indices)
# 3.  Add the point with the lowest risk to the stack. (maybe with point value as a tuple)
# 4.  Repeat until we reach bottom right of grid. 


import numpy as np
# from scipy.sparse.csgraph import shortest_path
from scipy.sparse import csr_matrix
import heapq
from math import inf

# ./day_15/
def data_load()->np.array:
	with open('./day_15/test_data.txt', 'r') as f:
		data = f.read().splitlines()
		arr = np.array([[int(x) for x in list(line)] for line in data])
	return arr


def dijkstra(adj, start, target):
    d = {start: 0}
    parent = {start: None}
    pq = [(0, start)]
    visited = set()
    while pq:
        du, u = heapq.heappop(pq)
        if u in visited: continue
        if u == target:
            break
        visited.add(u)
        for v, weight in adj[u]:
            if v not in d or d[v] > du + weight:
                d[v] = du + weight
                parent[v] = u
                heapq.heappush(pq, (d[v], v))


    return parent, d
def run_part_A():

	data = data_load()
	start_pos = (0, 0)
	final_pos = (data.shape[0]-1, data.shape[1]-1)
	paths, stuffs = dijkstra(data, start_pos, final_pos)
	return sum([sum(path) for path in paths])

print(f"Solution for Part A: {run_part_A()}")





# def run_part_A():

# 	data = data_load()
# 	start_pos = (0, 0)
# 	final_pos = (data.shape[0]-1, data.shape[1]-1)
# 	d_sparse = csr_matrix(data)
# 	paths = shortest_path(d_sparse, directed=True, indices=0, unweighted=False)
# 	return sum([sum(path) for path in paths])

# print(f"Solution for Part A: {run_part_A()}")
