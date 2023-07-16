# 14) Write a Python program to check whether a list contains a sub list

l1 = [12,'ac',23,45,'python','java','php',56,20]
l2 = ['python','java',56,45]

num = 0
result=False
for i in l2:
    if i in l1:
        num += 1
if(num==(len(l2))):
    result=True

print("\nlist contains in sub list : ",result,"\n")

     