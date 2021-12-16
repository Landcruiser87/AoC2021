# --- Day 13: Transparent Origami --

# Now the elves have reached a volcanic cave system
# Using a thermal imaging camera they haven't set up, they first need to get it working. 

#Our input is a transparent piece of paper with random dots.  
#Our job is to decode these dogs after we fold the piece of paper. 

#!Assumptions
#Dot points in first 1000 lines of input
#Folding instructions on lines 1000+
#Horiz = means fold the paper UPWARDS
#Vert = means fold the paper LEFTWARDS
#No fold lines will be input on a dot
#Top left coordinate is zero zero

#Increase in x -> move to right
#increase in y -> move down

import numpy as np
from inspect import stack

# ./day_13/
def data_load()->(list, list):
	caller = stack()[1].function
	with open('./day_13/data.txt', 'r') as f:
		data = f.read().splitlines()
		data, fold = data[:data.index("")], data[data.index("")+1:]
		data = [line.split(",") for line in data]
		data = [tuple(map(int, line)) for line in data]
		fold = [line.replace("fold along ", "") for line in fold]
		fold = [line.split("=") for line in fold]
		folds = []
		if caller == "run_part_A":
			folds.append((fold[0][0], int(fold[0][1])))
		elif caller == "run_part_B":
			for x, y in fold:
				folds.append((x, int(y)))

	return data, folds

#Increase in x -> move to right
#increase in y -> move down

def make_grid(data:list)->np.array:
	#Flipping row and column def.  I can't think in x -> right, y -> down.
	mx_rows = max([line[1] for line in data])+1
	mx_cols = max([line[0] for line in data])+1
	grid = np.zeros((mx_rows,mx_cols), dtype=int)
	for col, row in data:
		grid[row, col] = 1 
	return grid


def update_grid(grid:np.array, temp_grid:np.array)->np.array:
	#update the grid with the new folded grid
	for row in range(temp_grid.shape[0]):
		for col in range(temp_grid.shape[1]):
			if temp_grid[row, col] == 1:
				grid[row, col] = 1

	grid = grid[:temp_grid.shape[0], :temp_grid.shape[1]]
	return grid

def fold_it_up(grid:np.array, folds:list)->(int, np.array):
	for direction, div_line in folds:
		# print(f"Folding {direction} at {div_line}")
		# print(f'Pre fold shape: {grid.shape}')
		#for each direction, fold the paper along that axis
		if direction == "x":
			#fold along the columns
			temp_grid = np.flip(grid[:, div_line+1:], axis=1)
			grid = update_grid(grid, temp_grid)

		if direction == "y":
			#flip the rows
			temp_grid = np.flip(grid[div_line+1:, :], axis=0)
			grid = update_grid(grid, temp_grid)

	return len(np.where(grid == 1)[0]), grid

def print_grid(grid:np.array):

	print_g = np.zeros((grid.shape[0], grid.shape[1]), dtype=str)
	#replace the zeros with a period
	print_g[grid == 0] = "."
	#replace the ones with a #
	print_g[grid == 1] = "#"
	print_g = print_g.tolist()
	print_g = ["".join(row) for row in print_g]
	for grid in print_g:
		print(grid)

def run_part_A()->int:
	data, folds = data_load()
	grid = make_grid(data)
	dots, grid = fold_it_up(grid, folds)
	return dots

print(f'Solution to Part A: {run_part_A()}')

def run_part_B()->str:
	data, folds = data_load()
	grid = make_grid(data)
	dots, grid = fold_it_up(grid, folds)
	print_grid(grid)
	return "Above grid"

print(f'{run_part_B()} Code for thermal Camera: Part B')

