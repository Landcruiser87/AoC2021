import numpy as np

# Part 1

#Now we've got VENTS PEOPLE
#So, think of a 10x10 grid looking down at the ocean floor.  
#You're getting a list of tuples that dictate the coordinate path of the line
#x1, y1 is the starting point, x2, y2 is the ending point
#line segments include start and end
#Only looking at horizontal and vertical lines
	#ie x1 = x2 or y1 = y2
	#Means eval function will probably operate off either truth above
#Our job is to find points where the lines overlap (ie share points)
	#Could use sets again here
#We want to count how many points they share overlapping lines that 
#count more than 2

# ./day5/
def data_load():
	with open('./day5/data.txt') as f:
		data = f.read().splitlines()
		data = [line.replace(" -> ", ",").split(',') for line in data]
		data = np.array([(int(x[0]), int(x[1]), int(x[2]), int(x[3])) for x in data], dtype=int)
	return data

def straight_check(line: np.array)-> bool:
	return line[0] == line[2] or line[1] == line[3]

def calc_partA_points(line:np.array)-> np.array:
	#Generate a list of points contained in non-diagonal line
	x1, y1, x2, y2 = line
	
	if x1 == x2:
		points = [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
	elif y1 == y2:
		points = [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]
	else:
		points = []
	return points

def add_to_grid(grid:np.array, point:tuple):
	grid[point[0], point[1]] += 1	

def calc_grid(grid:np.array)-> int:
	return len(np.where(grid > 1)[0])

data = data_load()
grid = np.zeros((1000,1000), dtype=int)

for line in data:
	#Check for straightness
	if straight_check(line):
		line_points = calc_partA_points(line)
		[add_to_grid(grid, p) for p in line_points]

print(calc_grid(grid))



#Part B

#Now we have to calculate the diagonals.  Time for a new calc_points function

data = data_load()
grid = np.zeros((1000,1000), dtype=int)


def calc_partB_points(line:np.array)-> np.array:
	#Generate a list of points contained in non-diagonal line
	x1, y1, x2, y2 = line
	
	if x1 == x2:
		points = [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
	elif y1 == y2:
		points = [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]
	else:
		points = gimme_dat_diag(x1, y1, x2, y2)
	return points

def gimme_dat_diag(x1, y1, x2, y2):
	#Generate a list of points contained in diagonal line
	dx = abs(x2 - x1)
	dy = abs(y2 - y1)
	assert dx == dy
	dxx, dyy = np.diag_indices(n=dx+1, ndim=2)
	#four directions	#NE, SE, SW, NW
	
	#NE = increasing x, increasing y
	# [32,123,576,667]
	if x1 < x2 and y1 < y2:
		dxx = dxx + min(x1, x2)
		dyy = dyy + min(y1, y2)
	
	#SE = decreasing x, increasing y
	# [610,228,468,370]	
	elif x1 > x2 and y1 < y2:
		dxx = abs(dxx - max(x1, x2))
		dyy = dyy + min(y1, y2)

	#SW = decreasing x, decreasing y
	# [171,52,149,30]
	elif x1 > x2 and y1 > y2:
		dxx = abs(dxx - max(x1, x2))
		dyy = abs(dyy - max(y1, y2))

	#NW = increasing x, decreasing y
	#[60, 140, 96, 104]
	elif x1 < x2 and y1 > y2:
		dxx = dxx + min(x1, x2)
		dyy = abs(dyy - max(y1, y2))
	else:
		raise ValueError("Somethins' whack")
	di_arr = np.stack([dxx, dyy], axis=1)
	return di_arr

for line in data:
# line = [60, 140, 96, 104]
	line_points = calc_partB_points(line)
	[add_to_grid(grid, p) for p in line_points]

print(calc_grid(grid))

