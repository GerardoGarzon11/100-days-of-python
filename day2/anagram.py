def find_anagrams(word, candidates):
	lower_word = word.lower()
	sorted_lower_word = ''.join(sorted(lower_word))

	return [
		candidate 
		for candidate in candidates 
		if ''.join(sorted(candidate.lower())) == sorted_lower_word 
		and lower_word != candidate.lower()
		]
