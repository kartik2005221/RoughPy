# Write a program to find whether a given number is prime or not.

a=int(input('Enter a +ve number : '))
n=2
factr=[]

while a>n:
    if a%n==0:
        k=0
        factr.append(n)
    n = n + 1

if a==1:
    print(f"{a} is neither prime nor odd")
elif k==0:
    print(f"{a} is not prime\nbcz its divisible by {factr}")
else:
    print(f"{a} is prime")
