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

# print(f'Solution to part A: {run_part_A()}')


#Part B
#After some careful deduction, we've discovered the signal patterns layout.
#Which is the following. 
#  dddd
# e    a
# e    a
#  ffff
# g    b
# g    b
#  cccc
#After decoding the outputs with the above layout, 
#! We'll need to join the decoded outputs into a single number
#The tricky part is we have to build the digit codex for every entry in the input
#FUCK
#Alright.  First things first.  
# We know [1, 4, 7, 8] are the only ones that use unique strings


def test_data_load()->np.ndarray:
	# Load data
	with open('test_data.txt', 'r') as f:
		data = f.read().split('\n')
		inputs = [data[i].split("|")[0].strip() for i in range(len(data))]
		outputs = [data[i].split("|")[1].strip() for i in range(len(data))]
	return inputs, outputs

# wiring_dict = {
# 	8:'acedgfb',
# 	5:'cdfbe',
# 	2:'gcdfa',
# 	3:'fbcad',
# 	7:'dab',
# 	9:'cefabd',
# 	6:'cdfgeb',
# 	4:'eafb',
# 	0:'cagedb',
# 	1:'ab'}

def make_wiring_diagram(input_idx:int, in_str:str)->str:
	
	wiring_dict = {x:set() for x in range(10)}

	for inp in in_str.split(' '):
		inp_len = len(inp)


	# First thing is to isolate the lengths of 
	# [1, 4, 7 8] and assign those to the wiring_dict. 
	# Then we need to calculate the others. 
		#Not sure how to do this



inputs, outputs  = test_data_load()
# outputs = ['cdfeb fcadb cdfeb cdbaf', '']
def get_num_fromdict(str_num:str)->int:
	for k, v in wiring_dict.items():
		if set(str_num) == set(v):
			return k

results = []
for idx, out in enumerate(outputs):
	res = []
	wiring_dict = make_wiring_diagram(inputs[idx])
	for o in out.split(" "):
		num = get_num_fromdict(o, wiring_dict)
		if num != None:
			res.append(num)

	#Join them together	
	if len(res) > 1:
		res = int("".join([str(x) for x in res]))
	elif len(res) == 1:
		res = res[0]
	else:
		continue
	
	results.append(res)
	
print(sum(results))