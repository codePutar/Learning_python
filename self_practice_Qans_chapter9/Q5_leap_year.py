yr = int(input("Enter the year: "))

if yr%4==0 or (yr%100==0 and yr%400 ==0):
    print("its a leap year")
else:
    print("its not a leap year")