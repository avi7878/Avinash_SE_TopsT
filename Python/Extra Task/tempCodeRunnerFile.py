
print("----------------------------------------------------\n")

total_amount = total_gold_price + total_making_charges
print("Total amount is : ",total_amount)

while status:
    if gender == "male":
        if age >= 65:
            if total_amount > 200000 and total_amount < 300000:
                print("20% Discount on purchase of 2 lakh to 3 lakh")
                total_net_amount =  total_amount - (total_amount * 0.2)
                print("Your total net amount is : ",total_net_amount)
            elif total_amount > 300000 and total_amount < 500000: