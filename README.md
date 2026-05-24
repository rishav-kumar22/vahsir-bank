

---

```markdown
# VAHSIR Bank — Core Banking Application & Flat-File Transaction Simulator

A terminal-based banking simulation and primitive transactional accounting engine implemented in native Python. This architecture serves as a rigorous proof-of-concept for localized file-system data persistence, explicit multi-layer input validation barriers, operational session state tracking, and procedural software design patterns.

---

## 🛠️ Technical Architecture & Engineering Metrics

This platform structures transactional workflows without relying on external third-party database frameworks or Object-Relational Mappings (ORMs). Instead, it manages low-level **flat-file data persistence streams** directly, modeling data mutations, profile state records, and multi-user interaction cycles reliably.

### Key Programmatic Highlights:
* **Algorithmic Identifier Generation**: Uses a custom string manipulation algorithm to generate unique 11-digit account identifiers. The sequence parses structural indices of a user's name, extracts components into their respective decimal **ASCII values** (e.g., `R` $\rightarrow$ `82`), truncates the buffer strings, and introduces a randomized integer salt to eliminate structural key collisions.
* **Stream-Based State Persistence**: Integrates context-managed file streams (`with open()`) across the database interface to ensure optimal file-descriptor cleanup and safe exit locks. State changes load data rows dynamically, isolate targeting indices, complete balance operations, and commit execution strings cleanly.
* **Double-Entry Balance Multi-threading**: Guarantees transaction atomicity during peer-to-peer (P2P) local account payments. The transactional routing engine maps updates securely over the database layout—simultaneously debiting the sender's data row, applying a corresponding credit mutation to the receiver's data row, and enforcing a rollback exit state if invalid parameters are matched.
* **Defensive Error Sanitization**: Guards runtime execution environments against accidental crashes or unexpected string formatting types. Dedicated try-except exception blocks catch type mismatches, enforce configuration-defined age boundaries, and parse balance values cleanly.
* **Administrative Audit Deck**: Features an isolated command console guarded behind a rigid global passkey verification. Once authenticated, administrative actions access structural file buffers directly to run complete account purges, display global data strings, and evaluate transaction history arrays.

---

## 📂 System Data Schemas

### 📊 Persistent User Ledger (`user_data.csv`)
Client profiles and active balances are consistently saved as structural string records using comma-separated attributes:
```csv
Name,Age,Type,AccountNumber,Password,Balance

```

*The engine uses native string methods (`.strip()`, `.split()`) to extract parameters reliably on runtime boot.*

### 📝 Historical Audit Logs (`transactions.txt`)

Financial adjustments and fund routing tracks are permanently written as localized map strings to track activity logs:

```python
{"Sender": "821051...", "Receiver": "651141...", "Type": "TRANSFER", "Amount": "$2000.00", "Time": "2026-05-24 15:31:03"}

```

---

## 🚀 Local Installation & Execution

To test the banking engine on your local machine, follow this initialization sequence:

### System Prerequisites

* Verify that an active installation of **Python 3.x** or higher is mapped inside your terminal environment's systemic path variables.

### Boot Sequence:

1. **Clone the Core Repository**:
```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/vahsir-bank.git](https://github.com/YOUR_GITHUB_USERNAME/vahsir-bank.git)

```


2. **Move into the Active Project Working Directory**:
```bash
cd vahsir-bank

```


3. **Execute the Primary Application Script**:
```bash
python main.py

```



---

## 📈 Optimization Roadmap (Version 2.0 Benchmarks)

Future development sprints will move these flat data structures into an enterprise-grade framework:

1. **Cryptographic Credential Obfuscation (`hashlib`)**: Migrating raw-text passwords into non-invertible **SHA-256 secure hash strings** to follow true privacy guidelines.
2. **Relational Database Migration (`sqlite3`)**: Switching plain-text file storage to indexed SQL database engines to write clean queries (`SELECT`, `UPDATE`) and prevent simultaneous access file corruption.
3. **Decoupled User Interface Separation**: Isolating core transactional math scripts into separate backend code logic modules entirely apart from terminal menu inputs.

---

## 📜 Project Metrics & Certification

* **Lead Developer**: Rishav Kumar
* **Development Cycle**: Completed & Audited in 2026.
* **Project Classification**: Open-Source Academic Evaluation Portfolio Engine. Distributed under the MIT License framework.

```

```