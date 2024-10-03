# Write a program to print multiplication table of a given number using while loop.

a=int(input("Enter a : "))
n=1

while(n<=10):
    print(f"{a} x {n} = {a*n}")
    n +=1
else:
    print("byee")