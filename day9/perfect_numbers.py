def classify(number):
	if number < 1:
		raise ValueError("Number isn't correct")

	step = 2

	if number % 2 == 0:
		step = 1

	factors = [x for x in range(1, number // 2 + 1, step) if number % x == 0]

	if sum(factors) == number:
		return "perfect"
	elif sum(factors) < number:
		return "deficient"
	else:
		return "abundant"
