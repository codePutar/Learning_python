# pi*(r**2)*h

import math

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

#finding volume of cylinder

v = math.pi*(r**2)*h

print(f"Volume of Cylinder of radius={r} and height={h} is {v}")