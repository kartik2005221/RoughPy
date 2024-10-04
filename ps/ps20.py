#A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.

with open("donkey.txt", "r") as f:
    txtt=f.read()

txtt.replace("donkey", "#####")
txtt.replace("Donkey", "#####")

with open("donkey.txt", "w") as f:
    f.write(txtt)