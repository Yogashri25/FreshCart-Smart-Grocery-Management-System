# 🛒 FreshCart — Grocery Management System

A full-stack grocery store management system built to digitize daily shop operations — product management, inventory tracking, billing, and sales reporting — with a strong focus on software testing and quality assurance.

---

## 📖 Overview

FreshCart simulates how a real grocery/supermarket shop owner runs their business digitally:

- Manage what products are sold (Rice, Milk, Tomatoes, etc.)
- Track how many items are left in stock
- Generate a customer bill with automatic GST calculation
- Download that bill as a PDF invoice
- View sales reports and export data to CSV

---

## ✨ Features

### 📊 Dashboard
At-a-glance summary — total products, total revenue, number of bills generated, and low-stock alerts.

### 📦 Products Page
Add, edit, and delete products with name, price, and stock quantity. Includes a search bar for quick lookup.

### 🗃️ Inventory Page
Real-time stock tracking with visual alerts:
- 🟡 Yellow — low stock warning
- 🔴 Red — out of stock

Shop owners can manually update quantities here.

### 🧾 Billing Page
A digital cash counter:
- Enter customer name
- Select purchased items and quantities
- Click **Generate Bill**
- Automatically calculates **GST (5%)**
- Downloads a printable **PDF invoice** (via jsPDF)

### 📈 Reports Page
- Total revenue earned
- Number of bills generated
- Best-selling products
- Export all data to **CSV / Excel**

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Flask (Python) |
| Database | MySQL |
| PDF Generation | jsPDF |
| Data Export | CSV |
| Testing (Manual) | Manual test case documentation |
| Testing (Automated) | Selenium (Python) |

---

## 🧪 Testing

Quality assurance was a core focus of this project, not an afterthought.

- **Manual Testing** — 18 test cases covering valid and invalid inputs (empty fields, negative values, edge cases), documented in a test case table.
- **Automated Testing** — 23 Selenium (Python) test cases that simulate a real user clicking through the website, enabling fast regression testing after every code change.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- MySQL Server
- pip

### Installation
```bash
# Clone the repository
git clone https://github.com/Yogashri25/<repo-name>.git
cd <repo-name>

# Install dependencies
pip install -r requirements.txt

# Set up the MySQL database
# (import the provided schema.sql file into your MySQL instance)

# Run the app
python app.py
```

The app will be available at `http://localhost:5000` (or your configured port).

---

## 📸 Screenshots
> Add screenshots of the Dashboard, Products, Inventory, Billing, and Reports pages here.

---

## 📂 Project Structure
```
freshcart/
├── static/
│   ├── css/
│   └── js/
├── templates/
├── app.py
├── requirements.txt
├── schema.sql
└── tests/
    └── selenium_tests.py
```

## 📄 License
This project is open source and available for educational purposes.
