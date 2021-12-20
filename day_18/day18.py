# --- Day 18: Snailfish ---

# Now we've got snails people. And they do math quite differently than the rest.  

#.Assumptions
# We need to reduce the snails homework
# first off we isolate number pairs that are four brackets deep
# 


import numpy as np
# ./day_18/
def data_load():
	with open('test_data.txt', 'r') as f:
		data = f.read().splitlines()
	return data

def levels(l, depth = -4):
    if not isinstance(l, list):
        yield (l, depth)
    else:
        for sublist in l:
            yield from levels(sublist, depth + 1)


data = data_load()
list(levels(data[4]))
