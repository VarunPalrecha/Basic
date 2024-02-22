import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_char = string.punctuation
selection_pass = letters + digits + special_char

while True:
    try:
        password_len = int(input("Enter the desired password length (greater than 4): "))
        if password_len <= 4:
            print("Password length must be greater than 4. Please enter a valid length.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

while True:
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        if num_passwords <= 0:
            print("Please enter a positive integer for the number of passwords.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

for _ in range(num_passwords):
    password = ''.join(secrets.choice(selection_pass) for _ in range(password_len))
    print("Generated Password:", password)
