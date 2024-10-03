date = int(input("Enter date : "))
month = input("Enter month : ").lower()
year = int(input("Enter year : "))

invalid = "InValid date"
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
m31 = ('jan', 'mar', 'may', 'july', 'oct', 'dec')
m30=('apr', 'jun', 'sept', 'nov')

if date <= 0:
    print(invalid)
elif (month == 'feb') and ((is_leap_year and date > 29) or (not is_leap_year and date > 28)):
    print(invalid)
elif month in m31 and date > 31:
    print(invalid)
elif month in m30 and date > 30:
    print(invalid)
else:
    print("Date is Valid..!")
