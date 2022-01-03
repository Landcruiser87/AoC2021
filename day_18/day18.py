# --- Day 18: Snailfish ---

# Now we've got snails people. And they do math quite differently than the rest.  

#.Assumptions
# We need to reduce the snails homework
# first off we isolate number pairs that are four brackets deep
# Using rescusive level function, list out each number and its 
# level in the list.  This will eliminate the need for brackets.

# 

import numpy as np

# ./day_18/
def data_load():
	with open('test_data.txt', 'r') as f:
		data = f.read().splitlines()
		data = [eval(line) for line in data]
	return data

def get_depths(lev, depth = 0):
	if not isinstance(lev, list):
		yield (lev, depth)
	else:
		for sublist in lev:
			yield from get_depths(sublist, depth + 1)

# depth_list = [[0,'Hips'],[1,'Spine'],[2,'Spine1'],[3,'Spine2'],[4,'Neck'],[5,'Head'],[6,'HeadTop_End'],[4,'LeftShoulder']]
			# pair_count += 1
			# if pair_count <= 2:	
			# 	output.extend([int_add])
			# else:
			# 	#!TODO Fix edge case here of multiple lists in a level
			# 	output = output + int_add
			# 	pair_count = 0

def split_list(output:list)->(list, list):
	return output[:len(output)//2], output[len(output)//2:]


def construct(depth_list, current_level=1):
	output = []
	pair_count = 0
	while len(depth_list) > 0:
		int_add, new_level = depth_list[0]
		if new_level == current_level:
			pair_count += 1
			if pair_count > 2:
				return output
			else:
				output.append(int_add)
				depth_list.pop(0)


		elif new_level > current_level:
			child = construct(depth_list, new_level)
			output.append(child)

		else:
			return output

	return output
#Loads up to the first 3 lists right, but fails when more lists are on the same level. 
#fak


def run_part_A():
	data = data_load()
	for i, line in enumerate(data):
		#Transforms list into a list of depth tuples
		_open = 0
		for ch in i:
			if ch == '[':
				_open += 1
			elif ch == ']':
				_open -= 1
			

		# if any(pair[1] == 4 for pair in depths):
			# esploded = explode(test)
		


print(f'Solution for part A: {run_part_A()}')


def split():
	pass

def magnitude():
	return [3*pair[0], 2*pair[1]]

def explode(counts: list):
	pass	


#Plan of attack. 
# get the levels of each number.  Then when you need to split/explode. 
#index the number above or below the pair you're looking at. 
#will have to do some tricky list removal too.  

				



# def rebuild_levels(lev, depth=0):
# 	# Input: list of tuples (number, depth)
# 	# Output: recreated nested list

# 	rebuild_str = ""
# 	for i, (num, l_dep) in enumerate(lev):
		
# 		#Start of levels.  Match the depth appropriately
# 		if i == 0:
# 			rebuild_str += "["*l_dep + str(num) + ","
# 			continue		
		
# 		#Check end of input text
# 		if i == len(lev)-1:
# 			rebuild_str += str(num) + "]"*l_dep
# 			break

# 		#Check if current level is same as previous level
# 		if l_dep == lev[i-1][1]:
# 			rebuild_str += str(num) + "]"*(l_dep - lev[i+1][1]) + ","
# 			continue

# 		#Check if current level is deeper than previous level
# 		if l_dep < lev[i-1][1]:
# 			rebuild_str += "["*(l_dep - lev[i-1][1])
		
# 		#If the current level is shallower than the next level
# 		elif l_dep > lev[i-1][1]:
# 			rebuild_str += "["*(l_dep - lev[i-1][1]) + str(num) + ","
	
# 	return eval(rebuild_str)
	



# Might use this later
# https://stackoverflow.com/questions/66946328/how-to-get-all-elements-at-a-specific-depth-level-in-a-nested-list
# output = []
# def get_them_fours(lists, d=4):
#     if d == 1:
#         return output.extend(lists)

#     for sub_list in lists:
#         extract(sub_list, d - 1)



	# #Loop through list of tuples
	# for i in range(len(lev)):
	# 	#Check for end of lev
	# 	if i == len(lev)-1:
	# 		if rebuild_str[-1] == ',':
	# 			temp_str = temp_str + str(lev[i][0]) + ("]" * lev[i][1])
	# 		else:
	# 			temp_str = temp_str + "," + str(lev[i][0]) + ("]" * lev[i][1])
			
	# 		rebuild_str = rebuild_str + temp_str
	# 		break
	# 	#Check if next tuple is on the same level
	# 	if lev[i][1] == lev[i + 1][1]:
	# 		#if so, add to temp_str
	# 		temp_str = ("[" * lev[i][1]) + str(lev[i][0]) + ","
	# 	else:
	# 		temp_str = temp_str + str(lev[i][0]) + ("]" * (lev[i][1] - lev[i+1][1]))
