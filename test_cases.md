# FreshCart — Manual Test Cases
# Smart Grocery Management System

## Test Environment
- Application : FreshCart (index.html)
- Browser     : Chrome / Firefox / Edge
- Version     : v1.0.0

---

## TC001 — Add Product (Valid Data)
Module   : Products
Priority : High

Steps:
1. Click "+ Add Product" button
2. Enter Name: "Apple", Category: Fruits & Vegetables
3. Enter Price: 80, Stock: 100, Unit: kg
4. Click "Save Product"

Expected : Modal closes, product appears in table
Result   : PASS

---

## TC002 — Add Product (Empty Name)
Module   : Products
Priority : High

Steps:
1. Open Add Product modal
2. Leave Name field empty
3. Fill other fields
4. Click "Save Product"

Expected : Toast error — "Please fill all required fields"
Result   : PASS

---

## TC003 — Add Product (Negative Price)
Module   : Products
Priority : Medium

Steps:
1. Open Add Product modal
2. Enter Price: -50
3. Click "Save Product"

Expected : Error shown, product NOT saved
Result   : PASS

---

## TC004 — Edit Product
Module   : Products
Priority : High

Steps:
1. Click Edit on any product
2. Change price to 90
3. Click Save Product

Expected : Table shows updated price
Result   : PASS

---

## TC005 — Delete Product
Module   : Products
Priority : High

Steps:
1. Click Delete on any product
2. Click OK on confirmation

Expected : Product removed from table
Result   : PASS

---

## TC006 — Search Product
Module   : Products
Priority : Medium

Steps:
1. Type "rice" in search box

Expected : Only rice products shown
Result   : PASS

---

## TC007 — Category Filter
Module   : Products
Priority : Medium

Steps:
1. Select "Dairy" from category dropdown

Expected : Only Dairy products shown
Result   : PASS

---

## TC008 — Update Inventory Stock
Module   : Inventory
Priority : High

Steps:
1. Go to Inventory page
2. Enter 200 in qty field for Basmati Rice
3. Click Update

Expected : Stock changes to 200
Result   : PASS

---

## TC009 — Low Stock Alert
Module   : Inventory / Dashboard
Priority : High

Steps:
1. Set a product stock to 5
2. Check topbar

Expected : "Low Stock" badge appears
Result   : PASS

---

## TC010 — Out of Stock Badge
Module   : Inventory
Priority : Medium

Steps:
1. Set product stock to 0

Expected : Status shows "Out of Stock" (red)
Result   : PASS

---

## TC011 — Add Item to Bill
Module   : Billing
Priority : High

Steps:
1. Go to Billing page
2. Select "Tomatoes", enter qty 2
3. Click Add

Expected : Item appears with correct total
Result   : PASS

---

## TC012 — Exceed Stock in Bill
Module   : Billing
Priority : High

Steps:
1. Select product with stock 5
2. Enter qty 10
3. Click Add

Expected : Error — "Only 5 available"
Result   : PASS

---

## TC013 — Generate Bill (No Customer)
Module   : Billing
Priority : High

Steps:
1. Add items to bill
2. Leave Customer Name empty
3. Click Generate Bill

Expected : Error — "Enter customer name"
Result   : PASS

---

## TC014 — Generate Bill and PDF Download
Module   : Billing
Priority : Critical

Steps:
1. Enter customer name, add items
2. Click "Generate Bill & Download PDF"
3. Open PDF

Expected : PDF downloads with all bill details, stock reduces
Result   : PASS

---

## TC015 — GST Calculation
Module   : Billing
Priority : High

Steps:
1. Add item worth Rs.100

Expected : GST shows Rs.5.00, Total shows Rs.105.00
Result   : PASS

---

## TC016 — Clear Bill
Module   : Billing
Priority : Medium

Steps:
1. Add items to bill
2. Click Clear

Expected : All items removed, form cleared
Result   : PASS

---

## TC017 — Dashboard Stats
Module   : Dashboard
Priority : High

Steps:
1. Add a product — check Total Products count
2. Generate a bill — check Bills count and Revenue

Expected : All counts update correctly
Result   : PASS

---

## TC018 — CSV Export
Module   : Reports
Priority : Medium

Steps:
1. Go to Reports page
2. Click Export CSV

Expected : CSV file downloads with bill data
Result   : PASS

---

## Test Summary

Module      | Total | Pass | Fail | Pending
------------|-------|------|------|--------
Products    |   5   |   5  |   0  |    0
Inventory   |   3   |   3  |   0  |    0
Billing     |   6   |   6  |   0  |    0
Dashboard   |   1   |   1  |   0  |    0
Reports     |   1   |   1  |   0  |    0
Search      |   2   |   2  |   0  |    0
TOTAL       |  18   |  18  |   0  |    0
