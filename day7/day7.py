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
	with open('data.txt', 'r') as f:
		data = f.read().split("\n")
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

#For every crab's one movevment, the next costs twice as much
#one move costs 1 fuel
#two moves cost 3 fuel
#three moves cost 6 fuel
#four moves cost 10 fuel

#So, just add in a cost factor for that by squaring it, add the difference and divide by 2

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
