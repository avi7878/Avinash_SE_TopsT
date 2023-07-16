#  Write a Python program to find the repeated items of a tuple. 

tuple1 = ('python',78,'java','php','nord.js','c++','java','php','nord.js')
repeated = []
add = []

for i in tuple1:
    if i in add:
        repeated.append(i)
    else:
        add.append(i)

print("Main List : ",tuple1)
print("Repeated Items : ",repeated)
