def isPalindrome(number):
	numberList = list(str(number))

	if numberList == numberList[::-1]:
		return True

	return False

def largest(min_factor, max_factor):
	value = None
	factors = []

	if min_factor > max_factor:
		raise ValueError("min_factor must be smaller than max_factor")

	for x in range(min_factor, max_factor + 1):
		for y in range(x, max_factor + 1):
			if isPalindrome(x * y):
				if value is None:
					value = 0
				if value < x * y:
					value = x * y
					factors = [[x, y]]
				elif value == x * y:
					factors.append([x, y])

	return value, factors

def smallest(min_factor, max_factor):
	value = None
	factors = []

	if min_factor > max_factor:
		raise ValueError("min_factor must be smaller than max_factor")

	for x in range(min_factor, max_factor + 1):
		for y in range(x, max_factor + 1):
			if isPalindrome(x * y):
				if value is None:
					value = max_factor * max_factor
				if value > x * y:
					value = x * y
					factors = [[x, y]]
				elif value == x * y:
					factors.append([x, y])

	if value == max_factor * max_factor and not isPalindrome(max_factor * max_factor):
		value = None

	return value, factors
