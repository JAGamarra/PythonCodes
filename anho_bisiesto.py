year = int(input("Type a year to verify if it is a leap-year: "))

if (year % 4 != 0):
    print("No, ain't a leap-year.")
elif (year % 100 != 0):
    print("Yes, it's a leap-year.")
elif (year % 400 != 0):
    print("No, ain't a leap-year.")
else:
    print("Yes, it's a leap-year.")