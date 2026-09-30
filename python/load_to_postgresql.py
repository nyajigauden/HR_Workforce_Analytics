import pandas as pd
from pathlib import Path
from getpass import getpass
from sqlalchemy import create_engine, text


# Project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Excel file
excel_file = BASE_DIR / "HR_Workforce_Analytics.xlsx"


print("Loading HR data from Excel...")

# Read the employee data
employees = pd.read_excel(
    excel_file,
    sheet_name="Employees",
    usecols="A:K"
)

# Rename Excel columns to PostgreSQL column names
employees = employees.rename(columns={
    "EmployeeID": "employee_id",
    "EmployeeName": "employee_name",
    "Gender": "gender",
    "Department": "department",
    "JobTitle": "job_title",
    "Region": "region",
    "Salary": "salary",
    "HireDate": "hire_date",
    "Performance": "performance",
    "Status": "status",
    "Performance Level": "performance_level"
})

# Make sure the hire date is a proper date
employees["hire_date"] = pd.to_datetime(
    employees["hire_date"],
    errors="coerce"
)

# Ask for PostgreSQL password without displaying it
password = getpass("Enter PostgreSQL password: ")

# Create PostgreSQL connection
engine = create_engine(
    "postgresql+psycopg2://",
    connect_args={
        "host": "localhost",
        "port": 5432,
        "database": "hr_workforce",
        "user": "postgres",
        "password": password
    }
)

# Test the connection
with engine.connect() as connection:
    result = connection.execute(
        text("SELECT current_database();")
    )
    database_name = result.scalar()

print(f"Connected to database: {database_name}")

# Load data into PostgreSQL
employees.to_sql(
    "employees",
    engine,
    if_exists="append",
    index=False
)

print(f"Successfully loaded {len(employees)} employees into PostgreSQL.")