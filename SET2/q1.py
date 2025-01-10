# Given lists
EmployeeIDs = [101, 102, 103, 104, 105, 106, 107]
Salaries = [45000, 52000, 61000, 48000, 39000, 72000, 67000]

# Create a dictionary mapping EmployeeIDs to Salaries
EmployeeData = dict(zip(EmployeeIDs, Salaries))
print("EmployeeData Dictionary:", EmployeeData)

# a) Find the highest salary in the dictionary without using any built-in functions
highest_salary = -1  # Initialize with a very low value
for salary in EmployeeData.values():
    if salary > highest_salary:
        highest_salary = salary
print("Highest Salary:", highest_salary)

# b) Count the number of employees earning more than 50,000 without using any built-in functions
count = 0
for salary in EmployeeData.values():
    if salary > 50000:
        count += 1
print("Number of employees earning more than 50,000:", count)

# c) Find the salary of the employee whose ID is 106 using a linear search
employee_id_to_find = 106
salary_of_employee = None
for emp_id, salary in EmployeeData.items():
    if emp_id == employee_id_to_find:
        salary_of_employee = salary
        break
if salary_of_employee is not None:
    print(f"Salary of employee with ID {employee_id_to_find}:", salary_of_employee)
else:
    print(f"Employee ID {employee_id_to_find} not found.")
