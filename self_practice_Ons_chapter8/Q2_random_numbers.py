import random

a,b,c,d,e,f= random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10)

print(f"Random number 1: {a}\nRandom number 2: {b}\nRandom number 3: {c}\nRandom number 4: {d}\nRandom number 5: {e}\nRandom number 6: {f}")

# mean

sum = a+b+c+d+e+f

m = sum/6
m = int(m)
print(f"Mean of 6 digits = {m}")

# median
if sum%2==0:
    med = ((sum/2)+((sum/2)+1))/2
    med = int(med)
    print(f"Median = {med}th term")
    
else:
    med = (sum+1)/2
    med  = int(med)
    print(f"Median = value of {med}th term")
#mode