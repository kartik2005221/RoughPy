import random

word_list = ["aardvark", "baboon", "camel"]

random_word = random.choice(word_list)
print(random_word)

guess = input("Guess a Word: ").lower()

for letter in random_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
