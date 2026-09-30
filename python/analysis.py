import pandas as pd
from pathlib import Path

# Project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Excel file
excel_file = BASE_DIR / "HR_Workforce_Analytics.xlsx"

# Read only the actual employee data columns A:K
employees = pd.read_excel(
    excel_file,
    sheet_name="Employees",
    usecols="A:K"
)

print("First 5 rows:")
print(employees.head())

print("\nColumn names:")
print(employees.columns.tolist())

print("\nDataset shape:")
print(employees.shape)

print("\n==============================")
print("DATA INFORMATION")
print("==============================")

print("\nData types:")
print(employees.dtypes)

print("\nMissing values:")
print(employees.isnull().sum())

print("\nDuplicate rows:")
print(employees.duplicated().sum())

print("\nBasic statistics:")
print(employees.describe())

print("\n==============================")
print("DATA CLEANING")
print("==============================")

# Remove accidental spaces from column names
employees.columns = employees.columns.str.strip()

# Remove extra spaces from text columns
text_columns = [
    "EmployeeID",
    "EmployeeName",
    "Gender",
    "Department",
    "JobTitle",
    "Region",
    "Status",
    "Performance Level"
]

for column in text_columns:
    employees[column] = employees[column].astype(str).str.strip()

# Make sure Salary is numeric
employees["Salary"] = pd.to_numeric(
    employees["Salary"],
    errors="coerce"
)

# Make sure Performance is numeric
employees["Performance"] = pd.to_numeric(
    employees["Performance"],
    errors="coerce"
)

# Make sure HireDate is a proper date
employees["HireDate"] = pd.to_datetime(
    employees["HireDate"],
    errors="coerce"
)

print("Data cleaning completed.")

print("\nMissing values after cleaning:")
print(employees.isnull().sum())

print("\n==============================")
print("HR KEY METRICS")
print("==============================")

# Total number of employees
total_employees = employees["EmployeeID"].count()

# Total payroll
total_payroll = employees["Salary"].sum()

# Average salary
average_salary = employees["Salary"].mean()

# Minimum salary
minimum_salary = employees["Salary"].min()

# Maximum salary
maximum_salary = employees["Salary"].max()

print(f"Total Employees: {total_employees}")
print(f"Total Payroll: TZS {total_payroll:,.0f}")
print(f"Average Salary: TZS {average_salary:,.0f}")
print(f"Minimum Salary: TZS {minimum_salary:,.0f}")
print(f"Maximum Salary: TZS {maximum_salary:,.0f}")

print("\n==============================")
print("DEPARTMENT ANALYSIS")
print("==============================")

# Number of employees in each department
employees_by_department = employees.groupby("Department")["EmployeeID"].count()

print("\nEmployees by Department:")
print(employees_by_department)

# Total salary by department
salary_by_department = employees.groupby("Department")["Salary"].sum()

print("\nTotal Salary by Department:")
print(salary_by_department)

# Average salary by department
average_salary_by_department = employees.groupby("Department")["Salary"].mean()

print("\nAverage Salary by Department:")
print(average_salary_by_department.apply(lambda x: f"TZS {x:,.0f}"))

print("\n==============================")
print("REGION ANALYSIS")
print("==============================")

# Number of employees in each region
employees_by_region = employees.groupby("Region")["EmployeeID"].count()

print("\nEmployees by Region:")
print(employees_by_region)

# Total salary by region
salary_by_region = employees.groupby("Region")["Salary"].sum()

print("\nTotal Salary by Region:")
print(salary_by_region)

# Average salary by region
average_salary_by_region = employees.groupby("Region")["Salary"].mean()

print("\nAverage Salary by Region:")
print(
    average_salary_by_region.apply(
        lambda x: f"TZS {x:,.0f}"
    )
)

print("\n==============================")
print("PERFORMANCE ANALYSIS")
print("==============================")

# Number of employees by performance level
employees_by_performance = employees.groupby(
    "Performance Level"
)["EmployeeID"].count()

print("\nEmployees by Performance Level:")
print(employees_by_performance)

# Average performance score by performance level
average_performance_by_level = employees.groupby(
    "Performance Level"
)["Performance"].mean()

print("\nAverage Performance by Level:")
print(
    average_performance_by_level.apply(
        lambda x: f"{x:.1f}"
    )
)

# Overall average performance
overall_performance = employees["Performance"].mean()

print(f"\nOverall Average Performance: {overall_performance:.1f}")

print("\n==============================")
print("GENDER ANALYSIS")
print("==============================")

# Number of employees by gender
employees_by_gender = employees.groupby("Gender")["EmployeeID"].count()

print("\nEmployees by Gender:")
print(employees_by_gender)

# Percentage of employees by gender
gender_percentage = (
    employees_by_gender / total_employees * 100
)

print("\nGender Percentage:")
print(
    gender_percentage.apply(
        lambda x: f"{x:.1f}%"
    )
)

# Average salary by gender
average_salary_by_gender = employees.groupby(
    "Gender"
)["Salary"].mean()

print("\nAverage Salary by Gender:")
print(
    average_salary_by_gender.apply(
        lambda x: f"TZS {x:,.0f}"
    )
)

# Average performance by gender
average_performance_by_gender = employees.groupby(
    "Gender"
)["Performance"].mean()

print("\nAverage Performance by Gender:")
print(
    average_performance_by_gender.apply(
        lambda x: f"{x:.1f}"
    )
)

print("\n==============================")
print("EMPLOYEE STATUS ANALYSIS")
print("==============================")

# Number of employees by status
employees_by_status = employees.groupby(
    "Status"
)["EmployeeID"].count()

print("\nEmployees by Status:")
print(employees_by_status)

# Percentage of employees by status
status_percentage = (
    employees_by_status / total_employees * 100
)

print("\nStatus Percentage:")
print(
    status_percentage.apply(
        lambda x: f"{x:.1f}%"
    )
)

# Average salary by status
average_salary_by_status = employees.groupby(
    "Status"
)["Salary"].mean()

print("\nAverage Salary by Status:")
print(
    average_salary_by_status.apply(
        lambda x: f"TZS {x:,.0f}"
    )
)

print("\n==============================")
print("JOB TITLE ANALYSIS")
print("==============================")

# Number of employees by job title
employees_by_job_title = employees.groupby(
    "JobTitle"
)["EmployeeID"].count()

print("\nEmployees by Job Title:")
print(employees_by_job_title)

# Total salary by job title
salary_by_job_title = employees.groupby(
    "JobTitle"
)["Salary"].sum()

print("\nTotal Salary by Job Title:")
print(salary_by_job_title)

# Average salary by job title
average_salary_by_job_title = employees.groupby(
    "JobTitle"
)["Salary"].mean()

print("\nAverage Salary by Job Title:")
print(
    average_salary_by_job_title.apply(
        lambda x: f"TZS {x:,.0f}"
    )
)

# Average performance by job title
average_performance_by_job_title = employees.groupby(
    "JobTitle"
)["Performance"].mean()

print("\nAverage Performance by Job Title:")
print(
    average_performance_by_job_title.apply(
        lambda x: f"{x:.1f}"
    )
)

print("\n==============================")
print("HIRE DATE ANALYSIS")
print("==============================")

# Earliest hire date
earliest_hire_date = employees["HireDate"].min()

# Latest hire date
latest_hire_date = employees["HireDate"].max()

print(f"\nEarliest Hire Date: {earliest_hire_date.date()}")
print(f"Latest Hire Date: {latest_hire_date.date()}")

# Extract hire year
employees["HireYear"] = employees["HireDate"].dt.year

# Number of employees hired each year
employees_by_hire_year = employees.groupby(
    "HireYear"
)["EmployeeID"].count()

print("\nEmployees Hired by Year:")
print(employees_by_hire_year)

# Calculate employee tenure
today = pd.Timestamp.today()

employees["TenureYears"] = (
    (today - employees["HireDate"]).dt.days / 365.25
)

average_tenure = employees["TenureYears"].mean()

print(f"\nAverage Employee Tenure: {average_tenure:.1f} years")

print("\n==============================")
print("HR CHARTS")
print("==============================")

import matplotlib.pyplot as plt

# Employees by Department
employees_by_department = employees.groupby(
    "Department"
)["EmployeeID"].count()

plt.figure(figsize=(10, 6))

employees_by_department.plot(
    kind="bar"
)

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()