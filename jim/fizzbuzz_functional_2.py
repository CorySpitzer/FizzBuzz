"""
 fizzbuzz_functional_2.py    (Python 2.7.5)

 A second version of a functional approach.

 This one is essentially the same idea 
 as the first functional code, but with named
 rather than anonymous functions.
 
 One addition is a "function generator" (fb_func)
 for the fizzbuzz functions, allowing a more 
 perhaps more general form for the mod arithmetic.
 Be clear that fb_func returns a function, so
 for example fb_func(3, 'Fizz')(9) would be 'Fizz'.

 And one difference is that this time all the functions
 are called in succession on each integer, rather
 than transforming all of the integers. In other words,
 there is only one map() call here, not many as in 
 the first functional program.

 All of these are "pure" functions,
 without sideffects or global state changes.
 Each takes a clearly defined input and produces
 a clearly defined output, with no dependency
 on or modification of a "state" anywhere else.

 A python subtlety that I've used here which you may not
 have seen before is the * in argument lists. This 
 is used to convert a collection of arguments to their
 components before passing into a function. Like this :

   def printem(a,b):       # takes two arguments
       print a, b

   pair = (3,4)
   printem(pair)           # error
   printem(*pair)          # works - same as printem(3,4)

 In this case, each number (i.e. 19) has been turned into
 a tuple (i.e. (19, '')) where the 2nd element carries
 around the string which the number might be turning into.
 This lets us do the 'Fizz' and 'Buzz' checks one at a time,
 without losing the number along the way.

 Since the functions return by fb_func and contract all
 take two arguments, the * are needed to turn for example
 contract((19,'')) into contract(*(19,'')) which is contract(19,'').

 Well, anyway, it works.
   
 I haven't put docstrings on any of these functions. Nor tests.
 
 Can you 

 Jim Mahoney | cs.marlboro.edu | Jan 2014 | opensource.org/licenses/MIT 
"""
 
def expand(number):
    return (number, '')

def contract(number, string):
    if string == '':
        return str(number)
    else:
        return string

def fizzbuzz(i, fb_value, fb_string):
    if i % fb_value == 0:
        return fb_string
    else:
        return ''
    
def fb_func(fb_value, fb_string):
    return lambda i, s: (i, s + fizzbuzz(i, fb_value, fb_string))

def transform(i):
    return contract(*fb_func(5, 'Buzz')(*fb_func(3, 'Fizz')(*expand(i))))

print '\n'.join(map(transform, range(1, 101)))

