a, b = float(input("Enter a number: ")), float(input("Enter second number: "))

if (a-b) <= 0.001 or (b-a) <= 0.001:
    print("close")
else:
    print("not close")