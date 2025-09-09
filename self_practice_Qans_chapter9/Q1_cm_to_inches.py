a = float(input("Enter a value in cm: "))

if a<0:
    print("Invalid value enter positive value please !")
else:

    b = a//2.54
    print(f"{a}cm is {b}inch")