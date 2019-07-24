responses = {
	'question': 'Sure.',
	'yell': 'Whoa, chill out!',
	'yell_question': 'Calm down, I know what I\'m doing!',
	'empty': 'Fine. Be that way!',
	'anything_else': 'Whatever.'
}

def qualifyMessage(message):
	all_caps = True
	has_letters = False
	
	message = message.strip()

	if not len(message):
		return "empty"

	for x in message:
		if x.islower() and x.isalpha():
			all_caps = False
		if x.isalpha():
			has_letters = True 

	question = True if message[len(message) - 1] == '?' else False

	if all_caps and has_letters:
		return "yell_question" if question else "yell"
	elif question and (not all_caps or not has_letters):
		return "question"

	return "anything_else"

def response(hey_bob):
    return responses[qualifyMessage(hey_bob)]
