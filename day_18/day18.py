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
	with open('./day_18/test_data.txt', 'r') as f:
		data = f.read().splitlines()
		data = [eval(line) for line in data]
	return data

def check_depth(l, depth = -1):
    if not isinstance(l, list):
        yield (l, depth)
    else:
        for sublist in l:
            yield from check_depth(sublist, depth + 1)

#!todo. Might need function to rebuild the maninpulated string for mag calcs
def rebuild_levels(l, depth=0):
	#Rebuild the list with braces
	for tupes in l:
		if isinstance(tupes, tuple):
			left_brac = (tupes[1] + 1) * '['
			l[l.index(tupes)] = '(' + str(tupes[0]) + ',' + str(tupes[1]) + ')'
		else:
			l[l.index(tupes)] = str(tupes)
	#Rebuild the list with braces
	for tupes in l:
		
def reduce_list():
	pass

def explode():
	pass

def split():
	pass

def magnitude():
	return [3*pair[0], 2*pair[1]]



data = data_load()

test = list(check_depth(data[1]))	
test_dos = rebuild_levels(test)

	

#Plan of attack. 
# get the levels of each number.  Then when you need to split/explode. 
#index the number above or below the pair you're looking at. 
#will have to do some tricky list removal too.  
