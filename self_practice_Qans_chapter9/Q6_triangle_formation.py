# rule :  a+b>c; b+c>a; c+a>b
a,b,c = int(input("Enter 1st side of triangle: ")), int(input("Enter 2nd side of triangle: ")), int(input("Enter 3rd side of triangle: "))

if (a+b>c)and(b+c>a) and(c+a>b):
    print("All three sides will form a triangle ")
else:
    print("non will be able to form triangle")