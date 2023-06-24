#  Write a Python program to count occurrences of a substring in a string. 

str = input("Enter your string : ")

for i in range(len(str)):
    for j in range(i+1,(len(str)+1)):
        print(str[i:j],end=" ")
    print()
    