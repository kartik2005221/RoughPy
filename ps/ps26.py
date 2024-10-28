# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
import random

class Train:
    def BookTic(self):
        name=input("Enter Name: ")
        id=random.randint(1000, 1000000000)
        idk=int(id/7)
        # idk=random.random()
        print(f"Ticket booked, Mr. {name}\nTicket Id : {idk}\n**Note your Ticket Id for Future Reference")
    def getStation(self):
        stations = ["Delhi", "patli", "taj nagar", "rewari", "dahina", "kanina"]
        station=random.choice(stations)
        input("Enter Ticker Id: ")
        print(f"Your Train is on {station}")
    def getSeats(self):
        seat=random.randint(0,1000)
        coach=random.randint(1,40)
        input("Enter Ticket Id: ")
        print(f"Your Coach is {coach} coach \nand {seat} is the seat number.")
    def getFare(self):
        input("Enter the station\nFrom : ")
        input("To : ")
        fair=10*random.randint(1,99)
        print(f"Fair is  {fair} rupees\nPay Now to UPI:IndianRailways@UPI")

a=Train()
# a.BookTic()
k=1

while k==1:
    b = int(input(
        "\nWhich Service do you want?\n\t1 -> Book Ticket\n\t2 -> Where is my train?\n\t3 -> Where is my Seat?\n\t4 -> Get Fair\n::: "))
    if b == 1:
        a.BookTic()
    elif b == 2:
        a.getStation()
    elif b == 3:
        a.getSeats()
    elif b == 4:
        a.getFare()
    else:
        print("Invalid, Try Again")
        k=1
        continue
    k=int(input("Do You want to continue?\n\t1 -> Yes\n\t2 -> No\n::: "))
else:
    print("Quitting\nByee...")