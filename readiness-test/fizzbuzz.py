def fizzbuzz(intList):
	fizzbuzz = []
	for l in intList:
		value = ''
		if l%3 == 0:
			value += "Fizz"
		if l%5 == 0:
			value += "Buzz"
		if l%3 != 0 and l%5 != 0:
			value = l
		fizzbuzz.append(value)
	return fizzbuzz