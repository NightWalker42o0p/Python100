print("Welcome To Tip Generator")
bill=float(input("What was the amount of the bill?"))
tip=float(input("What percentage of tip would you like to give?"))
people=int(input("How many people to split the bill?"))
tip_num=(tip/100)*bill
tip_amount=round(tip_num,2)
total_bill=(bill+tip_amount)
perhead_pay=round(total_bill/people,2)
print(f"Each person should pay {perhead_pay}")
