import random
from django.core.urlresolvers import reverse
from django.shortcuts import HttpResponseRedirect, render


def main(request):
	"""
		default behavior is to roll four dice, as this is the standard amount
	"""
	return rollDice(request, 4)

def rollDice(request, diceAmt):
	"""
		rolls the given number of dice and renders it to the main template
		if given a diceAmt value outside the accepted bounds, just rolls 4 dice
	"""
	diceAmt = int(diceAmt)  #values passed from regex are always string
	if diceAmt < 0 or diceAmt > 255:    #upper bound is arbitrary
		diceAmt = 4
	roll = getRoll(diceAmt, -1, 1)
	total = sum(roll)
	return render(request, 'main.html', {"total":total, "roll":roll, "diceAmt":diceAmt, })

def diceAmtForm(request):
	"""
		allows the desired number of dice to be posted in a form
	"""
	if 'diceAmt' in request.POST:
		diceAmt = request.POST['diceAmt']
		if diceAmt.isdigit():
			return HttpResponseRedirect(reverse('rollDice', args=[ diceAmt ]))

	return HttpResponseRedirect(reverse('main'))

def getRoll(n, lower, upper):
	"""
		Returns a list of length n with values from lower to upper (inclusive)
	"""
	result = []
	for i in range(n):
		result.append(random.randint(lower,upper))
	return result