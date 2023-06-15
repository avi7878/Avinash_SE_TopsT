# 1) convert months into years


total_months = int(input("Enter month : "))
years,month = divmod(total_months, 12)

print(years,"Years",month,"Months")
