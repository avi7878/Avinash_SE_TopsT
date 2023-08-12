# Write a Python program to append text to a file and display the text.

file = open("tops.txt","a")	
file.write("Now this is Appended Data")
file = open("tops.txt","r")
print(file.read())
file.close()	