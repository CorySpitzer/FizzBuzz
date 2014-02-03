#Here is FizzBuzz programmed through a recursive, functional programming paradigm. 
def isDivisibleBy5():
	#Tests whether a number is evenly divisible by 3.
	if (n % 3 == 0):
		return True
	else:
		return False

def isDivisibleBy5(n):
	#Tests whether a number is evenly divisible by 5.
	if (n % 5 == 0):
		return True
	else:
		return False

def fizzBuzz(n):
	"""Utilizes both isDivisibleBy3() and isDivisibleBy5() to print out all of the integers from 1 to 100
	 according to the FizzBuzz rules."""
	if (isDivisibleBy3(n) and isDivisibleBy5(n)): 
		print "FizzBuzz"
	elif (isDivisibleBy3(n)): 
		print "Fizz"
	elif (isDivisibleBy5(n)): 
		print "Buzz"
	else: print n
	
	#Loops the process 100 times through recursion.
	if (n < 100): 
		fizzBuzz(n+1)
	
	pass

#Calls fizzBuzz().
fizzBuzz(1)