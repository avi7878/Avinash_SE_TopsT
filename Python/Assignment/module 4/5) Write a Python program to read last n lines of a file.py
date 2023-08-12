# Write a Python program to read last n lines of a file.
file = open("tops.txt","r")
last_line = file.readlines()[-1]
print(last_line)
file.close()
