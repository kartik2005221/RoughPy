#love calculator
# t r u e    l o v e = %%

n1=input("Enter your name? ").lower()
n2=input("Enter their name? ").lower()

t=n1.count("t") + n2.count("t")
r=n1.count("r") + n2.count("r")
u=n1.count("u") + n2.count("u")
e=n1.count("e") + n2.count("e")

l=n1.count("l") + n2.count("l")
o=n1.count("o") + n2.count("o")
v=n1.count("v") + n2.count("v")
e=n1.count("e") + n2.count("e")

a=str(t+r+u+e)
b=str(l+o+v+e)

ls = int(a +b)
# print(f"Your love score is {ls}")/

if ls<10 or ls>90:
    print(f"Your love score is {ls}%, you go like Coke and Mentos.")
elif ls<50 and ls>40:
    print(f"Your love score is {ls}%, you are alright together.")
else:
    print(f"Your love score is {ls}%.")