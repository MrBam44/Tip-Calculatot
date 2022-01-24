print("welcome to tip calculator!")
bill= float(input("wha is the total bill?"))
tip = int(input("what is the what percenteg tip would you like to give?"))
split = int(input("how may pepol to split the bill?"))
bill_with_tip = tip/100*bill+bill
print(bill_with_tip)