print("Welcome To Tip Generator")
bill=float(input("What was the amount of the bill?"))
tip=float(input("What percentage of tip would you like to give?"))
people=int(input("How many people to split the bill?"))
tip_num=(bill+(tip/100))/people
tip_amount=round(tip_num,2)
print(f"Each person should pay {tip_amount}")
