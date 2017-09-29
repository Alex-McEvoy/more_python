##########################################################################
#Author: Alex McEvoy
#Date: 09/25/17
#Description: This project takes in a paragraph with numbered blanks and
#				a list of correct answers. It then prompts the user to 
#				take the quiz, giving them 5 tries for each question. 
##########################################################################

#The possible options for input, not necessarily harder or easier

easy = '''___1___ is the command line command to access the tutorial for VIM, a ___2___ editor. 
The text editor can be exited by using the command ___3___. This, however, does not save the changes
may have made to the document. If you would like to exit and save the document, type in ___4___. 
While in VIM, you start in normal mode. This means you can navigate the document and delete characters.
to delete a character, hover over it with the cursor, and hit ___5___. '''

easy_answers = ['vimtutor', 'text', ':q!', ':wq', 'x']

medium = '''A ___1___ is any piece of data written directly into a programs code. This could include
a string or an integer, any piece of information that is not input by a user. In C++, the phrase,
cout << "Hello World";
the operator << is referred to as the stream ___2___ operator. C++ is known as a ___3___ level programming
language, which means it is closer to human speech than machine code. To use the cin or cout commands in C++,
the preprocessor directive #include ___4___ must be included. '''

medium_answers = ['literal', 'insertion', 'high', '<iostream>']

hard = '''Rick's favorite ride in anatomy park was Pirates of the ___1___. Morty's dog in season 1 was originally 
named snuffles, but later preferred to be called ___2___. Later, in the inception episode, Rick and Morty eventually 
employ the help of scary ___3___ to incept Morty's math teacher into giving him an A. The helpful blue creatures named 
Mr. Meseeks eventually confide that existence is ___4___ to them. '''

hard_answers = ['pancreas', 'snowball', 'Terry', 'pain']

#Inputs
	#The player will enter one to many strings corresponding to a list of correct answers
#outputs
	#The rules of the game
	#the paragraph with numbered blanks
	#Whether or not the previous answer was correct
	#The number of tries left
	#the paragraph with already guessed blanks filled in
	#congratulations or try again message

#Determine difficulty of game
def difficulty():
	#Determines which paragraph and answer set to use, based on user input
	user_choices = {
					'easy' : [easy, easy_answers],
					'medium' : [medium, medium_answers],
					'hard' : [hard, hard_answers]
					}

	user_selection = ''
	while user_selection not in user_choices:
		print "Please select a game difficulty by typing it in!!" 
		user_selection = raw_input("Possible choices include easy, medium and hard.\n").lower()
		if user_selection not in user_choices:
			print "That's not an option!!"
	print "You've chosen " + user_selection + '!'
	return user_choices[user_selection]

	

def any_tries_left(tries_left):
	if tries_left == 0:
		print "You've failed too many straight guesses!  Game over!"
		return False
	elif tries_left in range(2,5):
		print "That isn't the correct answer, Let's try again; you have {} trys left".format(tries_left)
	elif tries_left == 1:
		print "That isn't the correct answer! You only have 1 try left!  Make it count!"

	return True

def game_over(player_answers, tries_left, correct_answers):
	#Here a return value of True means that it's time to end the game, False means continue
	#use any_tries_left to see if we're out of tries
	if any_tries_left(tries_left):
		#Check to see if all answers are accounted for
		if player_answers == correct_answers:
			print "You won!"
			return True
	else:
		return True

def word_in_key_words(word, key_words):
	#Searches for our word within a list of keywords to see if we should convert it.
	for item in key_words:
		if item in word:
			return item

	return None

def print_paragraph(paragraph, player_answers):
	#prints our paragraph with the already correctly guessed words filled in
	key_words = ['___1___', '___2___', '___3___', '___4___', '___5___']
	#Only convert the key words the player has already successfully guessed
	key_words = key_words[:len(player_answers)]
	replaced = []
	split_paragraph = paragraph.split()
	print 'The current paragraph reads as such\n'
	for word in split_paragraph:
		new_word = word_in_key_words(word, key_words)
		if new_word:
			#Append to our list replaced[] the player answer corresponding to the index of the number, such as __1__, in key_words
			replaced.append(word.replace(new_word, player_answers[key_words.index(new_word)]))
		else:
			replaced.append(word)

	return ' '.join(replaced)


def ask_question(correct_answers, player_answers):
	#Asks our player to fill in the appropriate blank, based on how many answers have already been correctly guessed
	user_answer = ''
	answer_selector = ['___1___', '___2___', '___3___', '___4___', '___5___']

	user_answer = raw_input("What should be substituted in for {}?  ".format(answer_selector[len(player_answers)])).lower()

	if user_answer.lower() == correct_answers[len(player_answers)].lower():
		user_answer = correct_answers[len(player_answers)]
		print "Correct!"
		return user_answer
	else:
		return None



def play_game(paragraph, correct_answers):
	#print out the rules to the player
	print "You will get 5 guesses per problem"
	player_answers = []
	tries_left = 5
	#while the player has not correctly entered all of the answers or used all their tries
	while not game_over(player_answers, tries_left, correct_answers):
		#print out the paragraph with the correct answers
		print print_paragraph(paragraph, player_answers)
		#prompt the user for the next answer
		answer = ask_question(correct_answers, player_answers)
		if answer:
			player_answers.append(answer)
			tries_left = 5
		else:
			#Reduce the number of tries
			tries_left -= 1
					


user_difficulty = difficulty()

#Use argument unpacking to pass in 2 arguments to play_game()
play_game(*user_difficulty)



#x = ['world', 'Python', 'print', 'HTML']
#y = ['world', 'Python', 'print', 'HTML']
#print game_over(x, 0, y)



	