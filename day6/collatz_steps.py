def collatz_steps(number):
	if number < 1:
		raise ValueError("Invalid input")

	steps = 0

	while number != 1:
		if number % 2 == 0:
			number = number / 2
		else:
			number = (number * 3) + 1
		steps += 1

	return steps
