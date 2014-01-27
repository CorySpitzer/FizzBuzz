"""
 fizzbuzz_functional.py    (Python 2.7.5)

  And now a functional approach. 

  This particular example could be considered dataflow style, too,
  in that the data is steadily transformed as it moves through the code.

 Jim Mahoney | cs.marlboro.edu | Jan 2014 | opensource.org/licenses/MIT
"""

print '\n'.join(
    map(lambda (i, s): s if s else str(i),
        map(lambda (i, s): (i, s+'Buzz' if i % 5 == 0 else s),
            map(lambda (i, s): (i, s+'Fizz' if i % 3 == 0 else s),
                map(lambda i: (i, ''),
                    range(1, 101))))))
