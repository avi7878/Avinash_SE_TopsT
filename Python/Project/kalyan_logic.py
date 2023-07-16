def coustomer(name,gender,age,product_name,product_gram):
    print("\nName : ",name)
    print("Gender : ",gender)
    print("Age : ",age)
    print("Product name : ",product_name)
    print("Product gram : ",product_gram)

    print("-----------------------------------------------")
    print("\nCurrent gold price (1 gram) : 5752")
    total_gold_price = product_gram * 5752

    print("Your total gold price is : ",total_gold_price)
    print("Making charges (1 gram) : 845")
    total_making_charges = product_gram * 845
    print("Total making charge is : ",total_making_charges)

    total_amount = total_gold_price + total_making_charges
    print("Total amount is : ",total_amount)
    # total_net_amount = 0
    print("================================================\n")
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

    return