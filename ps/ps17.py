#Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

with open("poem.txt", "r") as f:
    p=f.read()

l= p.lower()

if l.find("twinkle")==-1:
    print("there is no 'Twinkle' on poem")
else:
    print("there is 'Twinkle' in poem")