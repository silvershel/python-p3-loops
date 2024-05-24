#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i >= 1:
        print(i)
        i -= 1
    print("Happy New Year!")
    

def square_integers(int_list):
    squared_list = [int ** 2 for int in int_list]
    return squared_list

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
    

# Write a function happy_new_year() using a while loop that outputs numbers 
# starting at 10 and counting down to 1. After reaching 1, print out "Happy New Year!"

# Write a function square_integers() that takes one argument, a list of integers 
# and returns the list of squared elements.

# Write a function fizzbuzz() that prints the numbers from 1 to 100. For multiples of three, 
# print "Fizz" instead of the number and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five, print "FizzBuzz".
