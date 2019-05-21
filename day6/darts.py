from math import pow, sqrt

def score(x, y):
	distance_to_center = sqrt(pow(x,2) + pow(y,2))

	if distance_to_center > 10:
		return 0
	elif distance_to_center > 5:
		return 1
	elif distance_to_center > 1:
		return 5
	else:
		return 10
