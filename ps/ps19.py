#Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.

a=int(input("enter a number\nfor which table is to be printed : "))

with open("table.txt", "w") as f:
    f.write("")

for i in range(0,11):
    table = f"{a} x {i} = {a*i}\n"
    with open("table.txt","a") as f:
        f.write(table)
else:
    print("Task Done, Check your file..!")