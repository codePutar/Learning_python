t, ta = int(input("Enter a number between 1 and 12: ")), int(input("How many hours ahead: "))

#calculation

c = t+ta

if c <=12:
    print(f"Time at that time would be: {float(c)} clock's")
elif c>12 and c<=24:
    d = c - 12
    print(f"Time at that time would be: {float(d)} clock's")
else:
    d = c-24
    print(f"Time at that time would be: {float(d)} clock's")