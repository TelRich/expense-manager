import uuid 
from datetime import datetime, timezone

class Expense:
    def __init__(self, title: str, amount: float):
        """
        Initialize an expense object with a unique ID, title, amount, and timestamps.
        """
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = float(amount)
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at
        
    def update(self, title=None, amount=None):
        """
        Update the title and/or amount of the expense object and refresh the updated_at timestamp.
        """
        if title:
            self.title = title
        if amount:
            self.amount = float(amount)
        self.updated_at = datetime.now(timezone.utc)
        
    def to_dict(self):
        """
        Return the expense object as a dictionary.
        """
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
        
class ExpenseDatabase:
    def __init__(self):
        """
        Initialize an empty list to store expense objects.
        """
        self.expenses = []
        
    def add_expense(self, expense: Expense):
        """
        Add an expense object to the database.
        """
        self.expenses.append(expense)
        
    def remove_expense(self, expense_id: str):
        """
        Remove an expense object from the database by its unique ID.
        """
        self.expenses = [exp for exp in self.expenses if exp.id != expense_id]
        
    def get_expense(self, expense_id: str):
        """
        Retrieve an expense object from the database by its unique ID.
        """
        for exp in self.expenses:
            if exp.id == expense_id:
                return exp
        return None
    
    def get_expense_by_title(self, expense_title: str):
        """
        Retrieve a list of expenses object from the database by its title.
        """
        return [exp.to_dict() for exp in self.expenses if exp.title.lower() == expense_title.lower()]
    
    def to_dict(self):
        """
        Return the database as a list of dictionaries.
        """
        return [exp.to_dict() for exp in self.expenses]
    
if __name__ == "__main__":
    # Example usage of the Expense and ExpenseDatabase classes
    expense_db = ExpenseDatabase()
    
    # Add new expenses
    expense1 = Expense("Groceries", 50.0)
    expense2 = Expense("Gas", 30.0)
    expense_db.add_expense(expense1)
    expense_db.add_expense(expense2)
    
    # Update an expense
    expense1.update(title="Food", amount=60.0)
    
    # Retrieve an expense by ID
    retrieved_expense = expense_db.get_expense(expense1.id)
    if retrieved_expense:
        print(retrieved_expense.to_dict())
    
    # Retrieve expenses by title
    retrieved_expenses = expense_db.get_expense_by_title("food")
    for exp in retrieved_expenses:
        print(exp.to_dict())
    
    # Remove an expense
    expense_db.remove_expense(expense2.id)
    
    # Print all expenses in the database
    print(expense_db.to_dict())