#  Write a python program to sum of the first n positive integers. 

n = int(input("Enter your number : "))
sum = 0

if n > 0:
    for i in range(1,n+1):
        sum += i
    print("sum of first to",n,"number is",sum)
else:
    print("Your number is nagetive.")
    

