factors = {
    3: 'Pling',
    5: 'Plang',
    7: 'Plong'
}

def raindrops(number):

    response = [factors[x] for x in factors if number % x == 0]

    if len(response):
    	return ''.join(response)

    return str(number)
