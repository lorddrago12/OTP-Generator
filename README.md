# 🔐 OTP Generator (Python)

A simple beginner-friendly **One-Time Password (OTP) Generator** built using Python. This script generates a random OTP, displays it to the user, and validates it during login.

---

## 📌 Features

* Generates a **random 6-digit OTP**
* Takes **username input**
* Verifies the entered OTP
* Displays login success or failure
* Beginner-friendly and easy to understand

---

## 🛠️ Technologies Used

* Python 3
* Built-in `random` module

---

## ▶️ How It Works

1. The program generates a random OTP.
2. The user enters their username.
3. The OTP is shown (for demo purposes).
4. The user is asked to re-enter the OTP.
5. The program checks if the OTP matches.

---

## ▶️ How to Run

1. Make sure Python is installed:

   ```bash
   python --version
   ```

2. Run the script:

   ```bash
   python OTP\ Generator.py
   ```

---

## 🧪 Example Output

```
Username: drago
Hello! drago
Here is your OTP for login 483920
Enter OTP to login: 483920
Login Successful!
```

---

## ⚠️ Important Notes

* This project is **for learning purposes only**.
* OTP is displayed in the console, which is **not secure** for real applications.
* In real-world systems, OTPs are sent via SMS, Email, or Authenticator apps.

---

## 🚀 Future Improvements

* Hide OTP from console
* Add OTP expiration timer
* Send OTP via email/SMS
* Use hashing for OTP verification
* GUI version using Tkinter or CustomTkinter

---
