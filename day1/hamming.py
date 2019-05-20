def distance(strand_a, strand_b):
	len_a = len(strand_a)
	len_b = len(strand_b)

	if(len_a != len_b):
		raise ValueError("Value Error")

	return len([1 for ch1, ch2 in zip(strand_a, strand_b) if ch1 != ch2])