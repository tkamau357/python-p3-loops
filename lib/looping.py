#!/usr/bin/env python3

def happy_new_year():
    countdown = 10
    while countdown >= 1:
        print(countdown)
        countdown -= 1
    print("Happy New Year!")

# Calling the function
happy_new_year()


def square_integers(numbers):
    squared_numbers = []
    for num in numbers:
        squared_numbers.append(num ** 2)
    return squared_numbers

numbers = [1, 2, 3, 4, 5]
squared_numbers = square_integers(numbers)
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


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

fizzbuzz()
