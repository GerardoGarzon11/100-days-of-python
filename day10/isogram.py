def is_isogram(string):

	string = string.lower()

	for x in string:
		if x.isalpha():
			if string.count(x) > 1:
				return False

	return True
