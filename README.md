# HR Workforce Analytics

An end-to-end HR workforce analytics project built to analyze employee demographics, salaries, performance, departments, regions, hiring trends, and workforce status using Excel, Python, PostgreSQL, SQL, and Power BI.

## Project Overview

This project demonstrates an end-to-end data analytics workflow:

1. Prepare and analyze HR employee data in Excel.
2. Perform data cleaning and exploratory analysis using Python and Pandas.
3. Load the workforce data into PostgreSQL.
4. Perform HR and business analysis using SQL.
5. Build an interactive Power BI dashboard with KPIs, charts, and slicers.
6. Document and publish the project on GitHub.

## Business Questions

This project answers the following questions:

- How many employees are in the organization?
- What is the total payroll?
- What is the average employee salary?
- Which departments have the most employees?
- Which departments have the highest payroll?
- Which regions have the largest workforce?
- What is the employee performance distribution?
- How do salary and performance compare by gender?
- Which job titles have the highest salaries and performance?
- How has employee hiring changed over the years?

## Dataset

The project uses a sample HR workforce dataset containing **20 employees**.

The dataset includes:

- Employee ID
- Employee Name
- Gender
- Department
- Job Title
- Region
- Salary
- Hire Date
- Performance Score
- Employment Status
- Performance Level

## Key HR Metrics

| Metric | Result |
|---|---:|
| Total Employees | 20 |
| Total Payroll | TZS 30,250,000 |
| Average Salary | TZS 1,512,500 |
| Minimum Salary | TZS 1,100,000 |
| Maximum Salary | TZS 2,100,000 |
| Average Performance | 84.6 |

## Employees by Department

| Department | Employees |
|---|---:|
| IT | 5 |
| Finance | 4 |
| Sales | 4 |
| HR | 3 |
| Marketing | 2 |
| Operations | 2 |

## Salary by Department

| Department | Total Salary (TZS) |
|---|---:|
| IT | 8,800,000 |
| Finance | 6,920,000 |
| Sales | 5,080,000 |
| HR | 4,000,000 |
| Marketing | 2,850,000 |
| Operations | 2,600,000 |

## Employees by Region

| Region | Employees |
|---|---:|
| Dar es Salaam | 7 |
| Arusha | 5 |
| Dodoma | 4 |
| Mwanza | 4 |

## Performance Distribution

| Performance Level | Employees |
|---|---:|
| Excellent | 7 |
| Good | 7 |
| Needs Improvement | 6 |

## Gender Analysis

The dataset contains an equal gender distribution:

| Gender | Employees |
|---|---:|
| Female | 10 |
| Male | 10 |

Average salary:

- Female: TZS 1,487,000
- Male: TZS 1,538,000

Average performance:

- Female: 86.4
- Male: 82.8

## Hiring Trend

| Year | New Hires |
|---|---:|
| 2019 | 1 |
| 2020 | 3 |
| 2021 | 4 |
| 2022 | 4 |
| 2023 | 4 |
| 2024 | 4 |

## Business Insights

### 1. IT has the largest workforce

The IT department has **5 employees**, making it the largest department in the dataset.

### 2. IT has the highest departmental payroll

IT has a total payroll of **TZS 8.8 million**, followed by Finance at **TZS 6.92 million**.

### 3. Dar es Salaam has the largest workforce

Dar es Salaam has **7 employees**, followed by Arusha with 5 employees.

Dar es Salaam also has the highest regional payroll at **TZS 11.2 million**.

### 4. Overall workforce performance is strong

The average performance score is **84.6**.

There are:

- 7 Excellent employees
- 7 Good employees
- 6 employees who Need Improvement

Therefore, **14 out of 20 employees** are rated Good or Excellent.

### 5. Equal gender representation

The dataset contains an equal number of female and male employees:

- 10 Female
- 10 Male

### 6. Hiring increased over time

The organization hired:

- 1 employee in 2019
- 3 employees in 2020
- 4 employees in each year from 2021 to 2024

This indicates stronger hiring activity after 2020.

## Tools and Technologies

### Microsoft Excel

Used for:

- Data preparation
- Data inspection
- PivotTables
- PivotCharts
- Initial HR analysis

### Python

Used for:

- Data cleaning
- Data validation
- Exploratory data analysis
- HR metrics
- Grouping and aggregation
- Data visualization

Main Python libraries:

- Pandas
- Matplotlib
- OpenPyXL

### PostgreSQL

Used for:

- Storing the HR workforce dataset
- Structured data management
- SQL-based analysis

Database:

```text
hr_workforce
