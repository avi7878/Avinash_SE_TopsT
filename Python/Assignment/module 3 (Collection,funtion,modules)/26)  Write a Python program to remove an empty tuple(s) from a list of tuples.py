#  Write a Python program to remove an empty tuple(s) from a list of tuples.

list1 = [("python",),"java",(),"nord.js",(),"tops",()]
print("Original List : ",list1)
for i in list1:
    if len(i) == 0:
        list1.remove(i)

print("Empty tuple remove list : ",list1)