# Write a Python program to read first n lines of a file

file =open("tops.txt","r")
first_line = file.readlines()
print("First line:", first_line)
file.close()