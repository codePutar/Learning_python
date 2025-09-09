a = []

for i in range(0,5):
    b = int(input(f"Enter numbers {i+1}/5: "))
    a.append(b)

a.sort()
print(f"Largest number: {a[len(a)-1]}")