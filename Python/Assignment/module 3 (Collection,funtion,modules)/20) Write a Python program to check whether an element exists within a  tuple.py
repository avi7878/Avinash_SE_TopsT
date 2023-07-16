#  Write a Python program to check whether an element exists within a tuple.

tuple1 = (1,2,3,4,5,6,7,8,9,10)

element = int(input("Enter number of 1 to 10 and check element in tuple : "))

if element in tuple1 :
    print(f"The element {element} exists in the tuple.")
else:
    print(f"\nThe element {element} does not exist in the tuple.")