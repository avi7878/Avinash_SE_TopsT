# Write a Python program to count the number of characters (character frequency) in a string.

str = input("Enter the string : ")# taking a variable and accept the value from user.
frequency = {}# taking a variable it is empt

for i in str:# loop is execute and looping a string 
    if i in frequency: # if i in frequency then condition is true and store in frequency.
        frequency[i] += 1 # count a same value in frequency/(string).
    else:# i in not frequency then condition is false and print
        frequency[i] = 1 # string (char) is store in frequency(string).

print(frequency)# print frequency.
