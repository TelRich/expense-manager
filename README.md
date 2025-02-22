# Expense Manager

## Project Description
The **Expense Manager** project is a Python-based application designed to help users track and manage their financial expenses. It follows Object-Oriented Programming (OOP) principles and includes two core classes:

1. **Expense Class**: Represents an individual financial expense with attributes such as a unique ID, title, amount, and timestamps.
2. **ExpenseDatabase Class**: Manages a collection of expenses, allowing users to add, remove, and retrieve expenses.

## Features
- Add new expenses with a unique ID, title, amount, and timestamps.
- Update expenses (title and/or amount) while refreshing the last updated timestamp.
- Retrieve expenses by ID or title.
- Remove expenses from the database.
- Convert expense records into a dictionary format for easy data handling.

## How to Clone the Repository
To get a local copy of the project, follow these steps:

```sh
# Open a terminal and navigate to your desired directory

# Clone the repository
git clone https://github.com/TelRich/expense-manager.git

# Change to the project directory
cd expense-manager
```

## How to Run the Code
Ensure you have Python installed (version 3.6 or later recommended). Then, run the following commands:

```sh
# Run the Python script
python expense_manager.py
```

## Example Usage
Here's an example of how to use the Expense Manager:

```python
from expense_manager import Expense, ExpenseDatabase

db = ExpenseDatabase()

# Create expenses
expense1 = Expense("Groceries", 50.25)
expense2 = Expense("Transport", 15.00)

# Add expenses to the database
db.add_expense(expense1)
db.add_expense(expense2)

# Print all expenses
print(db.to_dict())
```

## License
This project is open-source and available for personal and educational use.

## Author
Developed by **Goodrich Okoro**

## Contributing
Feel free to submit issues or pull requests to improve this project.
