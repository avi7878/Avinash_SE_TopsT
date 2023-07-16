#  Write a Python program to print all unique values in a dictionary.

d1 = {'a': 100, 'b': 200, 'c':300,'e': 100, 'f': 200, 'c':300}
l1 = []
for i in d1.values():
    l1.append(i)

s1 = set(l1)
print(s1)


