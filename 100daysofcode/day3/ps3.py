#leap year checker

year = int(input("enter a year : "))

if year % 4 == 0:
    if year % 100 !=0:
        print("leap year")
    elif year % 100 ==0:
        if year%400==0:
            print("leap century year")
        else:
            print("not leap year, but century year")
else:
    print("not leap year")