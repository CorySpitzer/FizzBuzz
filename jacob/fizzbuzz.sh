#!/bin/bash

function FizzBuzz {
	# Returns the FizzBuzz value of a given number
	# Ex. FizzBuzz 5 == 'Fizz'
	# FizzBuzz 4 == 4
	if [ $[$1 % 15] == 0 ]; then
		echo 'FizzBuzz'
	elif [ $[$1 % 3] == 0 ]; then
		echo 'Fizz'
	elif [ $[$1 % 5] == 0 ]; then
		echo 'Buzz'
	else
		echo $1
	fi
}

function main {
	# Loops through a number range and echos the FizzBuzz value of each number
	for (( i = $1; i <= $2; i++ )); do
		echo $(FizzBuzz $i)
	done
}

# Checks that the program was called with 2 arguments
if [ $# == 2 ]; then
	main $1 $2
else
	echo "Usage: ./fizzbuzz.sh min max"
fi