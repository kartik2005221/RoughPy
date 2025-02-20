n = int(input("enter a number to find square root : "))

x=n/2
old = 0

while True:
    old = x
    x = (x + (n/x))/2

    if old == x:
        print(f"sq root : {x}")
        break

