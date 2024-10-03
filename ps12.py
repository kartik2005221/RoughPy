#Write a program to calculate the factorial of a given number using for loop.

a=int(input("Enter a number : "))
b=1

while(a>0):
    b=b*a
    a-=1

print("factorial is", b)