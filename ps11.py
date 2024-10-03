# Write a program to find the sum of first n natural numbers using while loop.

n=int(input("enter n : "))
a=0
b=0

while(a<n):
    a+=1
    print(a)
    b=b+a

print(f"sum iz {b}")