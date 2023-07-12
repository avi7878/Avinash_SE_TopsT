#  Write a Python program to remove duplicates from a list.

list1 = ['python','java','nord.js','php','python','java','nord.js','php',]
unique_list2 = []

for i in list1:
    if i not in unique_list2:
        unique_list2.append(i)
    
print(unique_list2)


