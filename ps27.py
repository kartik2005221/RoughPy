a=[3,56,7]
b=[34, 56, 334]
c=[]

# this is main code of merging lists
for i in range(0, len(a)+len(b)):
    if i<len(a):
        c.append(a[i])
    elif i<=(len(a) + len(b)):
        c.append(b[i-len(a)])
print(c)