#Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

with open("poem.txt", "r") as f:
    p=f.read()

p.find("Twincle")