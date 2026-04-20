import re

def check_password_strength(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Strength result
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    elif score <= 6:
        return "Strong"
    else:
        return "Very Strong"


# Test passwords
passwords = [
    "password",
    "shree123",
    "Shree@123",
    "Shree@2026!",
    "S#r33$h@!L_2026",
    "Tiger$Runs@Midnight2026"
]

for pwd in passwords:
    print(pwd, "->", check_password_strength(pwd))