a = []

for i in range(0,5):
    b = int(input(f"Enter number {i+1}/5: "))
    a.append(b)

a.sort()
print(f"Second largest number: {a[len(a)-2]}")