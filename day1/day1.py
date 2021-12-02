import numpy as np
##Problem 1
#Goals
#1. Create a function that takes a list of nums, 
#	and returns whether or not the the value preceeding 
#	is increasing or decreasing.

#2. End Goal: Count how many times a depth measurement increases 
#	from the pervious measurement.

#.\day1\
depths = np.loadtxt('.\day1\data.txt', dtype=int)
res_dict = {"Increase":0, "Decrease":0}

def count_slopes(depths:np.array)->int:
	for i in range(1, len(depths)):
		if depths[i] > depths[i-1]:
			res_dict["Increase"] += 1
		else:
			res_dict["Decrease"] += 1
	
	return res_dict["Increase"]

print(f'Problem 1 Solution: {count_slopes(depths)}')


##Problem 2
#Repeat the above calculations but this time. 
# with a 3 measurement sliding window
# So sum the 3 wide sliding window, then compare 
# to the previous window shifted back 1 unit. 

from numpy.lib.stride_tricks import sliding_window_view
res_dict = {"Increase":0, "Decrease":0}

def slide_window_count_slopes(depths:np.array)->int:

	windowed_data = sliding_window_view(depths, window_shape = 3)
	for i in range(len(windowed_data)):
		if sum(windowed_data[i]) > sum(windowed_data[i-1]):
			res_dict["Increase"] += 1
		else:
			res_dict["Decrease"] += 1
	
	return res_dict["Increase"]

print('\n')
print(f'Problem 2 Solution: {slide_window_count_slopes(depths)}')
