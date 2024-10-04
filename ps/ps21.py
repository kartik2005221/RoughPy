#Write a program to mine a log file and find out whether it contains ‘python’.

with open("log.txt") as f:
    content = f.read()

content.lower()
if content.find("python")!=-1:
    print("this log file is about python")
else:
    print("this log file is not about python")