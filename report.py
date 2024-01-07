from fpdf import FPDF
import os


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