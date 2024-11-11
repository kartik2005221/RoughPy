#random head tail

import random

random.seed(int(input("Enter seed: ")) + random.randint(6546,549651))
k=random.randint(1,2)
print(k)

if k==1:
    print("Tails")
else:
    print("Heads")