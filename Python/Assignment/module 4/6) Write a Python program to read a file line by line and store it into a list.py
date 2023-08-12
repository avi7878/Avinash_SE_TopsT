# Write a Python program to read a file line by line and store it into a list

list = []

file = open("tops.txt","r")
list1 = file.read()

list.append(list1)
print(list)

file.close()
