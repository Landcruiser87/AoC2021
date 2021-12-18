# --- Day 14: Extended Polymerization ---

# We've got some polymers to make!  Our job is to mutate the input string
# by various insertion rules.  Find the most common pairs, and then the 
# least common pairs and subtract them. 

#!Assumptions
# - Polymer is a string of characters
# rules definitely keep in a dict
# Each rule insertion happens simultaneously
	#Meaning each step, only their pairs at the beginning are considered. 

from collections import Counter, defaultdict
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
	"""[Insert rules into polymer]

	Args:
		polymer (str): [Input polymer string]
		rules (dict): [rules for chain insertion]

	Returns:
		str: [Updated polymer string]
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

# print(f"Solution for Part A: {run_part_A()}")

#Turns out you can't just increase the range and compute the same.  List values get way too big. 
# Soooooooo.  time for a bunch of Counters or dictionaries

def pair_insert_dos(dict_counter:dict, rules:dict)-> dict:
	#Only want to pass counters back and forth.  Can't compute string as it gets ginormous

	static_dict = dict_counter.copy()
	for pair, val in static_dict.items():
		if val > 0:
			if pair in rules:
				#Insert the rule, but update the dict_counter.
				dict_counter[pair[0] + rules[pair]] += val
				dict_counter[rules[pair] + pair[1]] += val
				dict_counter[pair] -= val

	return dict_counter

def run_part_B()-> int:
	polymer, rules = data_load()

	#Initialize counter dict
	freq_dict = defaultdict(int)

	#start the madness with the initial pairs.  Add them to the defaultdict. 
	for x in range(len(polymer)-1):
		freq_dict[polymer[x:x+2]] += 1
	

	for i in range(10):
		#update the freq_dict for every step
		freq_dict = pair_insert_dos(freq_dict, rules)

	final_counts = defaultdict(int)
	for pairs in freq_dict.keys():
		for ch in pairs:
			final_counts[ch] += freq_dict[pairs]

	# counts = {k: (v + 1) // 2 for k, v in final_counts.items()}

	for key, val in final_counts.items():
		final_counts[key] = (val + 1) // 2

	ans = max(final_counts.values()) - min(final_counts.values())
	return ans

print(f"Solution for Part B: {run_part_B()}")