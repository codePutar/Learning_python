n = int(input("Enter a number (number > 20): "))

a = True
while a:
    if n > 20:
        a = False

for i in range(11, n+1):
    print(i,end=" ")
print()

if (n%3 ==0) and (n%7==0):
    print("TipsyTopsy")
elif n%7 ==0:
    print("Topsy")
elif n%3 ==0:
    print("Tipsy")