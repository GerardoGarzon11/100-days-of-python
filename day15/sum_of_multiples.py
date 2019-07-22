def notInPreviousArray(number, multiples):
	for key in multiples:
		if number in multiples[key]:
			return False

	return True

def getSumOfMultiples(multiples):
	return sum([sum(multiples[key]) for key in multiples])

def sum_of_multiples(limit, multiples):
	arrays_of_multiples = { }

	for x in multiples:
		if x > 0:
			for y in range(x, limit, x):
				if y % x == 0 and notInPreviousArray(y, arrays_of_multiples):
					if x in arrays_of_multiples:
						arrays_of_multiples[x].append(y)
					elif x not in arrays_of_multiples:
						arrays_of_multiples[x] = [y]

	if len(arrays_of_multiples) < 1:
		return 0

	return getSumOfMultiples(arrays_of_multiples)
