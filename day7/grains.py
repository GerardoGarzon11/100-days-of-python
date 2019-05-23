def valid(integer_number):
	if integer_number < 1 or integer_number > 64:
		return False

	return True

def on_square(integer_number):
	if not valid(integer_number):
		raise ValueError("Invalid input")

	return 2**(integer_number - 1)


def total_after(integer_number):
	if not valid(integer_number):
		raise ValueError("Invalid input")

	return sum([2**(x-1) for x in range(1, integer_number + 1)])