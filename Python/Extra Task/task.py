# task : accept 5 numbers from user and check even and odd numbers

for i in range(1,6): # loop will excute 1 to 5
    num = int(input("Enter the number : "))# taking one varibale and accept the value form user
    if num %2 == 0 :# check number is even then print
        print("Your number is Even.")
    else: # number is odd then print.
        print("Your number is Odd.")