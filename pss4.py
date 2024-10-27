# wap to create a array of 10 element, containing 10 prime numbers starting from 23

# a=int(input('Enter a +ve number : '))

b=int(input("how many prime number do you want : "))
prime=[]
counter=1
for a in range(23,100):
    n=2
    k=1
    while a>n:
        if a%n == 0:
            k = 0
        n = n + 1

    if k!=0:
        # print(f"{a} is prime")
        prime.append(a)
        counter = counter + 1

    if counter==b+1:
        break
    # print(counter)

print(prime)