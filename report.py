import webbrowser
import os

from fpdf import FPDF


class PdfReport:
    """
    Create a file that contains data about the flatmates such as their name, their due amount
    and period informaiton
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # add logo to the report
        pdf.image(name='files/house.png', w=30, h=30)

        # insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmate Bills', border=0, align="C", ln=1)

        # insert Period Label & Value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=100, h=40, txt=bill.period, border=0, ln=1)

        # Insert amount of first flatemate1
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=100, h=40, txt=str(round(flatmate2.pays(bill=bill, flatmate2=flatmate2), 2)), border=0, ln=1)

        # Insert amount of first flatemate2
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=100, h=40, txt=str(round(flatmate2.pays(bill=bill, flatmate2=flatmate1), 2)), border=0, ln=1)

        os.chdir('files')
        pdf.output(self.filename)
        webbrowser.open(self.filename)
