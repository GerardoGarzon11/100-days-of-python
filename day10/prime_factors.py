def factors(value):
    if value < 2:
    	return []

    factors = []
    divisor = 2

    while value != 1:
    	if value % divisor == 0:
    		factors.append(divisor)
    		value /= divisor
    	else:
    		divisor += 1

    return factors