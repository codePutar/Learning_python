a = int(input("Enter number of items: "))

cost = 0
#conditions
if a<10:
    cost = a*120
elif a>=10 and a<=99:
    cost = (10*120)+((a-10)*100)
elif a>=100:
    cost = (10*120)+(89*100)+((a-99)*70)


print(f"Cost: {cost}")