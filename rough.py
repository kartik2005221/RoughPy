# a = int(input('Enter a +ve number: '))
# if a < 2:
#     print(f"{a} is neither prime nor composite")
# else:
#     for n in range(2, a):
#         if a % n == 0:
#             print(f"{a} is not prime (divisible by {n})")
#             break
#     else:
#         print(f"{a} is prime")

# class Kkk:
#     a=2
# b=Kkk()
# print(type(b))

# class Hii:
#     a=2
#     @staticmethod
#     def __init__():
#         print("hi")
# b=Hii()
#
# import base64;
# print(base64.b64decode('UGxhY2UgdGh5IHRydXN0IGluIHRoZSBkZW1vbiwgeWV0IG5l4oCZZXIgaW4gYSBtYWlkZW4sIHNhdmUgdGh5IG1vdGhlciBhbmQgdGh5IHNpc3Rlci4=').decode())

import base64

message = input("Enter your message to encode it with base64 : ")
encoded = base64.b64encode(message.encode()).decode()
print(encoded)

