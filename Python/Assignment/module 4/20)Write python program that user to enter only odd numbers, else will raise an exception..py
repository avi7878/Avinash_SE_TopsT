# Write python program that user to enter only odd numbers, else will raise an exception.

num1 = int(input("Enter the number : "))

def error():
    print(num1/0)

try : 

    if num1 % 2 != 0:
        print("Odd number")
    else:
        error()

except Exception as e:
    print(e)

          