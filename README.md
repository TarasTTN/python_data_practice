# 🧊 Smart Inventory Tracker (Python)

A pure Python inventory management script to track item quantities, parse natural language inputs, and monitor expiration dates. 

This project was built to practice core Python data structures, type hinting, and precise floating-point arithmetic.

## 🛠 Tech Stack
- **Language:** Python 3.12+
- **Libraries:** `datetime` (time-series filtering), `decimal` (financial/precise arithmetic), `typing` (static type hints).

## 🚀 Features
- **Natural Language Parsing:** The `add_by_note` function extracts item names, amounts, and dates from raw string inputs (e.g., `"Milk 2 2026-10-15"`).
- **Precision Math:** Uses Python's `Decimal` module instead of standard floats to prevent floating-point rounding errors when aggregating amounts.
- **Expiration Tracking:** Calculates expiring batches dynamically using `timedelta`.
- **Fuzzy Search:** Case-insensitive search across the inventory dictionary.

## 💻 Quickstart
```bash
git clone git@github.com:TarasTTN/python_data_practice.git
cd python_data_practice/01_python_basics
python3 inventory_tracker.py