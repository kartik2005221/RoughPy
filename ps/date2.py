try:
    date = int(input("Enter date : "))
    year = int(input("Enter year : "))
except ValueError:
    print("Please enter valid integers for date and year.")
    exit()  # Exit the program if invalid input

month = input("Enter month : ").lower()  # Make the month input case-insensitive

valid_months = ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec')

if month not in valid_months:
    print(invalid)
elif date <= 0:
    print(invalid)
elif (month == 'feb') and ((is_leap_year and date > 29) or (not is_leap_year and date > 28)):
    print(invalid)
elif month in ('jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec') and date > 31:
    print(invalid)
elif month in ('apr', 'jun', 'sept', 'nov') and date > 30:
    print(invalid)
else:
    print(f"Date {date} {month.capitalize()} {year} is Valid..!")
