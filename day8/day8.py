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
# Numbers [1, 4, 7, 8] all use unique length string id's
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
import itertools


# ./day8/
def data_load()->np.ndarray:
	# Load data
	with open('./day8/data.txt', 'r') as f:
		data = f.read().split('\n')
		data.pop()
		inputs = [data[i].split("|")[0].strip() for i in range(len(data))]
		outputs = [data[i].split("|")[1].strip() for i in range(len(data))]
	return inputs, outputs
  
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


#Part B

#Now that we've figured out the first mapping, its time to do so for the rest of the outputs
#Our task:
#	1.	Find the mapping of each input for each output / display
#	2.  Decode and sum all the displays

#The tricky part is we have to build the digit codex for every code in the input
#FUCK

# ./day8/ 
def data_load_partB()->list:
	with open('./day8/data.txt', 'r') as f:
		data = f.read().splitlines()
	return data

#Initial wiring board Layout from p1
    # Patterns following the following configuration:
    #  aaaa 
    # b    c
    # b    c
    #  dddd 
    # e    f
    # e    f
    #  gggg 

wiring_dict = {		#Length
	"0": 'abcefg',	#6
	"1": 'cf',		#2
	"2": 'acdeg',	#5
	"3": 'acdfg',	#5
	"4": 'bcdf',	#4
	"5": 'abdfg',	#5
	"6": 'abdefg',	#6
	"7": 'acf',		#3
	"8": 'abcdefg',	#7
	"9": 'abcdfg',	#6
	}

def sort_alpha(input_str:str)->str:
	return "".join(sorted(input_str))

def switch_out_char(in_code:str, maps:dict)->str:
	return sort_alpha(maps[code] for code in in_code)

def decoder_ring(in_codes:str, wiring_dict:dict, update_dict:dict, known_code:list)->list:
	
	#Early stop if we've found all the codes
	if len(in_codes) == 0:
		return known_code
	
	#first code
	in_code = in_codes[0]

	for dict_key, dict_code in wiring_dict.items(): 
		#if key identified or length of dict_code isn't equal to the in_code we're deciphering.
		if dict_key in known_code or len(dict_code) != len(in_code):
			continue
		
		#Get the letters from incodes that are unidentified. 
		wires_to_map = [letter for letter in in_code if letter not in update_dict.keys()]

		#Get the letters from wiring_dict that are unindentified.
		wires_to_switch = [letter for letter in dict_code if letter not in update_dict.values()]

		# Check to make sure the wires lengths match. 
		if len(wires_to_map) != len(wires_to_switch):
			continue
		
		perms = itertools.permutations(wires_to_map)
		
		for perm in perms:
			maps = {k:v for k,v in zip(perm, wires_to_switch)}

			if switch_out_char(in_code, {**update_dict, **maps}) != dict_code:
				continue
		
			result = decoder_ring(in_codes[1:], wiring_dict, {**update_dict, **maps}, known_code+[dict_key])

			if result:
				return result
	return None

def run_part_B()->int:
	data = data_load_partB()
	result = 0

	for line in data:
		#Split the line into input/output
		inputs, outputs = line.split(" | ")
		in_codes = inputs.split()
		out_codes = outputs.split()
		
		#sort them by length
		in_codes = sorted([sort_alpha(x) for x in in_codes], key=len)

		#Make/Update the wiring dict
		found = decoder_ring(in_codes, wiring_dict, {}, [])
		if not found:
			print("Failed to decode")
			exit()		
		final_mapping = {k:v for k,v in zip(in_codes, found)}
		
		result += int("".join(final_mapping[sort_alpha(code)] for code in out_codes))
	return result

print(f'Solution to part B: {run_part_B()}')