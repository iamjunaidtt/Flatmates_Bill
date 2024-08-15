from flat import Bill, Flatmate
from report import PdfReport

amt = float(input("Hey enter the bill amount: "))
period = input("What is the bill period :  Eg- December 2020")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill period? "))
name2 = input("What is your name other person")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period? "))

bill = Bill(amount=amt, period=period)
flatmate1 = Flatmate(name=name1, days_in_house=days_in_house1)
flatmate2 = Flatmate(name=name2, days_in_house=days_in_house2)

print(f"{flatmate1.name} pays : {flatmate1.pays(bill=bill, flatmate2=flatmate2)}")
print(f"{flatmate2.name} pays : {flatmate2.pays(bill=bill, flatmate2=flatmate1)}")

report = PdfReport(f'{bill.period}.pdf')
report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=bill)
