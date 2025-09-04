p =  float(input("Enter principle amount: "))
r =  float(input("Enter interest rate: "))
t =  float(input("Enter time: "))

# calculating simple interest
si = (p*r*t)/100.0

#calculating amount payable
a= p +si

print(f"Amount payable after simple interest: {a}")