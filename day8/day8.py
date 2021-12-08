# Part A

# This one's a doozy.  
# In our great escape from the whale, we noticed some displays were malfunctioning
# Showing poorly rendered images. 

#Images are shown with the following format. 
#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

# different sections are turned on by string inputs (wires)
# But their mapping isn't direct.  The segments are messed up.
# ie - we can't just read the above pattern and assume that section is on. 
#! Our goal for part A is to find the number of times 
#! [1, 4, 7, 8] appear in the output. 
# Assumptions:

# The image is static in size.  
# Wires are connected to strings a-g
# Numbers [1, 4, 7, 8] all use unique string id's
	#ie, these are the keys to deducing the rest i'd bet
# Image count for turning on
#0:6- count repeated
#1:2- unique
#2:5- count repeated
#3:5- count repeated
#4:4- unique
#5:5- count repeated
#6:6- count repeated
#7:3- unique
#8:7- unique
#9:6- count repeated

#						Input format:
# [10 unique signal patterns] | [four digit output]

import numpy as np

# ./day8/
def data_load()->np.ndarray:
	# Load data
	with open('./day8/data.txt', 'r') as f:
		data = f.read().split('\n')
		data.pop()
		inputs = [data[i].split("|")[0].strip() for i in range(len(data))]
		outputs = [data[i].split("|")[1].strip() for i in range(len(data))]
	return inputs, outputs
  

# test = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab', 'cdfeb fcadb cdfeb cdbaf']
# inputs, outputs = test[0], test[1]
def run_part_A()->int:
	count_dict = {k:0 for k in range(9)}
	inputs, outputs = data_load()
	for out in outputs:
		for o in out.split(" "):
			out_len = len(o)
			if out_len == 2:
				count_dict[1] += 1
			elif out_len == 4:
				count_dict[4] += 1
			elif out_len == 3:
				count_dict[7] += 1
			elif out_len == 7:
				count_dict[8] += 1
	return sum(count_dict.values())

print(f'Solution to part A: {run_part_A()}')
