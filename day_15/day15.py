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

# ./day_15/
def data_load()->np.array:
	with open('./day_15/test_data.txt', 'r') as f:
		data = f.read().splitlines()
		arr = np.array([[int(x) for x in list(line)] for line in data])
	return arr

def on_board(data:np.array, x1:int, y1:int)->bool:
	ht = data.shape[0]
	wd = data.shape[1]
	if x1 < 0 or y1 < 0 or x1 >= ht or y1 >= wd:
		return False
	else:
		return True


def scan_for_min(data:np.array, row:int, col:int)->tuple:
	#Loop through outer perimeter. 
	perims = []
	for i in range(row-1, row+2):
		for j in range(col-1, col+2):
			if on_board(data, i, j):
				# Will need logic here to find the minium of the square perimeter.  
				# Probably just flatten it out and find the min, then index it. 
				# 	Also need logic to handle edge cases in case of tie. 
				# 	Which will require a 1 cell increase in the perimeter, 
				# 	and check those values. 
				
				#current value point doesn't matter.  Only the perimeter. 
				perims.append(((i, j), data[i, j]))

	#Pop off the center point
	perims.pop(perims.index(((row, col), data[row, col])))
	#Find the min of the perimeter.
	min_perim = min(perims, key=lambda x: x[1])
	#print(min_perim)
	
	if min_perim > 2:
		scan_for_min(data, row, col)
	else:
		return min_perim[0]

def run_part_A():
	data = data_load()
	final_pos = (data.shape[0]-1, data.shape[1]-1)
	path = []
	# Start at top left.
	for x in range(data.shape[0]):
		for y in range(data.shape[1]):
			next_point = scan_for_min(data, x, y)
			path.append(next_point)
			temp = data.copy()
			temp[next_point] = 100
			print(temp)
			del temp

			if next_point == final_pos:
				return sum(data[path] for path in paths)
			
print(f"Solution for Part A: {run_part_A()}")

