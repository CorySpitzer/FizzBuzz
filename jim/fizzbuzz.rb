#
# ruby stream processing approach to FizzBuzz problem.
#
puts (1..100) \
  .map {|x| [x,'']} \
  .map {|pair| pair[0] % 3 == 0 ? [pair[0], 'Fizz'] : pair} \
  .map {|pair| pair[0] % 5 == 0 ? [pair[0], pair[1] + 'Buzz'] : pair} \
  .map {|pair| pair[1] == '' ? pair[0] : pair[1]} \
  .join("\n")
