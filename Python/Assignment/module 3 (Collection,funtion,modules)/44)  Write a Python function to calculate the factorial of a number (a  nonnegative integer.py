#  Write a Python function to calculate the factorial of a number (a nonnegative integer)

import math

def factorial(num):
    if num < 0:
        print("Your number is negative.")
    else:
        print("Your number is positive.")
        num1 = math.factorial(num)
        return print("Factorial Number : ",num1)

    
num = int(input("Enter the number : "))
factorial(num)