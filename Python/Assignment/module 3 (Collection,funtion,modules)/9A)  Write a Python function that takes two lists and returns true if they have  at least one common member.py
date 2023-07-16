l1 = []
l2 = []

def add(l1):
    num = int(input("Enter how many elements input in list : "))
    for i in range(0,num):
        add = input("Enter Elements : ")
        l1.append(add)

def common(l1,l2):
    for i in l1:
        if i in l2:
            return "True"
        else:
            return "False"

print("\nAdd in list 1")
add(l1)
print(l1)
print("\nAdd in list 2")
add(l2)
print(l2)
print(common(l1,l2))






