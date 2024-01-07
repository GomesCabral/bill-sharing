# Import necessary module
from fpdf import FPDF

# Class to represent a bill
class Bill:
    """Object that contains data about a bill, such as total amount and period of the bill"""

    def __init__(self, amount, period):
        self.amount = amount  # Total amount of the bill
        self.period = period  # Period for which the bill is generated

# Class to represent a flatmate
class Flatmate:
    """Create a flatmate person who lives in the flat and pays a share of the bill"""

    def __init__(self, name, days_in_house):
        self.name = name  # Name of the flatmate
        self.days_in_house = days_in_house  # Number of days the flatmate lived in the house

    # Calculate the share to pay for the bill based on the number of days in the house
    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)  # Calculate weight
        to_pay = bill.amount * weight  # Calculate amount to pay based on the weight
        return f"{round(to_pay, 2)}£"  # Return the amount to pay as a string

# Class to generate a PDF report
class PdfReport:
    """Creates a Pdf file that contains data about the flatmates such as their names, their due amounts, and the period of the bill"""

    def __init__(self, filename):
        self.filename = filename  # Filename for the PDF report

    # Generate the PDF report with flatmates' details and bill information
    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation="P", unit="pt", format="A4")  # Create a PDF object
        pdf.add_page()  # Add a page to the PDF

        # Title
        pdf.set_font(family="Times", size=24, style='B')  # Set font properties
        pdf.cell(w=0, h=80, txt="Flatmates Bill", align="C", ln=1)  # Add title to the PDF

        # Period and value of the bill
        pdf.cell(w=150, h=40, txt="Period")
        pdf.cell(w=150, h=40, txt=bill.period, ln=1)

        # Name and amount of the first flatmate
        pdf.cell(w=150, h=40, txt=flatmate1.name)
        pdf.cell(w=150, h=40, txt=str(flatmate1.pays(bill, flatmate2)), ln=1)

        # Name and amount of the second flatmate
        pdf.cell(w=150, h=40, txt=flatmate2.name)
        pdf.cell(w=150, h=40, txt=str(flatmate2.pays(bill, flatmate1)), ln=1)

        pdf.output(self.filename)  # Output the generated PDF with the provided filename

# Creating instances and generating the report
the_bill = Bill(amount=120, period="November 2023")  # Creating a Bill object
john = Flatmate(name="John", days_in_house=20)  # Creating a Flatmate object for John
mary = Flatmate(name="Mary", days_in_house=25)  # Creating a Flatmate object for Mary

pdf_report = PdfReport(filename="Report.pdf")  # Creating a PdfReport object with filename
pdf_report.generate(flatmate1=john, flatmate2=mary, bill=the_bill)  # Generating the PDF report

# Printing the amounts each flatmate needs to pay individually
print("John pays:", john.pays(bill=the_bill, flatmate2=mary))
print("Mary pays:", mary.pays(bill=the_bill, flatmate2=john))