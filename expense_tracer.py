import os

# expense_list = []
expense_list = [
    {"expense_type": "Rice", "amount": 1200.0, "category": "Food & Groceries"},
    {"expense_type": "Milk", "amount": 180.0, "category": "Food & Groceries"},
    {"expense_type": "Bus Pass", "amount": 500.0, "category": "Transport"},
    {"expense_type": "Petrol", "amount": 1500.0, "category": "Transport"},
    {"expense_type": "Monthly Rent", "amount": 12000.0, "category": "Rent / Housing"},
    {
        "expense_type": "Electricity Bill",
        "amount": 850.0,
        "category": "Bills & Utilities",
    },
    {
        "expense_type": "Internet Recharge",
        "amount": 999.0,
        "category": "Bills & Utilities",
    },
    {
        "expense_type": "Doctor Visit",
        "amount": 600.0,
        "category": "Healthcare / Medical",
    },
    {"expense_type": "Movie Ticket", "amount": 350.0, "category": "Entertainment"},
    {
        "expense_type": "Python Course",
        "amount": 2000.0,
        "category": "Education / Learning",
    },
    {"expense_type": "Jeans", "amount": 1800.0, "category": "Shopping / Clothing"},
    {"expense_type": "Weekend Trip", "amount": 4500.0, "category": "Travel / Vacation"},
    {
        "expense_type": "Mutual Fund SIP",
        "amount": 3000.0,
        "category": "Savings / Investments",
    },
    {"expense_type": "Gift", "amount": 700.0, "category": "Miscellaneous / Others"},
]


def add_expense(expense):

    categories = [
        "Food & Groceries",
        "Transport",
        "Rent / Housing",
        "Bills & Utilities",
        "Healthcare / Medical",
        "Entertainment",
        "Education / Learning",
        "Shopping / Clothing",
        "Travel / Vacation",
        "Savings / Investments",
        "Miscellaneous / Others",
    ]

    while True:
        print()
        print("=" * 30)
        print("Add Expense")
        print("=" * 30)
        for i, cat in enumerate(categories, 1):
            print(f"{i}: {cat}")
        print("-" * 30)
        try:
            choice = int(
                input("Enter A Number To Choose A Category. To Go Back Enter '0': ")
            )
            if choice == 0:
                break
            if 1 <= choice <= len(categories):
                category_choice = categories[choice - 1]
                while True:
                    try:
                        type = input(
                            f"\nType of {category_choice}. To Go Back type 'yes': "
                        )

                        if type.lower() == "yes":
                            break

                        amount = float(
                            input("\nEnter Amount Spent or Enter 0 to go back: ")
                        )
                        if amount == 0:
                            break

                        category_expense = {
                            "type": type,
                            "amount": amount,
                            "category": category_choice,
                        }
                        expense_list.append(category_expense)

                    except ValueError:
                        print("enter a valid number")
            else:
                raise ValueError
        except ValueError:
            print("plese enter a valid number: 1-11")


def all_expenses(expense_list):
    coun_width = len(str(len(expense_list)))
    category_width = max(len(e["category"]) for e in expense_list)
    type_width = max(len(t["expense_type"]) for t in expense_list)
    amount_width = max(len(f"{e['amount']:.2f}") for e in expense_list)
    columns = 4
    column_padding = 3
    total_padding = columns * column_padding
    total_width = (
        coun_width + category_width + type_width + amount_width + total_padding
    )
    dashes = "-" * total_width

    print("All Expenses:")
    print(dashes)
    print(
        "NO".ljust(coun_width)
        + "|".center(column_padding)
        + "Category".ljust(category_width)
        + "|".center(column_padding)
        + "Type".ljust(type_width)
        + "|".center(column_padding)
        + "Amount".ljust(amount_width)
    )
    print(dashes)
    while True:
        for i, expense in enumerate(expense_list, 1):
            print(
                f"{i:<{coun_width}}{'|':^{column_padding}}{expense["category"]:<{category_width}}{'|':^{column_padding}}{expense["expense_type"]:<{type_width}}{'|':^{column_padding}}{expense["amount"]:>{amount_width}.2f} "
            )
        print(dashes)
        total = sum(a["amount"] for a in expense_list)
        print(f"Total Expense: {total:.2f}")
        print(dashes)

        user_input = input("To Go Back Enter 'yes': ")
        if user_input.lower() == "yes":
            break


def expenses_category(expense_list):
    category_expense_amt = {}

    for expense in expense_list:
        if expense["category"] not in category_expense_amt:
            category_expense_amt[expense["category"]] = expense["amount"]
        else:
            category_expense_amt[expense["category"]] = (
                category_expense_amt.get(expense["category"]) + expense["amount"]
            )

    category_width = max(len(elem) for elem in category_expense_amt.keys())
    amt_width = max(len(f"{elem:.2f}") for elem in category_expense_amt.values())
    padding = 3
    total_width = category_width + amt_width + padding
    dash = "-" * total_width
    while True:
        print()
        print("View Expenses By Category:")
        print(dash)
        for cat, amt in category_expense_amt.items():
            print(f"{cat:<{category_width}}{"|":^{padding}}{amt:>{amt_width}.2f}")

        user_input = input("To Go Back To Main Menu Enter 'yes' or 'y': ")
        if user_input.lower() == "yes" or user_input.lower() == "y":
            break


def main_menu():

    menu_items = [
        "Add New Expense",
        "View All Expenses",
        "View Expenses by Category",
        "View Expenses by Date",
        "Edit an Expense",
        "Delete an Expense",
        "View Total Expenses",
        "Set Budget",
        "Generate Summary Report",
        "Reset / Clear All Data",
        "Exit",
    ]

    functions = {1: add_expense, 2: all_expenses, 3: expenses_category}

    while True:
        print("=" * 30)
        print("Expense Calculator")
        print("=" * 30)
        for i, item in enumerate(menu_items, 1):
            print(f"{i}: {item}")
        print("-" * 30)

        try:
            choice = int(input("Enter A Number 1-11 To Enter A Menu Item.: "))

            if choice == 11:
                os.system("cls" if os.name == "nt" else "clear")
                print("!!!Thank You For Using Expense Tracker. Have A Nice Day!!!")
                return

            if 1 <= choice <= len(menu_items):
                functions[choice](expense_list)
            else:
                raise ValueError

        except ValueError:
            print("Enter A Valid Number: 1-11")


main_menu()
