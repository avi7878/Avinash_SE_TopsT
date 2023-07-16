import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 130)  
engine.setProperty('volume', 10) 


status = True
while status:
    print("\nWelcome to kalyan Jwellers")
    engine.say("Welcome to kalyan Jwellers")
    engine.runAndWait()
    
    engine.say("Enter your Name")
    engine.runAndWait()
    name = input("Enter your Name : ")
    
    engine.say("Enter your Gender(male,female)")
    engine.runAndWait()
    gender = input("Enter your Gender(male,female) : ")

    engine.say("Enter your age")
    engine.runAndWait()
    age = int(input("Enter your age : "))

    print("--------------------------------------------------\n")

    engine.say("Enter product name")
    engine.runAndWait()
    product = input("Enter product name : ")

    engine.say("Enter product gram")
    engine.runAndWait()
    gram = int(input("Enter product gram : "))
    print("Current gold price (1 gram) : 5752")
    total_gold_price = gram * 5752

    print("---------------------------------------------------\n")

    print("Your total gold price is : ",total_gold_price)


    print("Making charges (1 gram) : 845")
    total_making_charges = gram * 845
    print("Total making charge is : ",total_making_charges)

    print("----------------------------------------------------\n")

    total_amount = total_gold_price + total_making_charges
    print("Total amount is : ",total_amount)


    if gender == "male":
        if age >= 65:
            if  200000 < total_amount < 300000:
                print("20% Discount on purchase of 2 lakh to 3 lakh")
                total_net_amount =  total_amount - (total_amount * 0.2)
            elif 300000 < total_amount < 500000:
                print("30% Discount on purchase of 3 lakh to 5 lakh")
                total_net_amount =  total_amount - (total_amount * 0.3)
            elif total_amount > 500000:
                print("35% Discount on purchase to above 5 lakh")
                total_net_amount =  total_amount - (total_amount * 0.35)
        else:
            if 200000 < total_amount < 300000:
                print("10% Discount on purchase of 2 lakh to 3 lakh")
                total_net_amount =  total_amount - (total_amount * 0.1)
            elif 300000 < total_amount < 500000:
                print("20% Discount on purchase of 3 lakh to 5 lakh")
                total_net_amount =  total_amount - (total_amount * 0.2)
            elif total_amount > 500000:
                print("25% Discount on purchase to above 5 lakh")
                total_net_amount =  total_amount - (total_amount * 0.25)

    elif gender == "female":
        if age >= 65:
            if 200000 < total_amount < 300000:
                print("25% Discount on purchase of 2 lakh to 3 lakh")
                total_net_amount =  total_amount - (total_amount * 0.25)
            elif 300000 < total_amount < 500000:
                print("35% Discount on purchase of 3 lakh to 5 lakh")
                total_net_amount =  total_amount - (total_amount * 0.35)
            elif total_amount > 500000:
                print("40% Discount on purchase to above 5 lakh")
                total_net_amount =  total_amount - (total_amount * 0.4)
        else:
            if 200000 < total_amount < 300000:
                print("15% Discount on purchase of 2 lakh to 3 lakh")
                total_net_amount =  total_amount - (total_amount * 0.15)
            elif 300000 < total_amount < 500000:
                print("25% Discount on purchase of 3 lakh to 5 lakh")
                total_net_amount =  total_amount - (total_amount * 0.25)
            elif total_amount > 500000:
                print("30% Discount on purchase to above 5 lakh")
                total_net_amount =  total_amount - (total_amount * 0.3)
    print("Your total net amount is : ",total_net_amount)
    check = input("Do you want to shoping continue ? press y for yes and n for no : ")
    if check == 'y':
        status = True
    elif check == 'n':
        status = False
else:
    print("Thank you visit again\N{Person with Folded Hands}")
    engine.say("Thank you visit again.")

engine.runAndWait()
