-- HR Workforce Analytics
-- PostgreSQL SQL Analysis
-- Database: hr_workforce
-- Table: employees


-- 1. Overall HR Metrics
SELECT
    COUNT(*) AS total_employees,
    SUM(salary) AS total_payroll,
    ROUND(AVG(salary), 2) AS average_salary,
    MIN(salary) AS minimum_salary,
    MAX(salary) AS maximum_salary,
    ROUND(AVG(performance), 2) AS average_performance
FROM employees;


-- 2. Employees by Department
SELECT
    department,
    COUNT(*) AS total_employees
FROM employees
GROUP BY department
ORDER BY total_employees DESC;


-- 3. Salary by Department
SELECT
    department,
    SUM(salary) AS total_salary
FROM employees
GROUP BY department
ORDER BY total_salary DESC;


-- 4. Average Salary by Department
SELECT
    department,
    COUNT(*) AS total_employees,
    ROUND(AVG(salary), 2) AS average_salary
FROM employees
GROUP BY department
ORDER BY average_salary DESC;


-- 5. Employees by Region
SELECT
    region,
    COUNT(*) AS total_employees
FROM employees
GROUP BY region
ORDER BY total_employees DESC;


-- 6. Salary by Region
SELECT
    region,
    COUNT(*) AS total_employees,
    SUM(salary) AS total_salary
FROM employees
GROUP BY region
ORDER BY total_salary DESC;


-- 7. Average Salary by Region
SELECT
    region,
    COUNT(*) AS total_employees,
    ROUND(AVG(salary), 2) AS average_salary
FROM employees
GROUP BY region
ORDER BY average_salary DESC;


-- 8. Employees by Performance Level
SELECT
    performance_level,
    COUNT(*) AS total_employees
FROM employees
GROUP BY performance_level
ORDER BY total_employees DESC;


-- 9. Average Performance by Level
SELECT
    performance_level,
    COUNT(*) AS total_employees,
    ROUND(AVG(performance), 2) AS average_performance
FROM employees
GROUP BY performance_level
ORDER BY average_performance DESC;


-- 10. Gender Analysis
SELECT
    gender,
    COUNT(*) AS total_employees,
    ROUND(AVG(salary), 2) AS average_salary,
    ROUND(AVG(performance), 2) AS average_performance
FROM employees
GROUP BY gender
ORDER BY total_employees DESC;


-- 11. Employee Status
SELECT
    status,
    COUNT(*) AS total_employees,
    ROUND(AVG(salary), 2) AS average_salary
FROM employees
GROUP BY status
ORDER BY total_employees DESC;


-- 12. Job Title Analysis
SELECT
    job_title,
    COUNT(*) AS total_employees,
    SUM(salary) AS total_salary,
    ROUND(AVG(salary), 2) AS average_salary,
    ROUND(AVG(performance), 2) AS average_performance
FROM employees
GROUP BY job_title
ORDER BY total_employees DESC, average_salary DESC;


-- 13. Hiring Trend by Year
SELECT
    EXTRACT(YEAR FROM hire_date) AS hire_year,
    COUNT(*) AS total_hires
FROM employees
GROUP BY EXTRACT(YEAR FROM hire_date)
ORDER BY hire_year;