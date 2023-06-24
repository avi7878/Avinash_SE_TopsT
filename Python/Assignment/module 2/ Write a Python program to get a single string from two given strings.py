# Write a Python program to get a single string from two given strings, 
#separated by a space and swap the first two characters of each string. 
def string(a1,a2):# create a function and pass two parameter
    a = a1[:2] + a2[2:] # first string two char and second string after two char addition
    b = a2[:2] + a1[2:] # seond string two char and first string after two char addition

    return a + ' ' + b # return a , b and pass a1 to a2
# calling function
str1 = input("Enter the string1 : ")#taking a variable and accept the value from user.
str2 = input("Enter the string2 : ")#taking a variable and accept the value fron user.
print(string(str1,str2))#print 


