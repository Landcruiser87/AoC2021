# Day 12 - Passage Pathing. 

# Yay a graph problem. 

#We're still stuck in a network of caves that we need to navigate our way out of. 
#!Task
#We need to find the number of distinct paths through the cave that start at `start` and end at `end`.

#!Constraints
#The network has a finite number of nodes and edges.
#Small caves -lowercase - visit only once
#Large caves - uppercase - visit multiple times


import numpy as np
# ./day12/
def data_load()->list:
	with open('./day12/test_data.txt', 'r') as f:
		data = f.read().splitlines()
		arr = [list(line) for line in data]
	return arr

data = data_load()

