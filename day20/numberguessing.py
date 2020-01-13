# TODO: Clear screen after game
# TODO: Save winning % for each difficulty

#! python3
#  numberguessing.py

import random

# Each element in the tuple contains
# (number of guesses, max number, difficulty string)
GAME_CONFIG = ((5, 10, "easy"), (4, 15, "medium"), (3, 20, "hard"),
 (2, 25, "basically impossible"))

def play_game(difficulty):
	moves = GAME_CONFIG[difficulty - 1][0]
	max_num = GAME_CONFIG[difficulty - 1][1]
	difficulty_str = GAME_CONFIG[difficulty - 1][2]

	# generate random number
	answer = random.randrange(1, max_num)

	print(f"Starting {difficulty_str} game")

	moves_made = 0
	found = False
	while moves_made < moves and not found:
		print("Make your guess!:")
		guess = int(input())

		if guess < answer:
			print("Your guess is smaller than the answer.")
		elif guess > answer:
			print("Your guess is larger than the answer.")
		else:
			print("You've guessed it!")
			found = True
		
		moves_made = moves_made + 1

	if found:
		print("Well done!")
	else:
		print("Better luck next time!")

def print_game_menu():
	print("*********************************")
	print("* MENU                          *")
	print("* 1 - EASY (5 moves, 1-10)      *")
	print("* 2 - MEDIUM (4 moves, 1-15)    *")
	print("* 3 - HARD (3 moves, 1-20)      *")
	print("* 4 - BASICALLY IMPOSSIBLE (25) *")
	print("* 0 - EXIT                      *")
	print("*********************************")	

print("Welcome to the Number Guessing Game")
print_game_menu()
print("Please choose an option:")
choice = int(input())

while choice != 0:
	if choice > 0:
		play_game(choice)
	print_game_menu()
	print("Please choose an option:")
	choice = int(input())

print("Thanks for playing!")
