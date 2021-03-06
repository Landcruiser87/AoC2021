import numpy as np
#Day 10: Syntax Scoring

#Part 1

#Next we're having some trouble with the navigation systems and need some error checking. 

#Input
#Bunch of strings of various parentheses/braces/brackets/etc.

#Corrupted line = one that ends with the wrong type of bracket. 
#Some lines can just end incomplete. (ending with open brackets)
#Find and discard corrupted lines first. 
#Ignore the incomplete lines. 

#Stop at decoding at each incorrect closing character for each corrupted line.
def load_data():
	with open('./day_10/data.txt', 'r') as f:
		data = f.read().splitlines()
	return data

pair_dict = {
	"(": ")",
	"[": "]",
	"{": "}",
	"<": ">",
}

point_dict = {
	")": 3,
	"]": 57,
	"}": 1197,
	">": 25137,
}

autoc_dict = {
	")": 1,
	"]": 2,
	"}": 3,
	">": 4,
}

def run_part_A()->int:
	data = load_data()
	score = 0
	for line in data:
		char_list = []
		for char in line:
			if char not in point_dict.keys():
				char_list.append(char)
				
			else:
				if char == pair_dict[char_list[-1]]:
					char_list.pop()
				else:
					score += point_dict[char]
					break
	
	return score

print(f"Solution for Part A: {run_part_A()}")

# Part 2
def run_part_B()->int:
	data = load_data()
	final_scores = []
	
	for line in data:
		score = 0
		char_list = []
		for char in line:
			if char not in point_dict.keys():
				char_list.append(char)
			else:
				if char == pair_dict[char_list[-1]]:
					char_list.pop()
				else:
					char_list = []
					break
		if char_list:
			line_score = [pair_dict[char] for char in char_list[::-1]]
			for auto_key in line_score:
				score = (score * 5) + autoc_dict[auto_key]
			final_scores.append(score)
	return sorted(final_scores)[len(final_scores)//2]

print(f'Solution for Part B: {run_part_B()}')