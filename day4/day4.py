#Part 1

#Looks like we're going to be playing some bingo today. 
#Goals of which are:

#Inputs are a long string of random numbers and a bunch of 5x5 bingo boards. 
#Our job is to find the winning first winning board by locating any combination
#of the random number string in either of rows or columns.  My guess is the diagonals 
#will be the next part. 

import numpy as np
# ./day4/
def data_load()->[np.array, np.array]:
	data = []
	with open('./day4/data.txt', 'r') as f:
		data = f.read().splitlines()
		markers = np.array([int(s) for s in data[0].split(",")])
		bingo_boards = [[list(map(int, s.split())) for s in line.splitlines()] for line in data[1:]]
		_bingo = [np.array(bingo_boards[i:i+5]).reshape((5,5)) for i in range(1, len(bingo_boards), 6)]
		bingo_boards = np.dstack(_bingo)

	return markers, bingo_boards

def is_col_win(marks:list, board:np.array)->bool:
	for i in range(5):
		if set(marks) >= set(board[:,i]):
			return True
	return False

def is_row_win(marks:list, board:np.array)->bool:
	for i in range(5):
		if set(marks) >= set(board[i,:]):
			return True
	return False

def is_win(marks:list, board:np.array)->bool:
	col_check = is_col_win(marks, board)
	row_check = is_row_win(marks, board)
	if col_check or row_check:
		return True
	else:
		return False

def run_the_things():
	for x in range(1, markers.shape[0]):
		for board in range(0, bingo_boards.shape[2]):
			if is_win(markers[:x], bingo_boards[:,:,board]):
				unmarked_sum = sum(set(bingo_boards[:, :, board].flatten()) - set(markers[:x]))
				return (unmarked_sum * markers[x-1])


markers, bingo_boards = data_load()
SolutionA = run_the_things()
print(f"Solution for Part 1: {SolutionA}")

# Part B

#Now we want to let the giant squid win, because well he's a giant squid. 
#So we need to find the last board that could produce a win. 
#Once we find that last board, multiply it by the sum of the 
#remaining unmarked numbers in its array.


def run_the_other_things(markers:np.array, bingo_boards:np.array):
	win_set = set()
	board_set = set(range(0, bingo_boards.shape[2]))

	#Runs through each marker
	for x in range(1, markers.shape[0]):
		# For each marker, runs through all 100 boards
		for board in range(0, bingo_boards.shape[2]):
			# If the board is a win, add it to the win set
			if is_win(markers[:x], bingo_boards[:,:,board]):
				win_set.add(board)
				# win_set = win_set | set([board])
				#Look at the difference between the full board_set ID's
				#and the win set ID's
				set_diff = list(board_set - win_set)
				#When all id's exist in the win set, we have the last board. 
				if len(set_diff) == 0:
					unmarked_sum = sum(set(bingo_boards[:, :, board].flatten()) - set(markers[:x]))
					return (unmarked_sum * markers[x-1])
					

run_the_other_things(markers, bingo_boards)
SolutionB = run_the_other_things(markers, bingo_boards)
print(f"Solution for Part 2: {SolutionB}")

