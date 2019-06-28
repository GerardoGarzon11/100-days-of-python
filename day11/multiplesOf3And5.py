def getSumOfMultiples(number, divisor):
  """
  Returns sum of multiples of divisor below number
  Example:
  number = 20, divisor = 3
  result = 63
  
  Sum of multiples is 3+6+9+12+15+18
  """
  
	largestMultiple = (number // divisor) * divisor if number % divisor != 0 else number - divisor
	sumOfMultiples = ((largestMultiple + divisor) * 10 // 2) * ((number - 1) // divisor) // 10
	return sumOfMultiples

number = int(input())

# Code was used specifically for a Project Euler problem, so this stays like this
print(getSumOfMultiples(number, 3) + getSumOfMultiples(number, 5) - getSumOfMultiples(number, 15))
