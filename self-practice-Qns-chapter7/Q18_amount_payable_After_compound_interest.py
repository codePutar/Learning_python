p,r,t = float(input("Enter principal amount: ")), float(input("Enter rate of interest: ")),float(input("Enter time period: "))

#Calculating payable amount

A = p*((1+(r/100))**t)

print(f"Payable amount = {A}")