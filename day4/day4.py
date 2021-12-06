#Part 1

#Looks like we're going to be playing some bingo today. 
#Goals of which are:

#Inputs are a long string of random numbers and a bunch of 5x5 bingo boards. 
#Our job is to find the winning first winning board by locating any combination
#of the random number string in either of rows or columns.  My guess is the diagonals 
#will be the next part. 

import numpy as np

def data_load():
	data = []
	with open('.\day4\data.txt', 'r') as f:
		data = f.read().splitlines()
		markers = np.array([int(s) for s in data[0].split(",")])
		bingo_boards = [[list(map(int, s.split())) for s in line.splitlines()] for line in data[1:]]
		_bingo = [np.array(bingo_boards[i:i+5]).reshape((5,5)) for i in range(1, len(bingo_boards), 6)]
		bingo_boards = np.dstack(_bingo)

	return markers, bingo_boards

def is_col_win(marks, board):
	for i in range(5):
		if set(marks) >= set(board[:,i]):
			return True
	return False

def is_row_win(marks, board):
	for i in range(5):
		if set(marks) >= set(board[i,:]):
			return True
	return False

def is_win(marks, board):
	col_check = is_col_win(marks, board)
	row_check = is_row_win(marks, board)
	if col_check or row_check:
		return True
	else:
		return False


markers, bingo_boards = data_load()

for x in range(1, len(markers)):
	for board in range(0, bingo_boards.shape[2]):
		if is_win(markers[0:x], bingo_boards[:,:,board]):
			unmarked_sum = sum(set(bingo_boards[:, :, board].flatten()) - set(markers[0:x]))
			print(unmarked_sum * markers[x-1])
			exit(0)
