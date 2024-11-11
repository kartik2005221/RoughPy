# pizza challange...
# small pizza : 15
# medium pizza : 20
# large pizza : 25
# ppr for small : 2
# ppr for med, big,: 3
# extra chese : 1

ps = input("What size of pizza do you want? S/M/L ::: ")
ppr = input("Do you want Paperoni for your pizza? Y/N ::: ")
chs = input("Do you want Cheese for your pizza? Y/N ::: ")
bill=0

if ps == 'S':
    bill += 15
    if ppr=='Y':
        bill+=2
elif ps == 'M':
    bill += 20
    if ppr=='Y':
        bill+=3
elif ps == 'L':
    bill += 25
    if ppr=='Y':
        bill+=3

if chs=='Y':
    bill +=1

print(f"Your Total bill = ${bill}")