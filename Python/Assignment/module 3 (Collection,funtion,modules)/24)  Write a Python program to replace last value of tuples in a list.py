#  Write a Python program to replace last value of tuples in a list.

# def replace_last_value(tuples_list, new_value):
#     modified_list = []
#     for tpl in tuples_list:
#         modified_list.append(tpl[:-1] + (new_value,))
#     return modified_list

# # Example usage
# original_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# new_value = 10

# modified_list = replace_last_value(original_list, new_value)

# print("Original List:", original_list)
# print("Modified List:", modified_list)

original_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
change_value = int(input("Enter the change value : "))
modified_list = []

for i in original_list:
    new_tuple = i[:-1] + (change_value,)
    modified_list.append(new_tuple)

print("Original List:", original_list)
print("Modified List:", modified_list)


