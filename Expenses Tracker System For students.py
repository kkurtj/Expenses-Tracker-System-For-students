users = {}

expenses = {}

current_user = None

print("•Group 5's SIMPLE EXPENSE TRACKER•")

while True:

    while current_user is None:
        print("\nMain Menu")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose (1-3): ")

        if choice == "1":
            print("\n=== Register ===")
            username = input("Enter new username: ")

            if username in users:
                print("Username already taken.\n")
            else:
                password = input("Enter new password: ")
                users[username] = password
                expenses[username] = {}
                print("Account created successfully!\n")

        elif choice == "2":
            print("\n=== Login ===")
            username = input("Username: ")
            password = input("Password: ")

            if username in users and users[username] == password:
                current_user = username
                print(f"Welcome, {current_user}!\n")
            else:
                print("Incorrect username or password.\n")
        elif choice == "3":
            print("Goodbye!")
            exit()

        else:
            print("Invalid choice.\n")

    print(f"\nHello, : {current_user}")
    print("1. Add Expense")
    print("2. View Weekly Report")
    print("3. Logout")

    choice = input("Choose (1-3): ")

    if choice == "1":
        print("\n=== Add Expense ===")
        category = input("Enter category (e.g., Food, Things): ")

        try:
            amount = float(input("Enter amount: ₱"))
        except:
            print("Invalid amount.\n")
            continue

        if category in expenses[current_user]:
            expenses[current_user][category] += amount
        else:
            expenses[current_user][category] = amount

        print("Expense added!\n")

    elif choice == "2":
        print("\n=== Weekly Expense Report ===")
        if not expenses[current_user]:
            print("No expenses yet.\n")
        else:
            total = 0
            for cat, amt in expenses[current_user].items():
                print(f"{cat}: ₱{amt:.2f}")
                total += amt
            print("--------------------------")
            print(f"Total Weekly Expenses: ₱{total:.2f}\n")

    elif choice == "3":
        print("Logged out.\n")
        current_user = None

    else:
        print("Invalid choice.\n")