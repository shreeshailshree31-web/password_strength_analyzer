# 🔐 Password Strength Analyzer

## 📌 Objective

The objective of this task is to understand what makes a password strong and evaluate different passwords using password strength checking tools. This task also demonstrates how password complexity impacts security.

---

## 🛠 Tools Used

* PasswordMeter (Online Password Strength Checker)
* Python (Custom Password Strength Checker)

---

## 🔑 Passwords Tested

1. Srish@9612
2. shree123
3. Shree@123
4. Shree@2026!
5. S#r33$h@!L_2026

---

## 📊 Password Testing Results

| Password        | Score | Strength    |
| --------------- | ----- | ----------- |
| Srish@9612      | 98%   | Very Strong |
| shree123        | 37%   | Weak        |
| Shree@123       | 89%   | Very Strong |
| Shree@2026!     | 100%  | Very Strong |
| S#r33$h@!L_2026 | 100%  | Very Strong |

---

## 🔍 Observations

* Passwords with only lowercase letters and numbers are weak
* Adding uppercase letters improves password strength
* Use of special characters (symbols) increases security
* Longer passwords provide better protection
* Random and complex passwords achieve very strong ratings

---

## 🧠 Analysis

The password **"shree123"** is weak because it lacks uppercase letters and symbols, making it easy to guess using dictionary attacks.

Passwords like **"Shree@2026!"** and **"S#r33$h@!L_2026"** are very strong because they include a combination of uppercase letters, lowercase letters, numbers, and symbols. Their length and randomness make them resistant to brute force attacks.

---

## ⚠️ Common Password Attacks

* **Brute Force Attack:**
  Attempts all possible combinations to crack a password.

* **Dictionary Attack:**
  Uses a list of common passwords and words to guess credentials.

---

## 🔐 Best Practices for Strong Passwords

* Use at least 12–16 characters
* Include uppercase and lowercase letters
* Add numbers and special characters
* Avoid common words and personal information
* Use passphrases instead of simple passwords
* Enable Multi-Factor Authentication (MFA)

---

## 💡 Custom Implementation

A custom password strength checker was developed using Python to understand how password validation works internally.

### ▶️ How to Run

```bash
python password_checker.py
```

---

## 📁 Project Structure

Password-Strength-Analyzer/
│── password_checker.py
│── passwords.txt
│── README.md
│── screenshots/

---

## 🎯 Conclusion

This task helped in understanding the importance of password complexity and how strong passwords can prevent unauthorized access. It also provided insights into common attack techniques and security best practices.

---

## 🚀 Author-Srishaila_JT

Cyber Security Intern – Elevate Labs


