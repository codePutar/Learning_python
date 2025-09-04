a = int(input("Enter a Three digit number: "))

b = a
c =0 

while b != 0:
    r = b%10
    c = c*10+r
    b //= 10

print(f"reversed of {a} = {c}")