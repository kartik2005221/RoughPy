# prime number program by AiR
# date made - 27-10-2024

print("Welcome by AiR\n")
kk=int(input("What do you want\n\t1 -> If you want 'n' prime numbers, starting from 'm'\n\t2 -> If you want all prime numbers from 'm' to 'n'\n\t3 -> Prime number checker\n::: "))
print("\n")

prime = []
if kk==1:
    p = int(input("how many prime number do you want : "))
    m = int(input("where to start : "))
    counter = 1
    a=m
    # for a in range(m, 10000000):
    while a>=m:
        n = 2
        k = 1
        while a > n:
            if a % n == 0:
                k = 0
            n = n + 1

        if k != 0:
            # print(f"{a} is prime")
            prime.append(a)
            print(a)
            counter = counter + 1

        if counter == p + 1:
            break
        # print(counter)
        a=a+1

    print(prime)
elif kk==2:
    # b = int(input("how many prime number do you want : "))
    m = int(input("where to start : "))
    n = int(input("where to end : "))
    # prime = []
    # counter = 1
    for a in range(m, n):
        n = 2
        k = 1
        while a > n:
            if a % n == 0:
                k = 0
            n = n + 1

        if k != 0:
            # print(f"{a} is prime")
            prime.append(a)
            print(a)
            # counter = counter + 1

        # if counter == b + 1:
        #     break
        # print(counter)

    print(prime)
elif kk==3:
    a = int(input('Enter a +ve number for checking : '))
    n = 2
    factr = []
    k=1

    print("Entered number is divisible by : ")
    while a > n:
        if a % n == 0:
            k = 0
            factr.append(n)
            print(n)
        n = n + 1

    if a == 1:
        print(f"{a} is neither prime nor odd")
    elif k == 0:
        print(f"{a} is not prime\nbcz its divisible by {factr}")
    else:
        print(f"{a} is prime")

print("\nThanks\nByeee...!")