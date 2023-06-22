# ==> Write python program that swap two number with temp variable and without temp variable. 

a,b,temp = 22,33,0

print("After Swaping.")

print("A :",a)
print("B :",b)

print("Before swaping.")

a,b = b,a

print("A :",a)
print("B :",b)

print("\n-----------------------------")
print("\nUsing Temp variable.")

print("AFter Swaping.")

print("A :",a)
print("B :",b)

print("Before Swaping.")

temp = a
a = b
b = temp

print("A :",a)
print("B :",b)


