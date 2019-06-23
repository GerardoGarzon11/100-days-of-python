import string as str

def is_isogram(string):

	if len(string) < 1:
		return True

	string = string.lower()

	for x in string:
		if x in str.ascii_lowercase:
			if string.count(x) > 1:
				return False

	return True
