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
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

# ./day_15/
def data_load()->np.array:
	with open('test_data.txt', 'r') as f:
		data = f.read().splitlines()
		arr = np.array([[int(x) for x in list(line)] for line in data])
	return arr

def run_part_A():

	data = data_load()
	start_pos = (0, 0)
	final_pos = (data.shape[0]-1, data.shape[1]-1)
	d_sparse = csr_matrix(data)
	paths = dijkstra(d_sparse, directed=True, indices=start_pos, unweighted=False)
	return sum([sum(path) for path in paths])

print(f"Solution for Part A: {run_part_A()}")
