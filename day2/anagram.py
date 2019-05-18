def find_anagrams(word, candidates):
    word_as_letters = list(word).sort()
    anagrams = []
    for x in candidates:
    	if len(x) == len(word):
    		if(list(x).sort() == word_as_letters):
    			anagrams.append(x)
    return anagrams