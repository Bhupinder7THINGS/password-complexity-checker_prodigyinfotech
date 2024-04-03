import re
import sys
import getpass


if  sys.platform == 'linux' or sys.platform == 'linux2':
  ('clear')

elif sys.platform == 'win32':
    system('cls')

def password_strength(password):

    if len(password) < 8:
        return "Very weak: Password is too short."
    elif len(password) >= 16:
        strength = "strong"
    elif len(password) >= 12:
        strength = "moderate"
    else:
        strength = "weak"

    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password):
        return f"Weak: Password should contain both uppercase and lowercase letters."

    if not re.search(r'\d', password):
        return f"Weak: Password should contain at least one number."

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return f"Weak: Password should contain at least one special character."

    return f"{strength} password."

password = input("Enter your password: ")
print(password_strength(password))
