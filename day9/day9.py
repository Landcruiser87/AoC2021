#Day 9 - Smoke Basin

# Part 1

#Now we're mapping lava tubes along the ocean floor.  
#The tubes release smoke, that settles like rain into the low points
#of the landscape.  

#(Think Top down view)

#Assumptions
# a number corresponds to a height at location
# Range: 0 -9

#!Goals
# 1.  Find the low points where the smoke settles. 
#	- To qualify it needs to be surrounded N, S, E, W by a higher 
#		number
#	- If its on an edge, check 3 sides, etc. 
#		- Will need a function to check borders.
#		- Will need function to check heights around point. 
# 2.  Calculate Risk Level
#	- Risk level = 1 + height
# 3.  Sum up the risk levels of all low points.  

import numpy as np

def data_load()->list:
	with open('./day9/data.txt', 'r') as f:
		data = f.read().splitlines()
		arr = np.array([[int(x) for x in list(line)] for line in data])
	return arr

def height(board):
    return len(board)

def width(board):
    return len(board[0])

def on_board(board, x1, y1):
	ht = height(board)
	wd = width(board)
	if x1 < 0 or y1 < 0 or x1 >= ht or y1 >= wd:
		return False
	else:
		return True


def is_low_point(grid:np.array, x:int, y:int)->bool:
	#Dict of conditions to check borders
	directions = {
		'N': {'x': x-1, 'y': y},
		'S': {'x': x+1, 'y': y},
		'E': {'x': x, 'y': y+1},
		'W': {'x': x, 'y': y-1}
	}
	#Test for low point, sum for each direction, but only if valid. 
	for direction, coords in directions.items():
		if on_board(grid, coords['x'], coords['y']):
			if grid[coords['x'],coords['y']] > grid[x,y]:
				continue
			elif grid[coords['x'],coords['y']] <= grid[x,y]:
				return False

	return True

def run_part_A()->int:
	grid = data_load()
	result = 0
	print(f'Grid Shape:\n{grid.shape}')

	#Loop through coordinates.  Top left is 0,0
	for x in range(grid.shape[0]):
		for y in range(grid.shape[1]):
			#Test for lowpoint
			if is_low_point(grid, x, y):
				# print(f'Low point at {x}, {y}: Risk={grid[x,y]+1}')
				result += grid[x,y] + 1
	return result

print(f'Part A Solution: {run_part_A()}')
