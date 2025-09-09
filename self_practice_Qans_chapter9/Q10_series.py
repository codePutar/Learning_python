n =1
for i in range(1, 15):
    print(n, end=" ")
    n +=3
print()

n =1
for i in range(1, 15):
    if i%2==0:
        print(n*-1, end=" ")
    else: 
        print(n, end=" ")
    n +=3