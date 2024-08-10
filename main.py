import webbrowser

from fpdf import FPDF

class Bill:
    """
    Object that contain data about the bill such as total amount and period
    of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatmate person whom lives in the flat and pays the share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill,flatmate2):
        weight = self.days_in_house/(self.days_in_house+flatmate2.days_in_house)
        return bill.amount * weight


class PdfReport:
    """
    Create a file that contains data about the flatmates such as their name, their due amount
    and period informaiton
    """

    def __init__(self,filename):
        self.filename = filename

    def generate(self,flatmate1,flatmate2,bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #add logo to the report
        pdf.image(name='house.png', w=30, h=30)

        #insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmate Bills', border=0, align="C", ln=1)

        #insert Period Label & Value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=100, h=40, txt=bill.period, border=0,ln=1)

        # Insert amount of first flatemate1
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=100, h=40, txt=str(round(flatmate2.pays(bill=bill,flatmate2=flatmate2),2)), border=0,ln=1)

        # Insert amount of first flatemate2
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=100, h=40, txt=str(round(flatmate2.pays(bill=bill, flatmate2=flatmate1), 2)), border=0, ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)



bill = Bill(amount=120,period="March 2020")
junaid = Flatmate(name="Junaid",days_in_house=30)
shabeeb = Flatmate(name="Shabeeb",days_in_house=20)

print(f"Junaid pays : {junaid.pays(bill=bill,flatmate2=shabeeb)}")
print(f"Shabeeb pays : {shabeeb.pays(bill=bill,flatmate2=junaid)}")

report = PdfReport('Report1.pdf')
report.generate(flatmate1=junaid,flatmate2=shabeeb,bill=bill)
