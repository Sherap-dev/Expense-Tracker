import os
from datetime import datetime

# expense_list = []
expense_list = [
    {
        "expense_type": "Rice",
        "amount": 1200.0,
        "category": "Food & Groceries",
        "date": "2026-01-02",
    },
    {
        "expense_type": "Milk",
        "amount": 180.0,
        "category": "Food & Groceries",
        "date": "2026-01-03",
    },
    {
        "expense_type": "Bus Pass",
        "amount": 500.0,
        "category": "Transport",
        "date": "2026-01-01",
    },
    {
        "expense_type": "Petrol",
        "amount": 1500.0,
        "category": "Transport",
        "date": "2026-01-06",
    },
    {
        "expense_type": "Monthly Rent",
        "amount": 12000.0,
        "category": "Rent / Housing",
        "date": "2026-01-01",
    },
    {
        "expense_type": "Electricity Bill",
        "amount": 850.0,
        "category": "Bills & Utilities",
        "date": "2026-01-05",
    },
    {
        "expense_type": "Internet Recharge",
        "amount": 999.0,
        "category": "Bills & Utilities",
        "date": "2026-01-10",
    },
    {
        "expense_type": "Doctor Visit",
        "amount": 600.0,
        "category": "Healthcare / Medical",
        "date": "2026-01-08",
    },
    {
        "expense_type": "Movie Ticket",
        "amount": 350.0,
        "category": "Entertainment",
        "date": "2026-01-12",
    },
    {
        "expense_type": "Python Course",
        "amount": 2000.0,
        "category": "Education / Learning",
        "date": "2026-01-15",
    },
    {
        "expense_type": "Jeans",
        "amount": 1800.0,
        "category": "Shopping / Clothing",
        "date": "2026-01-18",
    },
    {
        "expense_type": "Weekend Trip",
        "amount": 4500.0,
        "category": "Travel / Vacation",
        "date": "2026-01-20",
    },
    {
        "expense_type": "Mutual Fund SIP",
        "amount": 3000.0,
        "category": "Savings / Investments",
        "date": "2026-01-25",
    },
    {
        "expense_type": "Gift",
        "amount": 700.0,
        "category": "Miscellaneous / Others",
        "date": "2026-01-28",
    },
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
            choice = int(input("Enter A Number To Choose A Category. To Go Back Enter '0': "))
            if choice == 0:
                break
            if 1 <= choice <= len(categories):
                category_choice = categories[choice - 1]
                while True:
                    try:
                        dates = input(f"\nType The Date Of This Expense in YYYY-MM-DD. To Go Back Enter 'yes': ")
                        if dates.lower() == "yes":
                            break
                        try:
                            datetime.strptime(dates, "%Y-%m-%d")
                        except ValueError:
                            print("Please Enter A Valid Date In 'YYYY-MM-DD' Format.")
                            continue

                        type = input(f"\nType of {category_choice}. To Go Back type 'yes': ")
                        if type.lower() == "yes":
                            break

                        amount = float(input("\nEnter Amount Spent or Enter 0 to go back: "))
                        if amount == 0:
                            print(expense_list)
                            break

                        category_expense = {"type": type, "amount": amount, "category": category_choice, "date": dates}
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
    dates_width = len("yyyy-mm-dd")
    columns = 5
    column_padding = 3
    total_padding = columns * column_padding
    total_width = coun_width + category_width + type_width + dates_width + amount_width + total_padding
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
        + "Dates".ljust(dates_width)
        + "|".center(column_padding)
        + "Amount".ljust(amount_width)
    )
    print(dashes)
    while True:
        for i, expense in enumerate(expense_list, 1):
            print(
                f"{i:<{coun_width}}{'|':^{column_padding}}{expense["category"]:<{category_width}}{'|':^{column_padding}}{expense["expense_type"]:<{type_width}}{'|':^{column_padding}}{expense["date"]:<{dates_width}}{'|':^{column_padding}}{expense["amount"]:>{amount_width}.2f} "
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


def expense_by_date(expense_list):
    dates = {}
    while True:
        for expense in expense_list:
            # building dict. amount of the same dates gets calculated
            if expense["date"] not in dates:
                dates[expense["date"]] = expense["amount"]
            else:
                dates[expense["date"]] += expense["amount"]
            # sorting based on the dates in ascending order
        sorted_dict = dict(sorted(dates.items()))
        dates_width = max(len(d) for d in sorted_dict.keys())
        amount_width = max(len(f"{a:.2f}") for a in sorted_dict.values())
        padding = 3
        total_width = dates_width + amount_width + padding

        print("Expenses By Dates:")
        print("=" * total_width)
        print(f"{'Dates':<{dates_width}}{'|':^{padding}}{'Amount':<{amount_width}}")
        print("-" * total_width)

        for i, d in enumerate(sorted_dict.items()):
            date = d[0]
            amount = d[1]
            print(f"{date:<{dates_width}}{'|':^{padding}}{amount:>{amount_width}.2f}")
        print("-" * total_width)
        total = sum(t for t in sorted_dict.values())
        print(f"Total Expense: {total:.2f}")
        user_input = input("To Return Back To Menu Enter 'yes': ")
        if user_input.lower() == "yes":
            break


def show_expenses(expense_list):
    coun_width = len(str(len(expense_list)))
    category_width = max(len(e["category"]) for e in expense_list)
    type_width = max(len(t["expense_type"]) for t in expense_list)
    amount_width = max(len(f"{e['amount']:.2f}") for e in expense_list)
    dates_width = len("yyyy-mm-dd")
    columns = 5
    column_padding = 3
    total_padding = columns * column_padding
    total_width = coun_width + category_width + type_width + dates_width + amount_width + total_padding
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
        + "Dates".ljust(dates_width)
        + "|".center(column_padding)
        + "Amount".ljust(amount_width)
    )
    print(dashes)

    for i, expense in enumerate(expense_list, 1):
        print(
            f"{i:<{coun_width}}{'|':^{column_padding}}{expense["category"]:<{category_width}}{'|':^{column_padding}}{expense["expense_type"]:<{type_width}}{'|':^{column_padding}}{expense["date"]:<{dates_width}}{'|':^{column_padding}}{expense["amount"]:>{amount_width}.2f} "
        )
    print(dashes)
    total = sum(a["amount"] for a in expense_list)
    print(f"Total Expense: {total:.2f}")
    print(dashes)


def edit_expense(expense_list):
    show_expenses(expense_list)
    print()
    while True:
        try:
            expense_choice = int(input("Enter The No. Of The Expense You Would Like To Edit: "))

            if 1 <= expense_choice <= len(expense_list):
                current_choice = expense_list[expense_choice - 1]

            num_width = len(str(expense_choice))
            category_width = len(current_choice["category"])
            type_width = len(current_choice["expense_type"])
            date_width = 10
            amt_width = len(f"{current_choice["amount"]:.2f}")
            padding = 3
            total_width = category_width + type_width + date_width + amt_width + (padding * 4)
            print()
            print("What Would You Like To Edit?")
            print("-" * total_width)
            print(
                f"{'Category':<{category_width}}{'|':^{padding}}{'Type':<{type_width}}{'|':^{padding}}{'Dates':<{date_width}}{'|':^{padding}}{'Amount':<{amt_width}}"
            )
            print(
                f"{current_choice['category']:<{category_width}}{'|':^{padding}}{current_choice['expense_type']:<{type_width}}{'|':^{padding}}{current_choice['date']:<{date_width}}{'|':^{padding}}{current_choice['amount']:>{amt_width}}"
            )
            print()
            while True:
                user_choice = input("Enter The Name Of The Category To Update it: ")
                print()
                if user_choice in ["Category", "Type", "Dates"]:
                    user_update = input(
                        f"Enter The New '{user_choice}' To Update. To choose another expense to edit enter 'Yes'. To go back to main menu Enter 'Menu': "
                    )
                    print()
                    if user_update.lower() == "yes":
                        break
                    elif user_update.lower() == "menu":
                        return
                else:
                    print("Please Enter A Valid Category")
                    continue

                if user_choice == "Category":
                    current_choice["category"] = user_update
                    continue
                elif user_choice == "Type":
                    current_choice["expense_type"] = user_update
                    continue
                elif user_choice == "Dates":
                    current_choice["date"] = user_update
                    continue
                elif user_choice == "amount":
                    current_choice["amount"] = float(input("Enter The New 'Amount' to Update: "))

        except ValueError:
            print("Please Enter A Valid Number")
            continue


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

    functions = {1: add_expense, 2: all_expenses, 3: expenses_category, 4: expense_by_date, 5: edit_expense}

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
