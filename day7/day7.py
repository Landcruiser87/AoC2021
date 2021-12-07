#Part A

#Oh man we've got crabs, whales,  Its a mess out there in the ocean. 
#So we need to optimize crab fuel consumption.  

#Assumptions/Goals
#Crabs only move horizontally. 
#We need to line them all up to blast a hole
#We want to use the least amount of fuel to line them up

import numpy as np

# ./day7/
def data_load()->list:
	with open('./day7/data.txt', 'r') as f:
		data = f.read().split(",")
		data = [int(x) for x in data]
	return data

def run_part_A()->int:
	data = data_load()
	# data = [16,1,2,0,4,2,7,1,2,14]
	fuel_dict = {}
	for crab_line in range(min(data), max(data)+1):
		fuel_cost = 0
		for crab in data:
			fuel_cost += abs(crab - crab_line)
		fuel_dict[crab_line] = fuel_cost

	return min(fuel_dict.values())

print(f'Solution to part A: {run_part_A()}')


#Part B

#Now our crabs are gettin fiesty with our calculations. 
#Apparently we didn't take into account crab fuel consumption. 

#So now we need to figure out how the crabs move


def run_part_B()->int:
	data = data_load()
	# data = [16,1,2,0,4,2,7,1,2,14]
	fuel_dict = {}
	for crab_line in range(min(data), max(data)+1):
		fuel_cost = 0
		for crab in data:
			diffs = abs(crab - crab_line)
			fuel_cost += (((diffs**2) + diffs)//2)
		fuel_dict[crab_line] = fuel_cost

	return min(fuel_dict.values())

print(f'Solution to part B: {run_part_B()}')
