import random
import sys

def main():
	print("Press enter to roll again")
	while True:
		roll = getRoll(4, -1, 1)
		total = sum(roll)
		sys.stdout.write("sum: " + str(total) + " ")
		sys.stdout.write(rollToStr(roll))
		
		#wait for user to press enter
		try:	#python 2 and 3 compat
			raw_input("")
		except NameError:
			input("")
			
def getRoll(n, lower, upper):
	"""
		Returns a list of length n with values from lower to upper (inclusive)
	"""
	result = []
	for i in range(n):
		result.append(random.randint(lower,upper))
	return result
	
def rollToStr(roll):
	"""
		Returns a str representation of a roll
	"""
	result = "("
	for d in roll:
		if d == -1:
			result += "-"
		elif d == 1:
			result += "+"
		else:
			result += str(d)
	result += ")"
	return result

main()