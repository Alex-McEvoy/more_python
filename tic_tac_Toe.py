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
	print '''\t\t\t   {} | {} | {}
			   ---------
			   {} | {} | {}
			   ---------
			   {} | {} | {}'''.format(board[0], board[1], board[2], 
			   				   board[3], board[4], board[5], 
			   				   board[6], board[7], board[8])
def start_game():
	print """Welcome to Tic-tac-toe! 
			Get three in a row, secure fame and glory for your house!
			The board will appear as such...."""
	board = create_board()
	display_board(board)

	print """\nSelect your position of choice on the board by selecting 
	the appropriate number\n"""

	go_first()

	return board, answer 
	
def go_first():
	answer = ''
	while answer not in ['y', 'n']:
		answer = input("Would you like to go first? Answer y or n...\n").lower()

	return answer

def legal_moves(board):
	legal_moves = []
	for index, spot in enumerate(board):
		if spot not in ['X', 'O']:
			legal_moves.append(index)

	return legal_moves

def 



board, go_first = start_game()

