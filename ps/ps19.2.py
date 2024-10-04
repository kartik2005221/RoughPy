#Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.

a=int(input("enter a number\nfor which table is to be printed : "))
fintab=""

for i in range(1,11):
    table = f"{a} x {i} = {a * i}\n"
    fintab = fintab + table
else:
    with open("table.txt", "w") as f:
        f.write(fintab)
    print("Task Done\nCheck Your File..!")