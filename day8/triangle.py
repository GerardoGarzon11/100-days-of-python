def has_zeros(sides):
	if 0 in sides:
		return True

	return False

def equilateral(sides):
	if has_zeros(sides):
		return False

	if sides.count(sides[0]) == 3:
		return True
	
	return False


def isosceles(sides):
	if has_zeros(sides):
		return False

	# find equal sides
	if sides.count(sides[0]) == 3:
		return True
	elif sides.count(sides[0]) == 2:
		equal_side = sides[0]
		if sides.count(sides[1]) == 1:
			dif_side = sides[1]
		else:
			dif_side = sides[2]
	elif sides.count(sides[1]) == 2:
		equal_side = sides[1]
		if sides.count(sides[0]) == 1:
			dif_side = sides[0]
		else:
			dif_side = sides[2]
	else:
		return False

	if equal_side * 2 < dif_side:
		return False

	return True

def scalene(sides):
	if has_zeros(sides):
		return False

	if sides.count(sides[0]) == 1 and sides.count(sides[1]) == 1:
		sides = sorted(sides)
		if sides[2] <= sides[0] + sides[1]:
			return True

	return False
