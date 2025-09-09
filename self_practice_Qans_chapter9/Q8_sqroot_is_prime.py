import math
num = int(input("Enter a number: "))

c = math.sqrt(num)
c = int(c)
d =0
for i in range(1,c+1):
    if c%i == 0:
        d +=1

if d==2:
    print("Entered number is a prime number")
else:
    print("Entered number is not a prime number")