a = int(input("Enter a number: "))
a = str(a)

if int(a[-1]) == 4:
    print("Ends with 4")
elif int(a[-1]) == 8:
    print("Ends with 8")
else:
    print("Ends with neither")