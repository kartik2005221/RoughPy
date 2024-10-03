# Write a program to print multiplication table of a given number using for loop.

a=int(input("Enter a : "))

for i in range(0,11):
    print(f"{a} x {i} = {a*i}")