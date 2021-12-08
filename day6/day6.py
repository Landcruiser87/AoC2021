#Part 1

#Heeeeere fishy fishy

#So for this problem we're looking at lanternfish growth rate modeling and how fast they regenerate. 

#Assumptions
#1. model a fish as a single number that represents the number of days until it creates a new lanternfish
	#This would explain the input.  List of ints
#2. When a fish rebirths, its timer is set to 6, and an additional fish is added to the list
#3. If its on its first cycle, add 2 more days = 8 total days
#The new lanternfish starts with an internal timer of 8 and does not start counting down until the next day.

import numpy as np

def data_load()->list:
	with open('./day6/data.txt', 'r') as f:
		data = f.read().split(",")
		data = [int(x) for x in data]
	return data

def run_part_A():
	data = data_load()
	# data = [3,4,3,1,2]
	days = 80

	# print(f'Initial State : {data}')
	while days > 0:
		for i in range(len(data)):
			if data[i] == 0:
				data[i] = 6
				data.append(8)
			else:
				data[i] -= 1

		days -= 1
		# print(f'After day {abs(days-18)} : {data}')
	
	return len(data)

print(f'Solution to part A: {run_part_A()}')

# Part B
#Well now these fish are out of control.  
#They live forever and have unlimited food and space. 
#How many lanternfish after 256 days.  

#Ran into a lot of memory problems with list implmentation
#so wound up going with a Counter() instead. 

from collections import Counter

def run_part_B():
	data = data_load()
	# data = [3,4,3,1,2]
	days = 256

	fish_counter = Counter(data)

	for day in range(days):
		#Get the counts of zero in fish_counter.
		zero_town = fish_counter[0]

		#Next iterate through the possible vals. 
		#For each possible val, set the current value to the one less in the index. 
		#Which should be the valid count for that index as its iterating down each fish timer, and adding zeros for every day based on 
		#the previous days zero count. 

		for x in range(1, 10):
			fish_counter[x - 1] = fish_counter[x]
			
		fish_counter[6] += zero_town
		fish_counter[8] += zero_town

	return sum(fish_counter.values())

print(f'Solution to part B: {run_part_B()}')



