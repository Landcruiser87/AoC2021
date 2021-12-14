# Day 11 - Dumbo Octopus

# Part 1
#Assumptions 
# 1. Octopus have an energy level associated with them
# 2. When the energy level gets greater than 9, the that octopus will flash
# 3. This will cause all the other octopuses in every direction to flash (including itself)
# 4. This resets the energy level to 0
# 5. With each step, octopuses energy level will increase by 1
# If an octopus flashes, it raises every ocotpus energy level around it (including diags) by 1


import numpy as np
# ./day11/
def data_load()->list:
	with open('./day11/data.txt', 'r') as f:
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

def flash_check(data:np.array)->np.array:
	id_nine = list(zip(np.where(data > 9)[0], np.where(data > 9)[1]))
	flashed_ocotpi = set()
	if id_nine != []:
		while id_nine:
			row, col = id_nine.pop(0)
			if (row, col) not in flashed_ocotpi:
				flashed_ocotpi.add((row, col))
				raise_outer_octopi(data, row, col)
				data[row, col] = 0
				# print("\n", (row, col), "\n")
				# print(data)
		for row, col in flashed_ocotpi:
			data[row, col] = 0
		data = np.where(data > 9, 0, data)

	return data

data = data_load()
flash_count = 0	
# print(f'Grid Start:\n{data}')
for i in range(10):
	data += 1
	# print(f'Current data\n{data} for step {i}')
	data = flash_check(data)
	# print(f'Current data\n{data} for step {i}')
	flash_count += len(np.where(data == 0)[0])

print(flash_count)

