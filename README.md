# ⚡ FastAPI + AWS RDS PostgreSQL Demo

A simple backend built with **FastAPI (Python)** connected to a **PostgreSQL database on AWS RDS**.  
Includes endpoints to test database connectivity and fetch sample data from two tables: `dim_sources` and `dim_authors`.

---

## 🧩 Overview

| Component | Technology |
|------------|-------------|
| **Framework** | FastAPI |
| **Database** | PostgreSQL (AWS RDS) |
| **Driver** | psycopg2 |
| **Config** | configparser |
| **Language** | Python |

---

## 🚀 Features

- ✅ Test database connection (`/test-db-connection`)
- ✅ Fetch all sources (`/sources`)
- ✅ Fetch all authors (`/authors`)
- ✅ SQL seed file for easy setup
- ✅ Modular and secure config management

---

## ⚙️ Setup Instructions

### 1️⃣ Clone & Install
```bash
git clone https://github.com/ANUJ-GAUTAM26/fastapi-aws-rds-demo.git
cd fastapi-aws-rds-demo
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
2️⃣ Configure Database

Copy and edit your credentials:

```bash
copy config.ini.example config.ini
```
2️⃣ Configure Database

Then open config.ini and update it with your AWS RDS details:

```ini
[database]
host = database-1.cen2gwsiejt4.us-east-1.rds.amazonaws.com
db_name = mydb
user = postgres
password = your_password_here
```
3️⃣ Seed the Database

Run this once to create and populate the tables:

& "C:\Program Files\PostgreSQL\17\bin\psql.exe" -h database-1.cen2gwsiejt4.us-east-1.rds.amazonaws.com -U postgres -d mydb -f ".\data\seed_data.sql"

4️⃣ Run the Application
python -m uvicorn Myapi:app --reload


Now visit:

Docs → http://127.0.0.1:8000/docs

Test DB → http://127.0.0.1:8000/test-db-connection

Sources → http://127.0.0.1:8000/sources

Authors → http://127.0.0.1:8000/authors

🧪 API Endpoints
Endpoint	Description
/test-db-connection	Test RDS connectivity
/sources	List all news sources
/authors	List all authors
/docs	Interactive Swagger UI

Example Response:

{
  "status": "success",
  "message": "Successfully connected to the database."
}
🧠 What I Learned

Structuring and building APIs with FastAPI

Connecting FastAPI securely to AWS RDS

Writing SQL seed scripts and using psycopg2

Managing configurations cleanly with configparser

👨‍💻 Author

Anuj Gautam
📍 India

💼 LinkedIn: https://www.linkedin.com/in/anuj-gautam-bb0b77326/

💻 GitHub: https://github.com/ANUJ-GAUTAM26

⭐ If you found this project helpful, please consider giving it a star on GitHub!
