#  Write a Python program to generate and print a list of first and last 5 
# elements where the values are square of numbers between 1 and 30. 

# list1 = [i**2 for i in range(1,31)]

# print("First 5 number square")
# for i in list1[:5]:
#     print(i)

# print("Last 5 number square")
# for i in list1[-5:]:
#     print(i)

list2 = []

for i in range(1,31):
    list2.append(i)
print(list2)

print("First 5 number of square")
for i in list2[:5]:
    print(i**2)

print("Last 5 number of square")
for i in list2[-5:]:
    print(i**2)
