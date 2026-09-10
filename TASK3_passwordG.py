import random
import string

print("===== PASSWORD GENERATOR =====")

while True:
    # --- Get a valid length safely ---
    try:
        length = int(input("\nEnter password length: "))
    except ValueError:
        print("That's not a valid number. Please enter a whole number.")
        continue

    if length <= 0:
        print("Length must be greater than 0.")
        continue

    if length < 4:
        print("Warning: very short passwords are weak. Consider 8+ characters.")

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""
    for i in range(length):
        password = password + random.choice(characters)

    print("Generated Password:", password)

    # --- Ask if the user wants another one ---
    again = input("\nGenerate another password? (y/n): ").strip().lower()
    if again != "y":
        print("Thank you for using Password Generator!")
        break