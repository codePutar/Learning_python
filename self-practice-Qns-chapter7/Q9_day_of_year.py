day= int(input("Enter a day no: "))
month = int(input("Enter Month number: "))

if not(1<= month <=12 and 1<=day<=30):
    print("Invalid date (day must be 1-30 adn months be 1-13)")
else:
    day_of_year = (month-1)*30+day
    print("Day of year: ", day_of_year)