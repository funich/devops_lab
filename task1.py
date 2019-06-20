year = int(input("input a year: "))
if year % 4:
    print("false")
elif year % 100 == 0 and year % 400:
    print("false")
else:
    print("true")
