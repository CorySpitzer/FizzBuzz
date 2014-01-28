//
// generic FizzBuzz program in C.
//
// One nod to "good programming style" here is 
// giving variable names to the constants 3, 5, and 100.
//
// This line was added in class.
//
// Jim Mahoney | Marlboro College
// Jan 2012    | opensource.org/licenses/MIT
//
#include <stdio.h>
int main(){
  int i;
  int fizz = 3;  
  int buzz = 5;  
  int nMax = 100;
  for (i=1; i<=nMax; i++){
    if (i % fizz == 0 && i % buzz == 0){
      printf("FizzBuzz\n");
    }
    else if (i % fizz == 0){
      printf("Fizz\n");
    }
    else if (i % buzz == 0){
      printf("Buzz\n");
    }
    else {
      printf("%i\n", i);
    }
  }
  return 0;
}
