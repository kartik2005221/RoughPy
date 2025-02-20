import os

print(os.getcwd())
print("changing directory to desktop/kartik")
os.chdir("C:\\Users\\kartik\\Desktop\\kartik")

dirname = input("give name of dir to find (make if not  found) ::: ")
if os.path.exists(dirname):
    print(f"directory exists : {dirname}")
else:
    os.mkdir(dirname)
    print(f"directory created : {dirname}")