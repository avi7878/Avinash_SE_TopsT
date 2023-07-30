import datetime
print("\n\tWelcome to Amazing Pizza and Pasta Pizzeria")

select = """
                    press 1 : Order menu

                    press 2 : Exit

"""
valid = True
pizza_dic = {
        "medium pizza" : 10.99,
        "large pizza" : 20.99,
        "family pizza" : 29.99
}
pasta_dic = {
        "normal pasta" : 9.5,
        "italian pasta" : 17.00,
        "noodle pasta" : 27.50
}

print(select)
today_payment = []
total_pizza_bill = []
total_pasta_bill = []
total_p_p = []
bruschetta = []
soft_drink = []
chocco = []
choice_select = int(input("Enter your choice : "))
while valid:
    if choice_select == 1:
        print("\n====================== ORDER MENU ======================")
        menu = """  
                        press 1 for pizza

                        press 2 for pasta
                """
        name = input("Enter your name : ")
        add = True
        total_net_amount = 0
        pizza_bill = 0
        pasta_bill = 0
        pizza_qty = 0
        pasta_qty= 0
        while add:
            print(menu)
            print(f"Welcome {name}")
            choice_menu = int(input("Enter your choice : "))
            if choice_menu == 1:
                print("\n====================== PIZZA MENU ======================")
                piza_menu = """
                    1) medium pizza = 10.99 AUD 

                    2) large Pizza = 20.99 AUD 

                    3) family Pizza = 29.99 AUD

        ***Buy 4 or more pizza and get 1.5lt of soft drink free***
        
***Buy 4 or more pizzas and pastas and get 2 chocco brownies ice cream free.
                            """
                print(piza_menu)
                pizza_order = input("Enter your order name : ")
                pizza_qty = int(input("Enter your Qty : "))
                total_p_p.append(pizza_qty)
                if pizza_order in pizza_dic:
                    pizza_bill = pizza_qty * pizza_dic.get(pizza_order)
                    total_pizza_bill.append(pizza_bill)
                    print("Your pizza order amount is : ",pizza_bill)
                if pizza_qty >= 4:
                    print("\n\t *** Congratulations !! 1.5lt softdrink free *** \n")
                    soft_drink.append(1)
            elif choice_menu == 2:
                print("\n====================== PASTA MENU ======================")
                pasta_menu = """
                    1 Normal pasta = 9.5 AUD 

                    2 italian pasta = 17.00 AUD 

                    3 noodle pasta = 27.50 AUD

        ***Buy 4 or more pastas and get 2 bruschetta free.***

                            """
                print(pasta_menu)
                pasta_order = input("Enter your order name : ")
                pasta_qty = int(input("Enter your Qty : "))
                total_p_p.append(pasta_qty)
                if pasta_order in pasta_dic:
                    pasta_bill = pasta_qty * pasta_dic.get(pasta_order)
                    total_pasta_bill.append(pasta_bill)
                    print("Your pasta order amount is :",pasta_bill)
                if pasta_qty >= 4:
                    print("\n\t *** Congratulations !! get 2 bruschetta free *** \n")
                    bruschetta.append(2)
                
                if pasta_qty >= 4 and pizza_qty >= 4:
                    print("\n---------------------- COMBO OFFER APPLY ----------------------\n")
                    print("*** Congratulations !! get 2 chocco brownies ice cream free ***")
                    chocco.append(2)
                    
            else:
                print("Invalid Input !!!\nPLEASE TRY AGAIN")
                add = True
            add_item = input("Do you want add more items(y/n) : ")
            if add_item == 'y':
                add = True
            else:
                add = False
        total_net_amount = pizza_bill + pasta_bill
        today_payment.append(total_net_amount)
        print("\nTotal net amount : ",total_net_amount)

    elif choice_select == 2:
        print("\n\t\texit")
    else:
        print("Invalid Input !!!\nPLEASE TRY AGAIN")
        valid = True
    add_item = input("Want to enter order from another customer (Y/N) : ")
    if add_item == 'y':
            valid = True
    else:
            valid = False

print("====================== TODAY SHOP RECEIPT ======================")
print("\npayment received from pizza : ",sum(total_pizza_bill))
print("\npayment received from pasta : ",sum(total_pasta_bill))
print("\npayment received today : ",sum(today_payment))
print("\nNumber of pizza and pasta sold in one shift :  ",sum(total_p_p))
print("\nNumber of 1.5lt soft drink bottles given : ",sum(soft_drink))
print("\nNumber of bruschetta given to customer : ",sum(bruschetta))
print("\nNumber of chocco brownies ice cream given to customer : ",sum(chocco))
print("*****************************************************************")
print("\n\t\t\tBye Bye !!!\n")

today = str(datetime.date.today())
name = today

file = open("ID"+name+".txt","a")

file.write("====================== TODAY SHOP RECEIPT ======================")
file.write("\npayment received from pizza : "+str(sum(total_pizza_bill)))
file.write("\npayment received from pasta : "+str(sum(total_pasta_bill)))
file.write("\npayment received today : "+str(sum(today_payment)))
file.write("\nNumber of pizza and pasta sold in one shift :  "+str(sum(total_p_p)))
file.write("\nNumber of 1.5lt soft drink bottles given : "+str(sum(soft_drink)))
file.write("\nNumber of bruschetta given to customer : "+str(sum(bruschetta)))
file.write("\nNumber of chocco brownies ice cream given to customer : "+str(sum(chocco)))
file.write("\n*****************************************************************")
file.write("\n\t\t\tBye Bye !!!\n")
file.close