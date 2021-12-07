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

def data_load():
	with open('./day6/data.txt', 'r') as f:
		data = f.read().split(",")
		data = [int(x) for x in data]
	return data

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
	

print(f'Solution to part A: {len(data)}')

# Part B

#Well now these fish are out of control.  
#They live forever and have unlimited food and space. 
#How many lanternfish after 256 days.  



