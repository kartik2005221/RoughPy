#tip calculator

print("welcome")
bill = float(input("enter the bill : $"))
tip = int(input("enter the tip % : "))
numbr = int(input("how many persons will pay the bill : "))

bill += bill * (tip/100)
result = bill / numbr

print(f"you have to pay : {round(result, 2)}")