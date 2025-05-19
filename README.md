# Coffee Shop Challenge
# Coffee Shop Challenge

## Overview
This project implements a simple coffee shop ordering system using Python with Object-Oriented Programming principles. It models Customers, Coffees, and Orders, along with their relationships, validations, and aggregate methods.

## Features
- **Customer class** with validation on name length and type
- **Coffee class** with validation on coffee name and immutability
- **Order class** linking Customers and Coffees with price validation
- Tracks all orders globally for reporting
- Methods to retrieve customer orders, coffees, and most frequent or highest-spending customers
- Average price calculations for coffees
- Comprehensive unit tests covering all core functionality and edge cases

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/coffee-shop-challenge.git
   cd coffee-shop-challenge

   Usage
Run the debug script to see example tests and outputs:

bash
Copy code
python debug.py
Run all unit tests:

bash
Copy code
python -m unittest discover -s tests -v
Run a specific test file:

bash
Copy code
python -m unittest tests.test_customer
Project Structure
pgsql
Copy code
coffee-shop-challenge/
├── coffee.py
├── customer.py
├── order.py
├── debug.py
├── tests/
│   ├── test_customer.py
│   ├── test_coffee.py
│   └── test_order.py
└── README.md
Testing
Unit tests cover:

Input validations (name lengths, types, price ranges)

Immutability of coffee names

Relationships between orders, customers, and coffees

Aggregation methods like average price and most aficionado customer

Run tests using:

bash
Copy code
python -m unittest discover -s tests -v
Author
Samuel [Simion]

License
This project is licensed under the MIT License. See the LICENSE file for details.



