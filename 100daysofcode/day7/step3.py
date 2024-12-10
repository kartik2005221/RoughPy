import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = []
word_length = len(chosen_word)
for position in range(word_length):
    placeholder.append("_")

unders = ""
word_length = len(chosen_word)
for position in range(word_length):
    unders+="_"
print(unders)

k=len(chosen_word)
# TODO-1: - Use a while loop to let the user guess again.

while k>0:
    guess = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        # print(i)
        if guess == chosen_word[i]:
            placeholder[i] = guess
            # print("t")
            k -= 1
            # break
        # else:
            # display.append("_")
            # pass
            # print("f")
    temp="".join(placeholder)
    print(temp)
print("You Win.")

# TODO-2: Change the for loop so that you keep the previous correct letters in display.



