#! python3

import random

dice_array = []
ascii_representations = (
		"*       *\n*   +   *\n*       *", #3
		"* +     *\n*       *\n*     + *", #2
		"* +     *\n*   +   *\n*     + *", #3
		"* +   + *\n*       *\n* +   + *", #4
		"* +   + *\n*   +   *\n* +   + *", #5
		"* +   + *\n* +   + *\n* +   + *" #6
	)

def gen_dice_array(number_of_dice):
	for x in range(0, number_of_dice):
		dice_array.append(random.randrange(1, 6))

def print_dice(output_format):
	if output_format == 1:
		print(dice_array)
	else:
		# print in text format
		for x in dice_array:
			print("*********")
			print(ascii_representations[x-1])
			print("*********")

print("Dice Roll Simulator")

print("Please select number of dice:")
number_of_dice = int(input("> "))

print("Please select the format of the output.\n1 - Just the numbers\n2 - ASCII Dice")
output_format = int(input("> "))

gen_dice_array(number_of_dice)
print_dice(output_format)
