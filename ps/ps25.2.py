import math

class Calculator:
    def __init__(self, no):
        self.no = no

    def square(self):
        return math.pow(self.no, 2)

    def cube(self):
        return math.pow(self.no, 3)

    def square_root(self):
        return math.sqrt(self.no)

# Input from user
a = int(input("Enter a number: "))
c = input("Enter what do you want to do? \n\t1 -> Square Root\n\t2 -> Square\n\t3 -> Cube\n::: ")

# Create a Calculator instance
b = Calculator(a)

# Perform the selected operation
if c == '1':
    result = b.square_root()
    print(f"The square root of {a} is {result}")

elif c == '2':
    result = b.square()
    print(f"The square of {a} is {result}")

elif c == '3':
    result = b.cube()
    print(f"The cube of {a} is {result}")

else:
    print("Invalid option selected.")

# BY CHATGPT