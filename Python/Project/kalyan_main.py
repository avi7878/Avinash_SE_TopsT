import kalyan_logic

status = True
while status:
    name = input("\nEnter your Name : ")
    gender = input("Enter your Gender : ")
    age = int(input("Enter your Age : "))
    product_name = input("Enter your Product Name : ")
    product_gram = int(input("Enter your Product Gram : "))

    print("-----------------------------------------------")

    print(kalyan_logic.coustomer(name,gender,age,product_name,product_gram))

    check = input("\nDo you want to shoping continue ? press y for yes and n for no : ")
    if check == 'y':
        status = True
    elif check == 'n':
        status = False
else:
    print("Thank you visit again")