# Write a Python program to count the number of lines in a text file.

nooflines = 0
with open("tops.txt","r") as f:
    for lines in f:
        nooflines += 1
print(nooflines)

