add_Name = int(input("Enter you want to add name : "))# taking variable and accept the users
names = [] #taking variable and add list

for i in range(1,add_Name+1):# loop will execute 1 to user enter value.
    name = input("Enter the name : ")# taking variable and accept the name
    names.append(name)# append function is use to add value in list
   
print(names)
