print("Welcome")

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

if a == b == c:
    print(f"All numbers are equal and the value is {a}")
elif a == b and a > c:
    print(f"a and b are equal and the greatest value is {a}")
elif a == c and a > b:
    print(f"a and c are equal and the greatest value is {a}")
elif b == c and b > a:
    print(f"b and c are equal and the greatest value is {b}")
elif a == b and a < c:
    print(f"a and b are equal, but the greatest value is {c}")
elif a == c and a < b:
    print(f"a and c are equal, but the greatest value is {b}")
elif b == c and b < a:
    print(f"b and c are equal, but the greatest value is {a}")
elif a >= b and a >= c:
    print(f"Greatest of the entered numbers is: {a}")
elif b >= a and b >= c:
    print(f"Greatest of the entered numbers is: {b}")
else:
    print(f"Greatest of the entered numbers is: {c}")
