import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount INTEGER,
    category TEXT
)
""")
conn.commit()

def add_expense():
    amount = int(input("Enter amount: "))
    category = input("Enter category (Food/Travel/etc): ")
    
    cursor.execute("INSERT INTO expenses (amount, category) VALUES (?, ?)", (amount, category))
    conn.commit()
    print("✅ Expense added")

def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    
    print("\n--- All Expenses ---")
    for row in rows:
        print(row)

def show_chart():
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = cursor.fetchall()
    
    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]
    
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title("Expense Distribution")
    plt.show()

def menu():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Show Chart")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            show_chart()
        elif choice == '4':
            break
        else:
            print("Invalid choice")

menu()
