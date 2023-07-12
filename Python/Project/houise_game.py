import random

l1 = []
user = []
computer = []

while len(l1) < 12 :
    l2 = random.randint(1,100)

    if l2 not in l1:
        l1.append(l2)

list_12 = [str(l1)for l1 in l1]
result = " ".join(list_12)
print("\n\n\n\t\t\t\t",result,"\n\n\n")

while len(user) < 6:
    u1 = random.choice(l1)

    if u1 not in user:
        user.append(u1)

user_6 = [str(user)for user in user]
u_result = " ".join(user_6)
print("\t\tUSER       : ",u_result)

for i in l1:
    if i not in user:
        computer.append(i)

computer_6 = [str(computer)for computer in computer]
c_result = " ".join(computer_6)
print("\t\tCOMPUTER   : ",c_result,"\n\n")

print("\t\tGAME START : \n\n")
for i in range(11):

    input("\t\tEnter.... ")
    choice = random.choice(l1)
    l1.remove(choice)
    print("\n\t\t\t\t\tLUCK NUMBER : ",choice,"\n\n")

    if choice in user:
        user.remove(choice)
    user_6 = [str(user)for user in user]
    u_result = " ".join(user_6)
    print("\t\tUSER       : ",u_result,)

    if choice in computer:
        computer.remove(choice)
    computer_6 = [str(computer)for computer in computer]
    c_result = " ".join(computer_6)
    print("\t\tCOMPUTER   : ",c_result,"\n\n")

    if len(user) == 0:
        print("\t\t\t\t\tUSER WON !!!\n\n")
        break
    
    elif len(computer) == 0:
        print("\t\t\t\t\tCOMPUTER WON !!!\n\n")
        break

