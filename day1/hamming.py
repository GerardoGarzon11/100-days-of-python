def distance(strand_a, strand_b):
	len_a = len(strand_a)
	len_b = len(strand_b)

	if(len_a == 0 and len_b == 0):
		return 0
	elif(len_a == 0 or len_b == 0 or (len_a != len_b)):
		raise ValueError("Value Error")

	return len([1 for x in zip(strand_a, strand_b) if x[0] != x[1]])