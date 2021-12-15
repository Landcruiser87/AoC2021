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
	with open('./day_12/data.txt', 'r') as f:
		data = f.read().splitlines()
		arr = [line.split("-") for line in data]
	return arr

def make_graph(data:list)->dict:
	#Make a dictionary of all nodes and possible edges
	#dict[leftsplit] : [list of rightsplit]]
	lefts = {data[start][0]: [] for start in range(len(data))}
	rights = {data[end][1]: [] for end in range(len(data))}
	graph = {**lefts, **rights}

	#Add all edges to graph
	for start, end in data:
		graph[start].append(end)
		graph[end].append(start)
	return graph

def is_smallcave(node:str)->bool:
	#Checks if lowercase
	return node.islower()

def count_paths(node:str='start')->int:
	#Recursive solution to finding all paths through a graph. 
	data = data_load()
	count = 0
	graph = make_graph(data)
	visited = set()

	def dfs(node):
		#If its the end node, thats a path! Increase count and return
		nonlocal count	
		if node == 'end':
			count += 1
			return
		#Make sure we haven't visited and its a small cave
		if is_smallcave(node) and node in visited:
			return

		#Add node to visited
		if is_smallcave(node):
			visited.add(node)

		#Add all neighbors to queue
		for edge in graph[node]:
			if edge == 'start':
				continue
			dfs(edge)
		#Deque node from visited
		if is_smallcave(node):
			visited.remove(node)
	#Recurse
	dfs(node)

	return count

def run_part_A()->int:
	return count_paths()
print(f"Solution for Part A: {run_part_A()}")


#New parameters:

#1. Small caves can be visited at most twice. 
#	1b. If one cave is visited twice, we can only visit the rest of the small caves
#		once.

#2. Large caves can be visited at most once.
#3. Start and end caves, can only be visited once each.

#Thinking i might just use a dict of sets?
#Or a dict of counts of each path node.  
#Such that once a small cave is visited twice, 
#then i can only add one cave for the following small caves.  


def count_paths_again(node:str='start')->int:
	#Recursive solution to finding all paths through a graph. 
	data = data_load()
	count = 0
	graph = make_graph(data)
	visited = {node:0 for node in graph.keys()}
	
	def dfs_dos(node):

		nonlocal count	
		#If its the end node, thats a path! Increase count and return
		if node == 'end':
			count += 1
			return
		# If small cave, and visited twice, return
		#Uses integer counter to make sure only one cave is above 2
		if is_smallcave(node):
			visited[node] += 1
			visit_limit = 0
			for key in visited.keys():
				if visited[key] > 1:
					visit_limit += 1

					if visited[key] > 2:
						visited[node] -= 1
						return

			if visit_limit > 1:
				visited[node] -= 1
				return
		# Add all neighbors to queue
		for edge in graph[node]:
			if edge == 'start':
				continue
			#Unless its a start cave, recurse
			dfs_dos(edge)

		#Deque node from visited
		if is_smallcave(node):
			visited[node] -= 1
	#Recurse
	dfs_dos(node)

	return count


def run_part_B()->int:
	return count_paths_again()
print(f"Solution for Part B: {run_part_B()}")