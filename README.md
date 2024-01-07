# Flatmates Bill 💸

This Python script calculates and generates a bill for flatmates living together. It computes the share of the bill each flatmate owes based on the number of days they've spent in the house.

## Usage

### Installation
- Clone the repository or download the code.

### Requirements
- Python 3.x
- fpdf library

### Running the Script
1. Open your terminal.
2. Navigate to the directory where the code is saved.
3. Run the script: `python flatmates_bill.py`.

### Instructions
- The script will prompt you to input the bill amount, period, names of the flatmates, and the number of days each flatmate stayed in the house.
- After inputting the required information, the script will calculate the amount each flatmate needs to pay and generate a PDF report summarizing the bill details.

## Code Structure

### Classes
- `Bill`: Contains data about a bill, including the total amount and period.
- `Flatmate`: Represents individuals living in the flat and calculates their share of the bill.
- `PdfReport`: Generates a PDF file containing details about the flatmates, their due amounts, and the period of the bill.

### Running the Script
- The code will request user input for bill details, names, and days stayed for each flatmate.
- It then creates instances of the `Bill` and `Flatmate` classes using the collected data and calculates the amount each flatmate needs to pay.
- Finally, it generates a PDF report with payment details for both flatmates and the bill.

---

Feel free to contribute or provide feedback to enhance this script further! 🚀
