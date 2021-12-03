import numpy as np

#Problem 1
#Inputs
# Forward x
# down x
# up X
# Depth - Down is positive, up is negative

#Given a planned course (data.txt) find out the current location of the sub
#Must return horzontal position and vertical position 

class Navigate(object):
	def __init__(self, data:np.array):
		self.data = data
		self.direct, self.mag = self.split_data(data)
		self.forward = 0
		self.ud = 0


	def split_data(self, data:np.array)->[list, list]:
		direct = [x.split(' ')[0] for x in data]
		mag = [int(x.split(' ')[1]) for x in data]
		return direct, mag

	def move(self)->[int, int]:
		for i in range(len(self.direct)):
			if self.direct[i] == 'forward':
				self.forward += self.mag[i]
			elif self.direct[i] == 'up':
				self.ud -= self.mag[i]
			elif self.direct[i] == 'down':
				self.ud += self.mag[i]
		return self.forward, self.ud

# ./day2/
data = np.genfromtxt('data.txt', delimiter=',', dtype=None, encoding="utf-8")
position = Navigate(data)
horizontal, vertical = position.move()
print(f'Horizontal position: \t {horizontal}')
print(f'Depth position: \t {vertical}')
print(f'Solution to part 1: \t {horizontal * vertical}')

#Problem 2

#Now we need to track another vector with slightly different rules. 
#Down x increases the aim by X units
#Up X decreases the aim by X units
#Forward X
	#Increases your horizontal position by X units
	#Increases your depth by your aim multiplied by X

class Navigate_aim(object):
	def __init__(self, data:np.array):
		self.data = data
		self.direct, self.mag = self.split_data(data)
		self.ud = 0
		self.aim = 0
		self.forward = 0

	def split_data(self, data:np.array)->[list, list]:
		direct = [x.split(' ')[0] for x in data]
		mag = [int(x.split(' ')[1]) for x in data]
		return direct, mag

	def move(self)->[int, int]:
		for i in range(len(self.direct)):
			if self.direct[i] == 'up':
				self.aim -= self.mag[i]
			elif self.direct[i] == 'down':
				self.aim += self.mag[i]
			elif self.direct[i] == 'forward':
				self.forward += self.mag[i]
				self.ud += self.aim * self.mag[i]
		return self.forward, self.ud

# ./day2/
data = np.genfromtxt('data.txt', delimiter=',', dtype=None, encoding="utf-8")
position = Navigate_aim(data)
horizontal, vertical = position.move()
print(f'Horizontal position: \t {horizontal}')
print(f'Depth position: \t {vertical}')
print(f'Solution to part 2: \t {horizontal * vertical}')