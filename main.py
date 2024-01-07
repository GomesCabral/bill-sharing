from fpdf import FPDF

class Bill:
    """Object that contains data about a bill, such as total amount and period of the bill"""

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
    """Creates a Pdf file that contains data about the flatmates such as their names, their due amounts, and the period of the bill"""

    def __init__(self, filename):
        self.filename = filename  

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation="P", unit="pt", format="A4")  
        pdf.add_page() 

        # Title
        pdf.set_font(family="Times", size=24, style='B')  
        pdf.cell(w=0, h=80, txt="Flatmates Bill", align="C", ln=1) 

        pdf.cell(w=150, h=40, txt="Period")
        pdf.cell(w=150, h=40, txt=bill.period, ln=1)

        pdf.cell(w=150, h=40, txt=flatmate1.name)
        pdf.cell(w=150, h=40, txt=str(flatmate1.pays(bill, flatmate2)), ln=1)

        pdf.cell(w=150, h=40, txt=flatmate2.name)
        pdf.cell(w=150, h=40, txt=str(flatmate2.pays(bill, flatmate1)), ln=1)

        pdf.output(self.filename)


amount = float(input("Enter the bill amount: "))
period = input("What is the bill period? E.g. November 2023: ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stayed in the house? "))

name2 = input("What is the name of your flatmate? ")
days_in_house_2 = int(input(f"How many days did {name2} stayed in the house? "))


the_bill = Bill(amount, period) 
flatmate1 = Flatmate(name1, days_in_house1)  
flatmate2 = Flatmate(name2, days_in_house_2) 



# Printing the amounts each flatmate needs to pay individually
print(f"{name1} pays:", flatmate1.pays(the_bill, flatmate2))
print(f"{name2} pays:", flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)