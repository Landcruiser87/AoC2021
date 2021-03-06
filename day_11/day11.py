# Day 11 - Dumbo Octopus

# Part 1
#Assumptions 
# 1. Octopus have an energy level associated with them
# 2. When the energy level gets greater than 9, the that octopus will flash
# 3. If an octopus flashes, it raises every ocotpus energy level around it (including diags) by 1
# 4. When an octopus flashes, it will return its energy level to zero
# 5. With each step, octopuses energy level will increase by 1



import numpy as np
# ./day11/
def data_load()->np.array:
	with open('./day_11/data.txt', 'r') as f:
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

def raise_outer_octopi(data:np.array, row:int, col:int)->np.array:
	#Loop through outer coordinates. 
	for i in range(row-1, row+2):
		for j in range(col-1, col+2):
			if on_board(data, i, j):
				data[i, j] += 1
				
	return data

def flash_check(data:np.array)->int:
	data += 1
	to_analyze = list(zip(np.where(data > 9)[0], np.where(data > 9)[1]))
	flashed = set()
	while to_analyze:
		row, col = to_analyze.pop(0)
		if data[row, col]> 9 and (row, col) not in flashed:	
			raise_outer_octopi(data, row, col)
			flashed.add((row, col))
			to_analyze.extend(list(zip(np.where(data > 9)[0], np.where(data > 9)[1])))
		# print("\n", (row, col), "\n")
		# print(data)

	for row, col in flashed:
		data[row, col] = 0

	return len(flashed)

def run_part_A()->int:
	data = data_load()
	flash_count = 0	
	# print(f'Grid Start:\n{data}')
	for i in range(100):
		# print(f'BeforeCheck for step {i} \n{data}')
		flash_count += flash_check(data)
		# print(f'Current data for step {i} \n{data}')
	return flash_count	

print(f"Solution for Part A: {run_part_A()}")

# part B

def run_part_B()->int:
	data = data_load()
	i=1
	while i < 10000:
		if flash_check(data) == data.size:
			return i 
		i += 1

print(f"Solution for Part B: {run_part_B()}")