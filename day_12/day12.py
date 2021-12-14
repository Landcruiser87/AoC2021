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
# ./day_12/
def data_load()->list:
	with open('./day_12/test_data.txt', 'r') as f:
		data = f.read().splitlines()
		arr = [line.split("-") for line in data]
	return arr

data = data_load()

def make_graph(data:list)->dict:
	graph = {data[start][0]: [] for start in range(len(data))}
	for start, end in data:
		graph[start].append(end)
	return graph

def is_smallcave(node:str)->bool:
	return node.islower()

def count_paths_dfs(node:str='start')->int:
	#Recursive solution to finding all paths through a graph.
	graph = make_graph(data)
	count = 0
	visited = set()
	
	def dfs(node):
		if node not in visited:
			visited.add(node)
			for child in graph[node]:
				dfs(child)
			count += 1

	return count

def run_part_A()->int:
	return count_paths_dfs()
print(f"Solution for Part A: {run_part_A()}")













# def count_paths_dfs(data:list)->list:
# 	graph = make_graph(data)
# 	count = 0
# 	visited = set()
	
# 	def dfs(node):
# 		if node == 'end':
# 			count += 1
# 			return
		
# 		if is_smallcave(node) and node in visited:
# 			return

# 		if is_smallcave(node):
# 			visited.add(node)

	
# 	for node, edges in graph.items():
# 		# if node != 'start':
# 		# 	continue
# 		for edge in edges:
# 			dfs(edge)


# 	return count

# def run_part_A()->int:
# 	return count_paths_dfs(data)
# print(f"Solution for Part A: {run_part_A()}")