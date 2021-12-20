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
import itertools

# ./day_17/
def target_load()-> int:
	with open('./day_17/data.txt', 'r') as f:
		data = f.read().split(":")[1].strip()
		x, y = data.split(", ")
		xmin, xmax = x[2:].split("..")
		ymin, ymax = y[2:].split("..")

	return int(xmin), int(xmax), int(ymin), int(ymax)


def target_hit(x:int, y:int)->bool:
	if xmin <= x <= xmax and ymin <= y <= ymax:
		# "Target hit!"
		return True 
	else:
		# "Target missed!"
		return False

def fire_the_cannons(xx:int, yy:int)->int:
	x, y = 0, 0
	hit_list = []
	traj_max = 0

	while y >= ymin and x <= xmax:
		x += xx
		y += yy

		if y > traj_max:
			traj_max = y
		
		if target_hit(x, y):
			hit_list.append(traj_max)
			# print(f"Hit at {xx}, {yy}")
			break
		
		if xx > 0:
			xx -= 1
		if xx < 0:
			xx += 1
		
		yy -= 1

	if not hit_list:
		return None, False

	return traj_max, True

def run_part_A():
	global xmin, xmax, ymin, ymax
	(xmin, xmax, ymin, ymax) = target_load()
	
	heights = []
	#Only looking in positive firing ranges as this is a height contest,
	x_rng, y_rng = range(200), range(-200,200)
	firing_grid = np.array(list(itertools.product(x_rng, y_rng)))

	for x, y in firing_grid:
		# print(f'firing vectors at x:{x}, y:{y}')
 
		height, hit_bool = fire_the_cannons(x, y)

		if hit_bool:
			# print(f"Hit with {x}, {y}")
			# print(f"Max height: {height")
			heights.append(height)
		else:
			continue

	if len(heights) > 0:
		return max(heights)

print(f"Solution for Part A: {run_part_A()}")


def run_part_B():
	global xmin, xmax, ymin, ymax
	(xmin, xmax, ymin, ymax) = target_load()
	
	battleships = []
	x_rng, y_rng = range(200), range(-200,200)
	# x_rng, y_rng = range(-40, 40), range(-15,15)
	firing_grid = np.array(list(itertools.product(x_rng, y_rng)))

	for x, y in firing_grid:
		height, hit_bool = fire_the_cannons(x , y)

		if hit_bool:
			# print(f"Hit with {x}, {y}")
			# print(f"Max height: {height}")
			battleships.append((x,y))

		continue

	if len(battleships) > 0:
		battle_sets = set(battleships)
		return len(battle_sets)

print(f"Solution for Part B: {run_part_B()}")
