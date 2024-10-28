# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    def reveal(self):
        print(f"Name : {self.name} \nSalary : {self.salary} \nCompany : {self.company}")

kartik=Programmer("kartik", "1Cr")

himanshu=Programmer("Himanshu", "2Cr")

anuj=Programmer("anuj", "50L")

kartik.reveal()