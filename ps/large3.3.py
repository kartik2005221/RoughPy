print("Welcome")

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

if a == b == c:
    print(f"All numbers are equal and the value is {a}")
else:
    largest = max(a, b, c)  # Find the largest number

    if a == b:
        print(f"a and b are equal, greatest value is {largest}")
    elif a == c:
        print(f"a and c are equal, greatest value is {largest}")
    elif b == c:
        print(f"b and c are equal, greatest value is {largest}")
    else:
        print(f"Greatest of the entered numbers is: {largest}")
