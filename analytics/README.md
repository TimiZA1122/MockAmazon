# MockAmazon – E-commerce Backend & Analytics Project

## Clarifications

POST Requests are used to store/submit data, on the contrary GET requests tend to retrieve information.

## Project Overview

MockAmazon Fullstack/Backend-Data Project. MockAmazon is a small e-commerce platform for purchasing amazing Seeds. It demonstrates skills in:

* DBMS: MySQL (users, products, orders, order\_items)
* Backend code: Python + SQLAlchemy
* Data analysis: Pandas, NumPy
* Visualization: Matplotlib Revenue & User Spending charts
* Optional API: FastAPI endpoints for live analytics (not yet implemented)

This is a great project for data analyst or backend developer portfolios.

## Features

* Database on MySQL with real world e-commerce tables
* Python script `analytics/run_analytics.py` that:

  * Retrieves data from the database
  * Calculates revenue per product
  * Computes total spend per user
  * Exports CSVs for further analysis
  * Generates visual charts automatically
* Optionally: FastAPI API endpoints to get analytics in real time (future improvement)

## Tech Stack

| Layer             | Technology                                                |
| ----------------- | --------------------------------------------------------- |
| Database          | MySQL                                                     |
| Backend           | Python - SQLAlchemy (uses more SQL than typical services) |
| API               | FastAPI (optional)                                        |
| Data Manipulation | Pandas, NumPy                                             |
| Visualization     | Matplotlib                                                |
| Environment       | VS Code, Python venv                                      |

## Getting Started

### 1️⃣ Clone the Repository

```bash
git clone <repo_url>
cd MockAmazon
```

### 2️⃣ Prepare Python Environment

```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# OR
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 3️⃣ Set Up the Database

Start MySQL:

```bash
brew services start mysql  # Mac users
```

Log in:

```bash
mysql -u root -p
```

Create the database:

```sql
CREATE DATABASE mock_amazon;
USE mock_amazon;
```

Create tables (or import the example SQL dump):

```sql
CREATE TABLE users (...);
CREATE TABLE products (...);
CREATE TABLE orders (...);
CREATE TABLE order_items (...);
```

Add Sample Data (Not Mandatory, but Recommended):

```sql
INSERT INTO users (...) SELECT...;
INSERT INTO products (...) VALUES (...);
INSERT INTO orders (...) VALUES (...);
INSERT INTO order_items (...) VALUES (...);
```

### 4️⃣ Configure Python Connection

In `analytics/run_analytics.py`:

```python
DB_USER = "root"
DB_PASSWORD = "zackTimmy678#"
DB_HOST = "127.0.0.1"
DB_NAME = "mock_amazon"
```

### 5️⃣ Run Analytics

```bash
python analytics/run_analytics.py
```

**What happens:**

* CSV outputs stored in: `analytics/outputs`
* Charts generated automatically (e.g., revenue per product, total spent per user)
* CSVs are Excel/Google Sheets compatible and charts can be viewed directly


```bash
uvicorn main:app --reload
```

* Access interactive API docs (Swagger) at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Try endpoints like `/top-products`, `/user-sales`, or `/low-stock`

## Project Output Examples

* CSV: Revenue by item, purchase history for users
* Charts:

  * Bar graph of product revenue
  * Bar chart of total spent per user
