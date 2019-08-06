#! 	python3
# 	hangman.py

import random

words = ['abnormal', 'because', 'certain', 'deafening', 'evacuate',
		'first', 'generate', 'hypercard', 'imagination', 'joking',
		'kill', 'limousine', 'main', 'new', 'operation',
		'palindrome', 'question', 'radio', 'stubborn', 'temporary',
		'ubiquitous', 'vengeance', 'willing', 'xenophobic', 'yesterday',
		'zoologist']

class Hangman:

	hangman_top = '  ____\n'
	hangman_states = [
		'  o  |\n     |\n     |',
		'  o  |\n /   |\n     |',
		'  o  |\n /|  |\n     |',
		'  o  |\n /|\\ |\n     |',
		'  o  |\n /|\\ |\n /   |',
		'  o  |\n /|\\ |\n / \\ |'
	]
	hangman_bottom = '\n     |\n_____|\n'

	def __init__(self):
		self.letters = []
		self.moves = 6
		self.word = list(random.choice(words))
		self.guess = [None for character in self.word]
		self.gameOver = False

	def setMove(self, chng):
		self.moves += chng

	def displayGameState(self, correctChoice, moves, guess):
		if not correctChoice:
			self.drawHangman(moves)

		self.displayCurrentGuess(guess)

	def updateGuess(self, letter):
		for i in range(0, len(self.word)):
			if self.word[i] == letter:
				self.guess[i] = letter

	def makeGuess(self, letter):
		if not letter.isalpha():
			return 'That\'s not a valid character!'

		if letter in self.letters:
			return 'You already used that letter'

		if letter not in self.letters:
			self.letters.append(letter)
			if letter not in self.word:

				self.displayGameState(False, self.moves, self.guess)
				self.setMove(-1)

				if self.moves == 0:
					self.gameOver = True
					return 'Game over!'

				return 'Wrong!' # you have x movements remaining
			else:

				self.updateGuess(letter)

				if self.guess == self.word:
					self.gameOver = True
					print(str(self.word))
					return 'You guessed the word!'

				self.displayGameState(True, self.moves, self.guess)
				return 'Good guess!' # return current guess

	def drawHangman(self, moves):
		print(Hangman.hangman_states[6 - moves], Hangman.hangman_bottom)

	def displayCurrentGuess(self, guess):
		displayStr =  'Your guess: '
		for c in guess:
			if c is None:
				displayStr += '_'
			else:
				displayStr += c

		print(displayStr)
