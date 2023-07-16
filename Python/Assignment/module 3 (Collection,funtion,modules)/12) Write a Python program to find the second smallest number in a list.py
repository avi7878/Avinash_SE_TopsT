#  Write a Python program to find the second smallest number in a list.

l1 = []
add = int(input("Enter the number of elements you add : "))

for i in range(1,add+1):
    num = int(input("Enter the number : "))
    l1.append(num)

l1.sort()
print("Second smallest number of list is : ",l1[1])



