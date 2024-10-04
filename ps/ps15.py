#Write a program to print multiplication table of n using for loops in reversed order

n=int(input("enter a : "))

# for i in range(n+1,0):
#     print(f"{n} x {i} = {n*i}")

i=10
while(i>0):
    print(f"{n} x {i} = {n*i}")
    i-=1