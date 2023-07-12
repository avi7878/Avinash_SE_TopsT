#  Write a Python program to get unique values from a list 

list1 = [1,1,2,"avinash","java",2,"java","python"]
unique_list = list(set(list1))


# print("\n",list1)

# for i in list1:
#     if i not in unique_list:
#         unique_list.append(i)

print("\nUnique value from the list : ",unique_list)
