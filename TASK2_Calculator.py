print("===== SIMPLE CALCULATOR =====")

while True:
    # --- Get first number safely ---
    try:
        num1 = float(input("\nEnter first number: "))
    except ValueError:
        print("That's not a valid number. Let's try again.")
        continue

    # --- Get second number safely ---
    try:
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("That's not a valid number. Let's try again.")
        continue

    print("\nChoose an operation:")
    print("+ for Addition")
    print("- for Subtraction")
    print("* for Multiplication")
    print("/ for Division")

    operation = input("Enter operation: ")

    result = None

    if operation == "+":
        result = num1 + num2

    elif operation == "-":
        result = num1 - num2

    elif operation == "*":
        result = num1 * num2

    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Cannot divide by zero.")

    else:
        print("Invalid operation.")

    # --- Print the result in a clean number format ---
    if result is not None:
        if result == int(result):
            # whole number -> show without decimals, e.g. 10 instead of 10.0
            print("Result =", int(result))
        else:
            # otherwise round to 2 decimal places, e.g. 3.33 instead of 3.3333333
            print("Result =", round(result, 2))

    # --- Ask if the user wants to calculate again ---
    again = input("\nCalculate again? (y/n): ").strip().lower()
    if again != "y":
        print("Thank you for using Simple Calculator!")
        break