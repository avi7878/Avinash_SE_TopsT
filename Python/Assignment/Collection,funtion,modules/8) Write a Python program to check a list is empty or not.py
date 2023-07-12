#  Write a Python program to check a list is empty or not

list1 = []
length = int(input("Enter how many value add in list : "))

for i in range(0,length):
    string_ = input("Enter your string : ")
    list1.append(string_)

if len(list1) == 0:
    print("List is Empty")
else:
    print("List is not Empty")
    
