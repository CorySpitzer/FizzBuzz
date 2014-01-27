"""
 fizzbuzz_objects.py    (Python 2.7.5)

 An object oriented approach to the FizzBuzz problem.
 
 Jim Mahoney | cs.marlboro.edu | Jan 2014 | opensource.org/licenses/MIT
"""

class FizzBuzzInt(object):
    """ An integer with a string representation per the FizzBuzz recipe. 
        >>> print FizzBuzzInt(7)
        7
        >>> print FizzBuzzInt(5)
        Buzz
        >>> print FizzBuzzInt(15)
        FizzBuzz
    """
        
    specials = {3: 'Fizz', 5: 'Buzz'}
    
    def __init__(self, value=1):
        self.value = value
        FizzBuzzInt.special_keys = sorted(FizzBuzzInt.specials.keys())

    def __str__(self):
        result = ''
        for i in FizzBuzzInt.special_keys:
            if self.value % i == 0:
                result += FizzBuzzInt.specials[i]
        return result if result else str(self.value)

class FizzBuzzRange(object):
    """ A range of FizzBuzzInts 
        >>> print FizzBuzzRange(11, 17)
        11
        Fizz
        13
        14
        FizzBuzz
        16
    """
    def __init__(self, low=1, high=101):
        self.low = low
        self.high = high
    def __str__(self):
        # Aside : This code puts an extra \n in the output, failing the spec.
        #    result = ''
        #    for i in xrange(self.low, self.high)):
        #      result += str(FizzBuzzInt()) + '\n'
        #    return result
        # The version below doesn't have that problem.
        # (Can you say 'fence post error'?)
        result = []
        for i in xrange(self.low, self.high):
            result.append(str(FizzBuzzInt(i)))
        return '\n'.join(result)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print FizzBuzzRange()
