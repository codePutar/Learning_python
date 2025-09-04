import random

for _ in range(10):
    num = random.randint(100,999)
    num = num-(num%5)
    print(num, end=" ")