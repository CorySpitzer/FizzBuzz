# generic FizzBuzz | Jim Mahoney | cs.marlboro.edu
for i in range(101):
    if i % 5 == i % 3 == 0:
        print 'FizzBuzz'
    elif i % 5 == 0:
        print 'Buzz'
    elif i % 3 == 0:
        print 'Fizz'
    else:
        print i

