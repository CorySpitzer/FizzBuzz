<?php
#
# fizzbuzz.php
#
# With a command line php installed, 
# this can be run with
#
#   $ php fizzbuzz.php
#
# Jim Mahoney | Marlboro College
# Jan 2012    | opensource.org/licenses/MIT
#
for ($i=1; $i<=100; $i++){
  if ($i % 3 == 0 and $i % 5 == 0){
    printf("FizzBuzz" . PHP_EOL);
  }
  else if ($i % 3 == 0){
    printf("Fizz" . PHP_EOL);
  }
  else if ($i % 5 == 5){
    printf("Buzz" . PHP_EOL);
  }
  else {
    printf("%d" . PHP_EOL,$i);
  }
}
?>

