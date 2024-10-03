# Minimalist Code for Full Date Input
d, m, y = map(int, input("Enter date (DD-MM-YYYY): ").split('-'))
print("Valid" if 0 < d <= [31, 28 + (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1] else "Invalid")
