import os
from datetime import datetime

# expense_list = []
budgets = {
    "Food & Groceries": 6000.0,
    "Transport": 3000.0,
    "Rent / Housing": 12000.0,
    "Bills & Utilities": 2500.0,
    "Healthcare / Medical": 2000.0,
    "Entertainment": 1500.0,
    "Education / Learning": 3000.0,
    "Shopping / Clothing": 2500.0,
    "Travel / Vacation": 5000.0,
    "Savings / Investments": 3000.0,
    "Miscellaneous / Others": 1000.0,
}


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

                        category_expense = {
                            "expense_type": type,
                            "amount": amount,
                            "category": category_choice,
                            "date": dates,
                        }
                        expense_list.append(category_expense)

                    except ValueError:
                        print("enter a valid number")
            else:
                raise ValueError
        except ValueError:
            print("plese enter a valid number: 1-11")


def all_expenses(expense_list):
    if len(expense_list) == 0:
        while True:
            show_expenses(expense_list)
            user_input = input('Enter "yes" to exit: ')
            if user_input == "yes":
                return
            else:
                print("'yes' to exit.")
    else:
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
                    f"{i:<{coun_width}}{'|':^{column_padding}}{expense['category']:<{category_width}}{'|':^{column_padding}}{expense['expense_type']:<{type_width}}{'|':^{column_padding}}{expense['date']:<{dates_width}}{'|':^{column_padding}}{expense['amount']:>{amount_width}.2f} "
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

    if len(expense_list) == 0:
        while True:
            show_expenses(expense_list)
            user_input = input('Enter "yes" to exit: ')
            if user_input == "yes":
                return
            else:
                print("'yes' to exit.")

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

    if len(expense_list) == 0:
        while True:
            show_expenses(expense_list)
            user_input = input("Enter 'yes' to exit: ")
            if user_input.lower() == "yes":
                return
            else:
                print("'yes' to exit.")
    else:
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

        print("\nExpenses By Dates:")
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
        while True:
            user_input = input("To Return Back To Menu Enter 'yes': ")
            if user_input.lower() == "yes":
                break
            else:
                print("Please enter the valid code to return. 'yes'.")


def show_expenses(expense_list):
    if len(expense_list) == 0:
        cat_width = len("category")
        type_width = len("Empty")
        amount_width = len("amount")
        num_width = 2
        padding = 3
        total_padding = cat_width + type_width + amount_width + num_width + (padding * 3)
        print("\nExpense List Empty!\n")
        print("-" * total_padding)
        print(
            f"{'NO':<{num_width}}{'|':^{padding}}{'Category':<{cat_width}}{'|':^{padding}}{'Type':<{type_width}}{'|':^{padding}}{'Amount':<{amount_width}}"
        )
        print("-" * total_padding)
        print(
            f"{'0':<{num_width}}{'|':^{padding}}{'Empty':<{cat_width}}{'|':^{padding}}{'Empty':<{type_width}}{'|':^{padding}}{'Empty':<{amount_width}}"
        )
        print()
    else:
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
                f"{i:<{coun_width}}{'|':^{column_padding}}{expense['category']:<{category_width}}{'|':^{column_padding}}{expense['expense_type']:<{type_width}}{'|':^{column_padding}}{expense['date']:<{dates_width}}{'|':^{column_padding}}{expense['amount']:>{amount_width}.2f} "
            )
        print(dashes)
        total = sum(a["amount"] for a in expense_list)
        print(f"Total Expense: {total:.2f}")
        print(dashes)


def current_choice_display(current_choice):

    category_width = len(current_choice["category"])
    type_width = len(current_choice["expense_type"])
    amt_width = len(f"{current_choice["amount"]:.2f}")

    if (
        len(current_choice["category"]) < len("category")
        or len(current_choice["expense_type"]) < len("type")
        or len(f"{current_choice['amount']:.2f}") < len("amount")
    ):
        category_width = len("category")
        type_width = len("type")
        amt_width = len("amount")
    date_width = 10
    padding = 3
    total_width = category_width + type_width + date_width + amt_width + (padding * 4)
    print()
    print("Expense Update")
    print("-" * total_width)
    print(
        f"{'Category':<{category_width}}{'|':^{padding}}{'Type':<{type_width}}{'|':^{padding}}{'Date':<{date_width}}{'|':^{padding}}{'Amount':<{amt_width}}"
    )
    print(
        f"{current_choice['category']:<{category_width}}{'|':^{padding}}{current_choice['expense_type']:<{type_width}}{'|':^{padding}}{current_choice['date']:<{date_width}}{'|':^{padding}}{current_choice['amount']:>{amt_width}}"
    )
    print()


def edit_delete_expense(expense_list):
    dict_key = {"category": "category", "type": "expense_type", "dates": "date"}

    if len(expense_list) == 0:
        while True:
            show_expenses(expense_list)
            print("Nothing To Edit/Delete")
            user_input = input("Enter 'yes' to exit: ")
            if user_input.lower() == "yes":
                return
            else:
                print("'yes' to exit.")

    else:
        while True:
            show_expenses(expense_list)
            print()
            try:
                expense_choice = int(
                    input(
                        "Enter The No. Of The Expense You Would Like To Edit Or Delete. To Go Back To Main Menu Enter '0': "
                    )
                )

                if expense_choice == 0:
                    return

                if 1 <= expense_choice <= len(expense_list):
                    current_choice = expense_list[expense_choice - 1]
                else:
                    print("Enter A Valid Number")
                    continue
                current_choice_display(current_choice)

                while True:

                    user_choice = input(
                        "Enter 'del' To Delete This Expense Or Enter The Name Of The Category To Update it. Enter 'list' To View All The Expenses: "
                    ).lower()
                    print()
                    if user_choice == "del":
                        print("!!Warning Deletion Is Not Undoable!!")
                        print()
                        user_input = input(
                            "Are You Sure You Want to Delete This Entry? Enter 'yes' to delete 'no' to go back: "
                        )
                        if user_input == "yes":
                            expense_list.remove(current_choice)
                            print("\nEntry Deleted\n")
                            break
                        elif user_input == "no":
                            break
                        else:
                            print("Please Enter A Valid confirmation key. 'yes' or 'no'")
                            continue

                    if user_choice == "list":
                        # show_expenses(expense_list)
                        break

                    if user_choice in dict_key:
                        key = dict_key[user_choice]
                        user_update = input(
                            f"Enter The New '{user_choice.title()}' To Update. To choose another expense to edit enter 'Yes'. To go back to main menu Enter 'Menu': "
                        )
                        print()
                        if user_update.lower() == "yes":
                            # show_expenses(expense_list)
                            break
                        elif user_update.lower() == "menu":
                            return

                        current_choice[key] = user_update.title()
                        print(f"{user_choice.title()} updated!")
                        current_choice_display(current_choice)

                    elif user_choice == "amount":
                        while True:
                            user_update = input(
                                f"Enter The New '{user_choice.title()}' To Update. To choose another expense to edit enter 'Yes'. To go back to main menu Enter 'Menu': "
                            )
                            if user_update.lower() == "yes":
                                show_expenses(expense_list)
                                break
                            elif user_update.lower() == "menu":
                                return

                            try:
                                float_test = float(user_update)
                                current_choice["amount"] = float_test
                                print(f"{user_choice.title()} updated!")
                                current_choice_display(current_choice)
                                break
                            except ValueError:
                                print("Please enter a valid amount")
                                continue
                    else:
                        print("Please Enter A Valid Category")
                        continue

            except ValueError:
                print("Please Enter A Valid Number")
                continue


def reset(expense_list):
    while True:
        show_expenses(expense_list)
        print("\n!!!Warning!!! Reset Cannot Be Undone!!\n")
        user_input = input("Are You Sure? Enter 'yes' to confirm 'no' to go back to menu: ")
        if user_input.lower() == "yes":
            expense_list.clear()
        elif user_input.lower() == "no":
            return
        else:
            print("Enter a valid confirmation. 'yes' or 'no'")

        while True:
            print("\nList Resetted")
            show_expenses(expense_list)
            _input = input("Enter 'yes' to exit: ")
            if _input.lower() == "yes":
                return


def view_total_expense(expense_list):
    all_expenses(expense_list)


def set_budget(expense_list):
    budget_category = [
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
        "View Budget",
    ]
    while True:
        category_width = max(len(c) for c in budget_category)
        print("=" * category_width)
        print("Set Budget:")
        print("=" * category_width)
        print("categories:")
        print("-" * category_width)
        for i, cat in enumerate(budget_category, 1):
            print(f"{i}: {cat}")
        try:
            budget_choice = int(
                input(
                    "\nEnter The No. Of The Category From The List To Set The Budget Of, Enter '0' To Go Back To Main Menu: "
                )
            )
            if budget_choice == 0:
                return

            if not (1 <= budget_choice <= len(budget_category)):
                print("Enter A Valid No. From The List")
                continue
            else:
                category_choice = budget_category[budget_choice - 1]

            if category_choice == "View Budget":
                while True:
                    if not budgets:
                        print("\n!!!No Budget Set Yet!!!\n")
                        break
                    else:
                        cat_width = max(len(c) for c in budgets.keys())
                        amount_width = max(len(f"{a:.2f}") for a in budgets.values())
                        padding = 3
                        total_Width = cat_width + amount_width + padding
                        print("Budget:")
                        print("-" * total_Width)
                        print(f"{'Category':<{cat_width}}{'|':^{padding}}{'Amount':^{amount_width}}")
                        print("-" * total_Width)
                        for b, a in budgets.items():
                            print(f"{b:<{cat_width}}{'|':^{padding}}{a:>{amount_width}.2f}")

                        user_input = input(
                            "\nEnter 'budget' To Go Back To Set Budget, Enter 'main menu' To Go Back To Main Menu: "
                        )

                        if user_input.lower() == "budget":
                            break
                        elif user_input.lower() == "main menu":
                            return
                        else:
                            print("Enter A Valid Choice.")
            else:
                header = "Set Budget For"
                total_Width = len(category_choice) + len(header)
                print(f"\n{header} {category_choice}")
                print("-" * total_Width)

                while True:
                    try:
                        budget = float(input(f"Please Enter The Budget For {category_choice}: "))
                        if budget < 0:
                            print("Budget Amount Cannot Be Negative.")
                            continue
                        else:
                            budgets[category_choice] = budget
                            print("Budget Added")
                            break
                    except ValueError:
                        print("Please Enter A Valid Value.")
        except ValueError:
            print("Enter A Valid Number.")


def summary_report(expense_list):
    spent_per_category = {}
    # aggrigating the amount
    for expense in expense_list:
        category = expense["category"]
        amount = expense["amount"]

        if category not in spent_per_category:
            spent_per_category[category] = 0

        spent_per_category[category] += amount
    # building the nested dictionary
    summary = {}
    for category, budget in budgets.items():
        summary[category] = {"spent": spent_per_category.get(category, 0), "budget": budget}

    total_spent = 0
    total_budget = 0
    budget_usage = {}  # budget usage storing
    for cat, elems in summary.items():
        spent = elems["spent"]
        buds = elems["budget"]

        total_spent += spent
        total_budget += buds

        if buds != 0:
            budget_usage[cat] = (spent / buds) * 100  # budget usage calculation
        else:
            budget_usage[cat] = 0

    overall_usage = (total_spent / total_budget) * 100  # overall average budger usage calculation

    category_width = max(len(c) for c in summary.keys())
    spent_width = len(f"{total_spent:.2f}")
    budget_width = len(f"{total_budget:.2f}")
    budget_usage_width = len("budget usage")
    padding = 3
    total_width = category_width + spent_width + budget_width + budget_usage_width + (padding * 4)

    print("=" * total_width)
    print("Summary Report:")
    print("=" * total_width)
    print(
        f"{'Category':<{category_width}}{'|':^{padding}}{'Spent':^{spent_width}}{'|':^{padding}}{'Budget':^{budget_width}}{'|':^{padding}}{'Budget Usage':^{budget_usage_width}}"
    )
    print("-" * total_width)

    for cat, elems in summary.items():
        spent = elems["spent"]
        budget = elems["budget"]
        print(
            f"{cat:<{category_width}}{'|':^{padding}}{spent:>{spent_width}.2f}{'|':^{padding}}{budget:>{budget_width}.2f}{'|':^{padding}}{budget_usage[cat]:>{budget_usage_width}.2f} %"
        )
    print("-" * total_width)
    print(f"Total Spent: {total_spent}\nTotal budget: {total_budget}\nOverall Budget Usage: {overall_usage:.2f} %\n")
    user_input = input("Enter Anything To Go Back: ")
    if user_input:
        return


def main_menu():

    menu_items = [
        "Add New Expense",
        "View All Expenses",
        "View Expenses by Category",
        "View Expenses by Date",
        "Edit Or Delete an Expense",
        "View Total Expenses",
        "Set Budget",
        "Generate Summary Report",
        "Reset / Clear All Data",
        "Exit",
    ]

    functions = {
        1: add_expense,
        2: all_expenses,
        3: expenses_category,
        4: expense_by_date,
        5: edit_delete_expense,
        6: view_total_expense,
        7: set_budget,
        8: summary_report,
        9: reset,
    }

    while True:
        print("=" * 30)
        print("Expense Calculator")
        print("=" * 30)
        for i, item in enumerate(menu_items, 1):
            print(f"{i}: {item}")
        print("-" * 30)

        try:
            choice = int(input("Enter A Number 1-10 To Enter A Menu Item.: "))

            if choice == 10:
                os.system("cls" if os.name == "nt" else "clear")
                print("!!!Thank You For Using Expense Tracker. Have A Nice Day!!!")
                return
            elif choice in functions:
                functions[choice](expense_list)
            else:
                raise ValueError
        except ValueError:
            print("Enter A Valid Number: 1-10")


main_menu()
