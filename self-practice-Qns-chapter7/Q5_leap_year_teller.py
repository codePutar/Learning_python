# A year is a leap year when it is divisible by 4 compeletly

year = int(input("Enter the year: "))

if year%4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")