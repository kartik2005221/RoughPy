# 6. Write a program to mine a log file and find out whether it contains ‘python’.
# 7. Write a program to find out the line number where python is present from ques 6.

a=0
i=1
f=open("log.txt")

while a==0:
    cont = f.readline()
    content=cont.lower()
    print(f"scanning line number {i}")
    if content.find("python")==-1:
        a=0
    else:
        a=1
        print(f"python found in line number {i}")
        break
    if cont == "":
        a=1
        print(f"no line number {i} exist in file\nquiting...")

    i+=1
else:
    print("no python found in none of line")
f.close()
print("Task Done")
