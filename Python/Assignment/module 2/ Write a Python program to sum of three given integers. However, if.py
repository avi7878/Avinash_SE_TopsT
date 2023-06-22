num1 = int(input("Enter the Number1 : "))
num2 = int(input("Enter the Number2 : "))
num3 = int(input("Enter the Number3 : "))

if num1 == num2 or num2 == num3 or num3 == num1 :
   print("0")
else :
   print("Sum of three number :",num1+num2+num3)
