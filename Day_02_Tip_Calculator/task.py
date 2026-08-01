print("Welcome to the TIP CALCULATOR!")
bill= float(input("What's your Total Bill? : $"))
tip_percentage = int(input("How much percentage would you like to tip 0,5,10,15,20? "))
total_bill_with_tip = (bill / 100) * tip_percentage + bill
print(f"Your total bill including TIP : ${round(total_bill_with_tip,2)}")
total_members= int(input ("How many people to split the bill? "))
split_bill= round(total_bill_with_tip / total_members,2)
print(f"Each person have to pay:${split_bill}")
