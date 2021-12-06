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

def data_load():
	with open('./day5/data.txt') as f:
		data = f.read().splitlines()
		data = [line.replace(" -> ", ",").split(',') for line in data]
		data = np.array([(int(x[0]), int(x[1]), int(x[2]), int(x[3])) for x in data], dtype=int)
	return data

def straight_check(line: np.array):
	return line[0] == line[2] or line[1] == line[3]

def calc_points(line):
	#Generate a list of points contained in the line
	x1, y1, x2, y2 = line
	
	if x1 == x2:
		points = [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
	elif y1 == y2:
		points = [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]
	else:
		points = []
	return points

def add_to_grid(grid, point):
	grid[point[0], point[1]] += 1	

def calc_grid(grid):
	return len(np.where(grid > 1)[0])

data = data_load()
grid = np.zeros((1000,1000), dtype=int)

for line in data:
	#Check for straightness
	if straight_check(line):
		add_line = calc_points(line)
		[add_to_grid(grid, p) for p in add_line]

print(calc_grid(grid))

#data layout
# col
# 0  1  2  3
#x1, y1, x2, y2

# Build a 1000x1000 grid of zeros
# Loop over shape[0]
# Need a check to make sure its not a diagonal line.
	#ie x1 = x2 or y1 = y2
# add a function to drawline
	# Generate a 1d array of points occupied by line
# add a function to add each resulting point to grid
# 



