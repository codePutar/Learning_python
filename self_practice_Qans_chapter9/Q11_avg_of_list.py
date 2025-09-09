a = []

for i in range(0,5):
    b = int(input(f"{i+1} Enter a number: "))
    a.append(b)

b = 0
for i in range(0,len(a)):
    b +=a[i]

avg = b//len(a)

print(f"Avg: {avg}")