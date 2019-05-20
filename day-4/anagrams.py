def find_anagrams(word, candidates):
    lower_word = word.lower()
    sorted_lower_word = ''.join(sorted(lower_word))

    anagrams = []

    for candidate in candidates:
    	if(''.join(sorted(candidate.lower())) == sorted_lower_word):
    		if(lower_word != candidate.lower()):
    			anagrams.append(candidate)

    return anagrams
