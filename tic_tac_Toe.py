#Creates a tic tac toe game that the user can play with the computer.


# pseudocode for the game...

#Greet the user and announce the rules
#Create a game board
#determine who goes first
#while neither player has won and no tie
	#if players turn
		#display the board
		#get the players mover
	#else (computers turn)
		#calculate the computers move (using the current board)
		#update the board
	#change turns

#declare the outcome (tie, comp wins, player wins)

#Let's get some global variables in there

BLANK = " "



#Greet the user


def create_board():
	board = []
	for spot in range(9):
		board.append(spot)
	return board

def display_board(board):
	return '''\t{} | {} | {}
\t---------
\t{} | {} | {}
\t---------
\t{} | {} | {}'''.format(*board)


def start_game():
	print """Welcome to Tic-tac-toe! 
Get three in a row, secure fame and glory for your house!
The board will appear as such...."""
	board = create_board()
	print display_board(board)

	print """\nSelect your position of choice on the board by selecting 
	the appropriate number\n"""

	player,computer = go_first()

	return board, player, computer
	
def go_first():
	answer = ''
	player = ''
	computer = ''
	while answer not in ('y', 'n'):
		answer = raw_input("Would you like to go first? Answer y or n...\n").lower()
	if answer == 'y':
		player = "X"
		computer = "O"
	else:
		player = "O"
		computer = "X"
	return player, computer

def legal_moves(board):
	legal_moves = []
	for index, spot in enumerate(board):
		if spot not in ['X', 'O']:
			legal_moves.append(index)

	return legal_moves

def is_winner(board):
	wins = ((0, 1, 2),
			(3, 4, 5),
			(6, 7, 8), 
			(0, 4, 8),
			(2, 4, 6),
			(0, 3, 6),
			(1, 4, 7),
			(2, 5, 8))
	for row in wins:
		winner = ''
#		print str(type(board[row[0]])) + str(type(board[row[1]])) + str(type(board[row[2]]))
		if str(board[row[0]]) == str(board[row[0]]) == str(board[row[0]]):
			winner == board[row[0]]
			return winner
	if not set(range(9)).intersection(board):
		return "TIE"

	return 0

def human_move(board):
	print 'Your turn, HUMAN!'
	print display_board(board)
	answer = ''
	while answer not in legal_moves(board):
		answer = int(raw_input('Please select a valid move from the board..'))
	
	return answer

def computer_move(board, computer, player):
	if 4 in legal_moves(board):
		move = 4
		
	return move

	



'''
board, go_first, player, computer = start_game()
display_board(board)
print is_winner(board)
'''

board, player, computer = start_game()
turn = "X"

while not is_winner(board):
	if turn == "X":
		if player == "X":
			move = human_move(board)
			board[move] = player
		else:
			move = computer_move(board, computer)
		turn = "O"
	else:
		if player == "O":
			move = human_move(board)
			board[move] = player
		else:
			move = computer_move(board, computer, player)
			board[move] = computer
		turn = "X"
	print display_board(board)


