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
	winner = ''
	wins = ((0, 1, 2),
			(3, 4, 5),
			(6, 7, 8), 
			(0, 4, 8),
			(2, 4, 6),
			(0, 3, 6),
			(1, 4, 7),
			(2, 5, 8))
	for row in wins:
		if board[row[0]] == board[row[1]] == board[row[2]]:
			winner = board[row[0]]
			return winner
	if len(set(range(9)).intersection(board)) == 0:
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
	nice_moves = (4, 0, 2, 6, 8, 1, 3, 5, 7)
	#see if any move will result in a win
	for move in legal_moves(board):
		board[move] = computer
		if is_winner(board) == computer:
			print 'Computer takes {}!'.format(str(move))
			return move
		#return the board back if doesnt result in a win
		board[move] = move

	#else see if any move will result in opponent winning
	for move in legal_moves(board):
		board[move] = player
		if is_winner(board) == player:
			print 'Computer takes {}!'.format(str(move))
			return move
		board[move] = move
	#If not then make move based on best posible moves available
	for move in nice_moves:
		if move in legal_moves(board):
			print 'Computer takes {}!'.format(str(move))
			return move
		
	return move

	



'''
board, go_first, player, computer = start_game()
display_board(board)
print is_winner(board)
'''
def main():
	board, player, computer = start_game()
	turn = "X"

	while is_winner(board) == 0:
		if turn == "X":
			if player == "X":
				move = human_move(board)
				board[move] = player
			else:
				move = computer_move(board, computer, player)
				board[move] = computer
			turn = "O"
		else:
			if player == "O":
				move = human_move(board)
				board[move] = player
			else:
				move = computer_move(board, computer, player)
				board[move] = computer
			turn = "X"
	winner = is_winner(board)
	print winner
	if winner == computer:
		print "The computer won"
	elif winner == player:
		print "You won!!"
	elif winner == 'TIE':
		print 'Dang, looks like a Tie..'
main()

