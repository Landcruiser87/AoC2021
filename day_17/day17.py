# --- Day 17: Trick Shot ---

# Now we've gotta launch some probes!  

#!Assumptions
# So we're moving our launch spot vertically from (0, 0) top left. 
# As we move our launch spot, we fire off a probe that we want to hit 
# a certain target range (x:x1, y:y1)
# We fire the probe with different Vx and Vy (velocity) directions.

# Drag effects. 
# For every step, our drag decreases our Vx by one, converging to zero (when it will drop straight down)

# Gravity effects. 
# For every step, gravity will increase the Vy component by one.  

#!Goal
# Find the max height we can fire the probe at to still hit the target area.  
# I'm choosing to think of this like battleship just in a different 2d.



import numpy as np
# ./day_17/
def data_load()-> int:
	with open('test_data.txt', 'r') as f:
		data = f.read().split(":")[1].strip()
		x, y = data.split(", ")
		xmin, xmax = x[2:].split("..")
		ymin, ymax = y[2:].split("..")

	return int(xmin), int(xmax), int(ymin), int(ymax)


def target_hit(x:int, y:int)->bool:
	if xmin <= x <= xmax and ymin <= y <= ymax:
		return "Target hit!"
	else:
		return "Target missed!"

(xmin, xmax, ymin, ymax) = data_load()
target_hit(30, -10)
