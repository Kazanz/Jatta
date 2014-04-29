import re
	
def Check_Word_is_Valid(word, word_length_for_game = 5):
	"""Returns True is word is only letters and the length of arg 2."""
	if re.search(r'[0-9]',word) or len(word) != word_length_for_game:
		print "Word must be %d letters long and letters only." % word_length_for_game
		return 0
	else:
		return 1
		
		
def Make_Lists_from_Guess(guess, word_to_guess):
	"""Returns two lists of the letters in the 2 args"""
	guess_list = []
	target_list = []
	for letter in guess:
		guess_list.append(letter)
	for letter2 in word_to_guess:
		target_list.append(letter2)
	return guess_list,target_list
	
	
def Find_Matched_Letters(guess_list, target_list):
	"""Returns the # of matched letters"""
	temp_target = []
	temp_target.extend(target_list)
	matches = 0
	for letter in guess_list:
		if letter in temp_target:
			matches += 1
			temp_target.remove(letter)
	return matches
	

def Check_Win(guess, target):
	"""Returns Victory Message if the correct word is guessed.  Returns True if
	   Player wants to play again.  False if not.  Passes if not a Win"""
	if guess == target:
		print "YOU WIN!"
		print "Would you like to play again? (yes/no)"
		answer = raw_input().lower()
		if answer == 'yes':
			Main_Game()
		elif answer == 'no':
			exit()
		else:
			print "Please type 'yes' or 'no'."
			answer = raw_input().lower()
	else:
		pass
		
		
def Display_all_Guesses(current_guess, current_match_number, guess_list):
	"""Prints all previous guesses and matches after appending the current guess
	   and match to the dictionary"""
	print '_' * 20
	print 'Your Guesses:'
	gList = guess_list
	gList.append((current_guess,current_match_number))
	for k,v in gList:
		print k,v
	return gList


def Get_Entry_until_Valid():
	"""Keeps looping until the word entered satisfies the Check_Word_is_Valid function"""
	Target_Word = raw_input().lower()
	while not Check_Word_is_Valid(Target_Word):
		"Please try another word:"
		Target_Word  = raw_input().lower()
	return Target_Word


def Main_Game():
	"""This is the main Gameplay Function for Jatta"""
	print "WELCOME TO JATTA"
	print "Please enter the word to guess:"
	Target = Get_Entry_until_Valid()
	guesses = []

	while True:
		print "Input Your Guess:"
		Guess = Get_Entry_until_Valid()

		g_list,t_list = Make_Lists_from_Guess(Guess,Target)
		count = Find_Matched_Letters(g_list,t_list)

		Display_all_Guesses(Guess,count,guesses)

		Check_Win(Guess,Target)

### Executed Code ###
Main_Game()
	
	
	
	
