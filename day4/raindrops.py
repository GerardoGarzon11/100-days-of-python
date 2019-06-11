FACTORS = [(3, 'Pling'), (5, 'Plang'), (7, 'Plong')]

def raindrops(number):

    response = [x[1] for x in FACTORS if number % x[0] == 0]

    if len(response):
    	return ''.join(response)

    return str(number)
