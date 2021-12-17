# --- Day 14: Extended Polymerization ---

# We've got some polymers to make!  Our job is to mutate the input string
# by various insertion rules.  Find the most common pairs, and then the 
# least common pairs and subtract them. 

#!Assumptions
# - Polymer is a string of characters
# rules definitely keep in a dict
# Each rule insertion happens simultaneously
	#Meaning each step, only their pairs at the beginning are considered. 

import numpy as np
from collections import Counter

# ./day_14/
def data_load()-> (dict, str):
	with open('./day_14/data.txt') as f:
		data = f.read().splitlines()
		data = [line.split(" -> ") for line in data]
		polymer = data.pop(0)[0]
		data.pop(0)
		rules = {x[0]:x[1] for x in data}

	return polymer, rules

def pair_insert(polymer:str, rules:dict)-> str:
	"""[Insert rules into polymer.  Returns updated polymer]

	Args:
		polymer (str): [Input polymer string]
		rules (dict): [rules for chain insertion]

	Returns:
		dict: [Updated dict_counter]
	"""	
	res = ""
	for x in range(len(polymer)):
		pair = polymer[x:x+2]
		if pair in rules:
			#Insert the rule
			res += pair[0] + rules[pair]
	#Adds back the last character
	res += polymer[-1]
	
	return res
def run_part_A()-> int:
	polymer, rules = data_load()
	poly_update = pair_insert(polymer, rules)
	for i in range(1, 10):
		poly_update = pair_insert(poly_update, rules)

	dict_counter = Counter(poly_update)

	ans = max(dict_counter.values()) - min(dict_counter.values())
	return ans

print(f"Solution for Part 1: {run_part_A()}")
