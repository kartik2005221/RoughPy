#rock paper scisor

import random

comcho = random.randint(1,3)
print('''
Welcome

1 -> for rock
2 -> for paper
3 -> for scisor''')
mycho = int(input("Whats your choice ? ::: "))

print(f"your choice = {mycho}\nand computer choice = {comcho}")

if comcho == mycho:
    print("Draw...!")
elif comcho == 1 and mycho == 2:
    print("You win..!")
elif comcho == 1 and mycho == 3:
    print("You lose")
elif comcho == 2 and mycho == 1:
    print("You lose")
elif comcho == 2 and mycho == 3:
    print("You win..!")
elif comcho == 3 and mycho == 1:
    print("You win..!")
elif comcho == 3 and mycho == 2:
    print("You lose")
