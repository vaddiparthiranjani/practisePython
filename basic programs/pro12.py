# year is leap or not

year = int(input("enter year"))

if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(year,"is a leap year")
        else:
            print(year, "is a not leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is a not leap year")