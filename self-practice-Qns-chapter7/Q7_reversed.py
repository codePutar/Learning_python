a = int(input("Enter a number: "))

b = a
c = 0

while b!=0:
    r = b%10
    c = c*10+r
    b = b//10 # use double slash(//) for getting quient in int format 

print(f"Reversed form of {a} is {c}")