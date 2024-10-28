# Write a class “Calculator” capable of finding square, cube and square root of a number.

import math

class Calculator:
    def __init__(self, no):
        self.no=no

    def square(self):
        return math.pow(self.no, 2)

    def cube(self):
        return math.pow(self.no, 3)

    def sqoot(self):
        return math.sqrt(self.no)

k=1
while k==1:
    a = int(input("enter a number : "))
    c = input("Enter what do you want to do? \n \t1 -> Square Root\n \t2 -> Square\n \t3 -> Cube\n::: ")

    b = Calculator(a)

    if c == '1':
        print(f"Square Root is {b.sqoot()}")
    elif c == '2':
        print(f"Square Root is {b.square()}")
    elif c == '3':
        print(f"Square Root is {b.cube()}")
    else:
        print("Invalid Number Entered")
        k=1
        continue

    k=int(input("Do You want to continue?\n\t1 -> Yes\n\t2 -> No\n\t::: "))
else:
    print("Quitting\nByee...")


