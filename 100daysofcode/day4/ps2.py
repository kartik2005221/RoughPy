#who pays the bill

import random
random.seed(int(input("Enter seed: ")))

name = input("enter names separated by (just) commas : ").split(",")

lenn = len(name)
payer = name[random.randint(0, lenn-1)]

print(f"{payer} will pay the bill")