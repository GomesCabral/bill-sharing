from fpdf import FPDF


class Bill:
    """Object that contains data about a bill, such as totam amount and period of the bill"""

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period
        

class Flatmate:
    """Create a flatmate person who lives in the flat and pays a share of the bill"""

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return f"{round(to_pay, 2)}£"


class PdfReport:
    """Creates a Pdf file thet contains data about the flatmates such as their names, their due amounts and the period of the bill"""

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        #Title
        pdf.set_font(family="Times", size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", align="C", ln=1)

        #Period and value
        pdf.cell(w=150, h=40, txt="Period")
        pdf.cell(w=150, h=40, txt=bill.period, ln=1)

        #Name and amount of the first flatmate
        pdf.cell(w=150, h=40, txt=flatmate1.name)
        pdf.cell(w=150, h=40, txt=str(flatmate1.pays(bill, flatmate2)), ln=1)

        #Name and amount of the second flatmate
        pdf.cell(w=150, h=40, txt=flatmate2.name)
        pdf.cell(w=150, h=40, txt=str(flatmate2.pays(bill, flatmate1)), ln=1)

        pdf.output(self.filename)


the_bill = Bill(amount=120, period="November 2023")
john = Flatmate(name="john", days_in_house=20)
marry = Flatmate(name="marry", days_in_house=25)

pdf_report = PdfReport(filename="Report.pdf")
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=the_bill)

print("Jonh pays: ", john.pays(bill=the_bill, flatmate2=marry))
print("Marry pays: ", marry.pays(bill=the_bill, flatmate2=john))
