import math

side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the seconde side: "))

# implementing pythogorus theorum
side3 = math.sqrt(side1**2 + side2**2)

print(f"Side 3 = {side3}")