#bmi calculator 2.0
wt=float(input("enter weight(KG) : "))
ht=float(input("enter height(M) : "))

bmi = int(wt/(ht*ht))

if bmi <18.5:
    print("underweight")
elif bmi <25:
    print("normal weight")
elif bmi <30:
    print("overweight")
elif bmi <35:
    print("obese")
else:
    print("clinically obese")
