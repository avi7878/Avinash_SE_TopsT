# Write a Python program to copy the contents of a file to another file.

file = open("tops.txt","r")
c=file.read()

f = open("Copy.txt","w")
f.write(c)
