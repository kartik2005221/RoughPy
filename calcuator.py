# welcome (by AiR)
# 08-11-2024

def calc():
    a=float(input("Enter a number : "))
    b=input("+\n-\n*\n/\nEnter a operator:")
    c=float(input("Enter second number : "))
    if b=='+':
        d=a+c
    elif b=='-':
        d=a-c
    elif b=='*':
        d=a*c
    elif b=='/':
        d=a/c
    else:
        d="NA"
    if d=='NA':
        pass
    print(f"Your Result is:\n{a} {b} {c} = {d}\n")
    return d

def calc_old():
    a=e
    b=input("Enter a operator:")
    c=float(input("Enter second number : "))
    if b=='+':
        d=a+c
    elif b=='-':
        d=a-c
    elif b=='*':
        d=a*c
    elif b=='/':
        d=a/c
    else:
        d="NA"
    if d=='NA':
        pass
    print(f"Your Result is:\n{a} {b} {c} = {d}\n")
    return d

print("Welcome")
e=calc()
f='o'

while f!='q':
    f = input(f"Type 'y' to continue with {e}\nor Type 'n' to continue with new calculation\nor Type q for exit\n:::")
    if f == 'y':
        calc_old()
    elif f == 'n':
        calc()
    # elif f == 'q':
    #     break

print("Bye..!")