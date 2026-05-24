
````markdown
# VAHSIR Bank

A terminal-based banking management system built in Python as part of my learning journey in software development.

VAHSIR Bank simulates core banking operations such as account creation, authentication, deposits, withdrawals, balance management, money transfers, transaction logging, and administrative controls. The project was designed and implemented independently using Python fundamentals, with a strong focus on problem-solving, file handling, data persistence, and application design.

---

## Overview

This project demonstrates how real-world banking workflows can be modeled using Python without external frameworks or databases.

Instead of relying on advanced libraries, the system uses:

- Native Python
- CSV-based data storage
- Text-based transaction logging
- Menu-driven interaction
- File handling for persistent records
- Authentication and validation mechanisms

The primary objective was to apply programming concepts to a practical project while developing a deeper understanding of software design and data management.

---

## Features

### Account Management
- Create new customer accounts
- Generate unique account numbers automatically
- Support for Savings and Current accounts
- Store account information persistently

### Authentication & Security
- Account login verification using passkeys
- Password confirmation before sensitive operations
- Admin authentication system
- Validation of account ownership before transactions

### Banking Operations
- Deposit funds
- Withdraw funds
- Transfer money between accounts
- Balance verification before processing transactions
- Prevention of self-transfers

### Transaction Logging
- Automatic transaction recording
- Unique transaction ID generation
- Timestamp tracking using Python's datetime module
- Sender and receiver tracking
- Administrative transaction history viewing

### Administrative Controls
- View all registered accounts
- Delete customer accounts
- Access transaction history
- Password-protected administration panel

### Data Persistence
- User records stored in CSV format
- Transaction records stored in text files
- Feedback records stored separately
- Data remains available between program sessions

### Input Validation & Error Handling
- Numeric menu validation using try-except
- Age verification during account creation
- Account existence verification
- Balance validation checks
- Invalid input protection
- Runtime error prevention for common user mistakes

---

## Technologies Used

- Python 3
- File Handling
- CSV Data Storage
- Dictionaries
- Functions
- Loops
- Conditional Statements
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
│
└── data/
    ├── user_data.csv
    ├── transactions.txt
    └── feedback.txt
````

---

## Sample Transaction Record

```python
{
    "Sender": "82105136516",
    "Receiver": "65114149949",
    "Amount": 2000,
    "Type" : 1 
    "Time": "2026-05-24 15:31:03"
}
```

---

## Key Concepts Practiced

During the development of this project, I gained practical experience with:

* File handling and persistent storage
* Reading and writing CSV data
* Working with nested dictionaries
* Designing menu-driven applications
* Authentication systems
* Transaction processing logic
* Input validation techniques
* Exception handling
* Program modularization using functions
* Managing application state
* Using Python standard library modules

---

## Future Improvements

Planned upgrades for future versions include:

* Password hashing using `hashlib`
* SQLite database integration
* Search and filtering capabilities
* Account update and profile management
* Interest calculation system
* Transaction receipts
* Enhanced transaction reporting
* Object-Oriented Programming (OOP) redesign
* Graphical User Interface (GUI)
* Modular multi-file architecture

---

## Project Background

This project was built independently while learning Python programming fundamentals.

The goal was not only to practice syntax, but also to understand how software systems manage data, validate user actions, maintain records, and implement business logic in a structured way.

Every feature, workflow, and system design decision was implemented as part of the learning process and evolved through multiple iterations during development.

---

## Author

**Rishav Kumar**



GitHub: https://github.com/rishav-kumar22

---

## License

This project is licensed under the MIT License.

````


```markdown
## Author

Rishav Kumar

Built independently while learning Python and software development.
````

