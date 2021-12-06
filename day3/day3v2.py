#Part 1
#.\day3\
import numpy as np
def load_data()->np.array:
	with open('.\day3\data.txt', mode='r') as f:
		data = f.read().splitlines()
	return np.array([list(map(int, (s))) for s in data])

def power_consumption()->int:
	data = load_data()
	gamma, epsilon, ones, zeros = [], [], [], []

	for x in range(0, data.shape[1]):
		counts = np.unique(data[:,x], return_counts=True)
		zeros.append(counts[1][0])
		ones.append(counts[1][1])
		if ones[x] > zeros[x]:
			gamma.append(1)
			epsilon.append(0)
		else:
			gamma.append(0)
			epsilon.append(1)

	gamma_int = int(''.join(map(str, gamma)), 2)
	epsilon_int = int(''.join(map(str, epsilon)), 2)
	return gamma_int * epsilon_int
power_cons_rating = power_consumption()
print(f'Solution to part 1 (Power Consumption rating): \t {power_cons_rating}')


#Part 2 
def most_common(data:np.array, x:int)->[int, int]:
	mx = np.bincount(data[:,x])
	if mx.size > 1:
		if mx[0] == mx[1]:
			return 1, mx.argmax()
		else:
			return mx.argmax(), mx.max()
	else:
		return mx.argmax(), mx.max()

def least_common(data:np.array, x:int)->[int, int]:
	mx = np.bincount(data[:,x])
	if mx.size > 1:
		if mx[0] == mx[1]:
			return 0, mx.argmin()
		else:
			return mx.argmin(), mx.min()
	else:
		return mx.argmin(), mx.min()

def filter_array(data:np.array, mc_num:int, x:int)->np.array:
	return data[np.where(data[:, x] == mc_num)]

def oxy_co2_rating()->int:
	data = load_data()
	x = 0
	#Oxy rating
	filt_data = data.copy()
	while x < data.shape[1] and filt_data.shape[0] > 1:
		mc_num, mc = most_common(filt_data, x)	
		filt_data = filter_array(filt_data, mc_num, x)
		x += 1
	
	oxy_int = "".join([str(x) for x in filt_data[0]])
	oxy_int = int(''.join(oxy_int), 2)
	x = 0
	#co2 rating
	filt_data = data.copy()
	while x < data.shape[1] and filt_data.shape[0] > 1:
		mc_num, mc = least_common(filt_data, x)	
		filt_data = filter_array(filt_data, mc_num, x)
		x += 1
	
	co2_int = "".join([str(x) for x in filt_data[0]])
	co2_int = int(''.join(co2_int), 2)

	return oxy_int * co2_int

life_support_rating = oxy_co2_rating()
print(f'Solution to part 2 (Life support rating): \t {life_support_rating}')

