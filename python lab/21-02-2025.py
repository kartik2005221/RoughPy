import base64

a='kartik'
c=a.encode()
x=base64.b64encode(c)
print(x)

y=base64.b64decode(x.decode())
print(y)

