# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

a=int(input("enter marks of subject 1: "))
b=int(input("enter marks of subject 2: "))
c=int(input("enter marks of subject 3: "))

if a<0 or b<0 or c<0:
    print("marks cant be -ve")
elif a>100 or b>100 or c>100:
    print("marks cant exceed more than 100 marks")
elif a<=33 and b<=33 and c<=33:
    print("failed")
elif (a+b+c)/3 <=40:
    print("failed")
else:
    print("pass")