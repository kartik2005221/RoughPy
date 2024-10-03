print("Welcome")

a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))

normess= 'Greatest of entered number is : '
mess=normess

if a>b:
    if a==c:
        large = a
        mess="a&c are equal and", normess
    elif b==c:
        large = a
        mess="b&c are equal and", normess
    elif c>a:
        large = c

    elif a>c:
        large = a

elif b>a:
    if a==c:
        large= b
        mess="a&c are equal and", normess
    elif b==c:
        large = b
        mess="b&c are equal and", normess
    elif c>b:
        large= c

    elif b>c:
        large = b

elif a==b:
    if a>c:
        large = a
        mess="a&b are equal and", normess

    elif c>a:
        large=c
        mess = "a&b are equal and", normess

    elif a==c:
        large=a
        mess="all numbers are equal and value is"

print(mess, large)