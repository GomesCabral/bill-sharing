# Flatmates Bill Calculator 💰💡

This Python script allows you to calculate and generate a bill for flatmates living together. It helps compute the share of the bill each flatmate owes based on the number of days they've spent in the house.

## Usage 🚀

### Setup
1. Clone the repository or download the code.

### Requirements 🛠️
- Python 3.x
- Libraries: fpdf

### Running the Script 🏡
1. Open your terminal.
2. Navigate to the directory where the code is saved.
3. Run the script: `python main.py`.

### Instructions 📝
- The script prompts you to input the bill amount, period, names of the flatmates, and the number of days each flatmate stayed in the house.
- After inputting the required information, the script calculates the amount each flatmate needs to pay.
- It generates a PDF report summarizing the bill details with payment information for both flatmates and the bill itself.

## Code Structure 🧱

### Classes and Functionality 🏠
- `Bill`: Holds data about a bill, including the total amount and period.
- `Flatmate`: Represents individuals in the flat, calculating their share of the bill based on days stayed.
- `PdfReport`: Generates a PDF file detailing flatmates' due amounts and the bill's period.

### Running the Script 🔄
- The code collects user input for bill details and flatmates' information.
- It creates instances of the `Bill` and `Flatmate` classes using the collected data.
- Calculates and displays the amount each flatmate needs to pay.
- Generates a PDF report with payment details for both flatmates and the bill.

---

Contributions and feedback are welcome to enhance this script! Feel free to explore and improve it further! 🛠️
