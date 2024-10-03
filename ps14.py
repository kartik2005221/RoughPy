# Write a program to print the following star pattern.
# * * *
# *    * for n = 3
# * * *

# basically we have to make a ring

a=int(input("enter a : "))

for i in range(1,a+1):
    if(i==1) or i==a:
        print("*"*a, end="")
    else:
        print("*", end="")
        print(" "*(a-2), end="")
        print("*", end="")
    print("")