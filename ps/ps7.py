# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

a=input("Enter comment here : ")

spammess=("Make a lot of money", 'buy now', 'subscribe this', 'click this')
find=a.find(spammess)

if find>=0:
    print("Spam detected")
else:
    print("No Spam detected")