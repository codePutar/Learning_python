# are of sphere = 4pi(r**2)

import math

area = float(input("Enter the area of sphere: "))

#finding radius
radius = math.sqrt(area/(4*math.pi))

print(f"radius: {radius}")