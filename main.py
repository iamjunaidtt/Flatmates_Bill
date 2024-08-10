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

    def generate(self,flatmate1,flatmate2):
        pass


bill = Bill(amount=120,period="March 2020")
junaid = Flatmate(name="Junaid",days_in_house=30)
shabeeb = Flatmate(name="Shabeeb",days_in_house=20)

print(f"Junaid pays : {junaid.pays(bill=bill,flatmate2=shabeeb)}")
print(f"Shabeeb pays : {shabeeb.pays(bill=bill,flatmate2=junaid)}")
