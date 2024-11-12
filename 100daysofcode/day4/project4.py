#rock paper scisor

import random

rock = '''

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

art = [rock, paper, scissors]
comcho = random.randint(1,3)
print('''
Welcome

1 -> for rock
2 -> for paper
3 -> for scisor''')
mycho = int(input("Whats your choice ? ::: "))

print(f"your choice = {mycho}\n{art[mycho-1]}\nand computer choice = {comcho}\n{art[comcho-1]}")

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
