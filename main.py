# Import necessary classes/modules from 'flat', 'report' files
from flat import Bill, Flatmate
from report import PdfReport

# Request user input for bill details, names, and days stayed for each flatmate
amount = float(input("Enter the bill amount: "))  # Get the bill amount as a floating-point number
period = input("What is the bill period? E.g. November 2023: ")  # Get the bill period

name1 = input("What is your name? ")  # Get the name of the first flatmate
days_in_house1 = int(input(f"How many days did {name1} stay in the house? "))  # Get days stayed by the first flatmate

name2 = input("What is the name of your flatmate? ")  # Get the name of the second flatmate
days_in_house_2 = int(input(f"How many days did {name2} stay in the house? "))  # Get days stayed by the second flatmate

# Create instances of the Bill and Flatmate classes using the collected data
the_bill = Bill(amount, period)  # Create a Bill instance with the provided amount and period
flatmate1 = Flatmate(name1, days_in_house1)  # Create a Flatmate instance for the first flatmate
flatmate2 = Flatmate(name2, days_in_house_2)  # Create a Flatmate instance for the second flatmate

# Calculate and display the amount each flatmate needs to pay
print(f"{name1} pays:", flatmate1.pays(the_bill, flatmate2))  # Calculate amount to be paid by the first flatmate
print(f"{name2} pays:", flatmate2.pays(the_bill, flatmate1))  # Calculate amount to be paid by the second flatmate

# Create a PDF report with the payment details for both flatmates and the bill
pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")  # Create a PDF report with the provided period as filename
pdf_report.generate(flatmate1, flatmate2, the_bill)  # Generate the PDF report with flatmates' payment details and bill info
