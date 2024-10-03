# Write a program using functions to find greatest of three numbers

def large(a,b):
    if a>=b:
        return a
    else:
        return b

a=int(input("enter a : "))
b=int(input("enter b : "))
c=int(input("enter c : "))

if large(a, b)==a:
    ans=large(a,c)
elif large(a,b)==b:
    ans=large(b,c)

print(f"Largest of three numbers is {ans}")