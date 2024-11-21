#Samantha Trejo, Password Validator

import re


def is_strong_password(password):
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False
    if not re.search(r'\d', password):
        print("Password must include at least 1 number.")
        return False
    if not re.search(r'[!@#$%^&*]', password):
        print("Password must include at least 1 special character (Examples: @, #, $, %, *, &).")
        return False
    return True


while True:
    password = input("Enter a password: ")
    if is_strong_password(password):
        print("Your password has been accepted.")
        break
    else:
        continue
