# FreshCart — Smart Grocery Management System

A real-time grocery management web application with manual and automation testing.

## How to Run

### Step 1 — Open in VS Code
1. Open VS Code
2. File → Open Folder → select smart-grocery folder

### Step 2 — Install Live Server Extension
1. Press Ctrl+Shift+X
2. Search "Live Server"
3. Install it (by Ritwick Dey)

### Step 3 — Run the App
1. Right-click on index.html
2. Click "Open with Live Server"
3. Browser opens at http://127.0.0.1:5500

---

## Run Selenium Tests

Open VS Code terminal (Ctrl + backtick) and run:

    pip install -r requirements.txt
    pytest tests/selenium/test_automation.py -v

For HTML test report:

    pytest tests/selenium/test_automation.py -v --html=report.html

---

## Project Structure

    smart-grocery/
    ├── index.html
    ├── css/
    │   └── style.css
    ├── js/
    │   └── app.js
    ├── tests/
    │   ├── manual/
    │   │   └── test_cases.md
    │   └── selenium/
    │       └── test_automation.py
    ├── requirements.txt
    └── README.md

---

## Features

- Product Management — Add, Edit, Delete, Search
- Inventory Tracking — Stock levels with color alerts
- Billing — GST calculation, PDF invoice download
- Dashboard — Live stats and low stock alerts
- Reports — Revenue summary, CSV export
- 18 Manual Test Cases
- 24 Selenium Automation Tests
