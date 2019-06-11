from random import randrange

def modifier(value):
	return (value - 10) // 2

def setStat():
	dice_throws = [randrange(1,7,1) for x in range(0,4)]
	dice_throws.remove(min(dice_throws))
	return sum(dice_throws)

class Character:

	def ability(self):
		abilities = [
			self.strength,
			self.dexterity,
			self.constitution,
			self.intelligence,
			self.wisdom,
			self.charisma
		]

		return abilities[randrange(1,7,1)]

	def __init__(self):
		self.strength = setStat()
		self.dexterity = setStat()
		self.constitution = setStat()
		self.intelligence = setStat()
		self.wisdom = setStat()
		self.charisma = setStat()
		self.hitpoints = 10 + modifier(self.constitution)
