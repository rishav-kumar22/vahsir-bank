# VAHSIR Bank

A terminal-based banking system built in Python while learning programming fundamentals.

This project simulates basic banking operations such as account creation, deposits, withdrawals, money transfers, transaction tracking, and administrative account management.

The goal of this project was to apply core Python concepts in a real-world style application and gain hands-on experience with problem solving, data management, and program design.

---

## Features

### Account Management
- Create new bank accounts
- Generate unique account numbers
- Store account information
- Account type selection (Savings / Current)

### Authentication
- Passkey-based account verification
- Admin authentication system
- Transaction confirmation using passkeys

### Banking Operations
- Deposit funds
- Withdraw funds
- Transfer money between accounts
- Balance validation before transactions

### Transaction Tracking
- Generate unique transaction IDs
- Record sender and receiver information
- Store transaction amount and timestamp
- View transaction history through the admin panel

### Administrative Controls
- View all account details
- Delete user accounts
- View complete transaction history
- Password-protected admin access

### Input Validation
- Numeric menu validation using try-except
- Age verification during account creation
- Balance validation
- Account existence checks
- Prevention of self-transfers

---

## Technologies Used

- Python 3
- Dictionaries
- Loops
- Functions and Control Flow
- Exception Handling
- Random Module
- Datetime Module

---

## Project Structure

```text
VAHSIR-Bank/
│
├── main.py
├── README.md
└── data/
    ├── user_data.csv
    ├── transactions.txt
    └── feedback.txt
```

---

## Sample Transaction Record

```python
{
    "Sender": "82105136516",
    "Receiver": "65114149949",
    "Amount": 2000,
    "Time": "2026-05-24 15:31:03"
}
```

---

## What I Learned

While building this project, I practiced:

- Working with nested dictionaries
- Input validation techniques
- Error handling with try-except
- Designing menu-driven applications
- Managing application state
- Using modules such as random and datetime
- Structuring larger Python programs

---

## Future Improvements

Planned upgrades include:

- File handling for permanent data storage
- Password hashing using hashlib
- SQLite database integration
- Transaction search functionality
- Account update features
- Interest calculation system
- Graphical User Interface (GUI)
- Modular project structure using functions and classes

---

## Author

**Rishav Kumar**

Built independently while learning Python and software development.

---

## License

This project is released under the MIT License.