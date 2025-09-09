p = int(input("Enter the Perpendicular side of triangle: "))
b = int(input("Enter the Base side of triangle: "))
h = int(input("Enter the Hypotenious side of triangle: "))

print()
if p == b ==h:
    print("Its an Equilateral triangle")
elif (p==b) or (p==h) or (b==h):
    print("Its an Isosceles triangle")
else:
    print("Its an Scalene triangle")