years = float(input("How many years ? : "))

if years%4 == 0:
    days = 12*366
    hours = days*24
    min = hours*60
    seconds = min*60

    print("days: ",days)
    print("hours: ",hours)
    print("min: ",min)
    print("sec: ",seconds)
else:
    days = 365
    hours = days*24
    min = hours*60
    seconds = min*60

    print("days: ",days)
    print("hours: ",hours)
    print("min: ",min)
    print("sec: ",seconds)