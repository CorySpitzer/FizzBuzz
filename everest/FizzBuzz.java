public class FizzBuzz {

	public static void main(String[] args) {
		
		for (int number = 1; number <= 100; number++ ){
			if (number % 3 == 0 && number % 5 == 0){
				System.out.println("FizzBuzz");
			}
			else if (number % 3 == 0){
				System.out.println("Fizz");
			}
			else if (number % 5 == 0){
				System.out.print("Buzz");
			}
			else {
				System.out.println(number);
			}
		}

	}

}