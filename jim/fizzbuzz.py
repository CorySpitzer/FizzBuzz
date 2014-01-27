"""
 fizzbuzz.py    (Python 2.7.5)
 
  FizzBuzz assignment for the Programming Workshop

    Write a program that prints the numbers from 1 to 100. 
    But for multiples of three print 'Fizz' instead of the number 
    and for the multiples of five print 'Buzz'. For numbers 
    which are multiples of both three and five print 'FizzBuzz'.

  This one is a python solution with all the trimmings:
  functions, docstrings, tests, keywords, generality: the works.
  Massive overkill for this problem, clearly, but it does illustrate
  the style I emphasize in the Intro Programming class.

  And here are some python trivia questions for the code below:
    * Why use xrange() rather than range() ?
    * Why is there a comma at the end of 'print fizzbuzz(),' ?

  And a few more questions to consider:
    * Would output like "1 2 Fizz 4 Buzz Fizz 7 8 Fizz ..." also be correct?
    * If no, what in the specification says there should be one per line?
    * If so, is the specifification too vague?
    * Which versions of Python will run this code correctly?
      And does Python have a standard way of dealing with version issues?
  
 Jim Mahoney | cs.marlboro.edu | Jan 2014 | opensource.org/licenses/MIT
"""

def divides(a, b):
    """ Return True if a goes into b.
        >>> divides(3, 6)             # Tests!
        True
        >> divides(3, 7)
        False
    """
    return b % a == 0

def fizzbuzz(numberToWord={3:'Fizz', 5:'Buzz'}, nMax=100):
    """ Return fizzbuzz lines as described above, for the general case. """
    result = ''
    for n in xrange(1, nMax+1):
        word = ''
        for number in sorted(numberToWord.keys()):
            if divides(number, n):
                word += numberToWord[number]
        result += (word or str(n)) + "\n"
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print fizzbuzz(),
