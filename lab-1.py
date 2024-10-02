'''
Shahhill Islam
CISC 4631
LAB 1 - 10/1/2024
In collaboration with Joon Park
'''

import numpy as np

# Function for Min-Max normalization
def min_max_normalization(data, value):
    min_val = min(data)
    max_val = max(data)
    normalized_value = (value - min_val) / (max_val - min_val)
    return normalized_value

# Function for Z-score normalization
def z_score_normalization(data, value):
    mean_val = np.mean(data)
    std_dev = np.std(data)
    normalized_value = (value - mean_val) / std_dev
    return normalized_value

# Function to input the dataset from the user
def input_dataset():
    dataset = {}
    
    # Handle invalid input for the number of employees
    while True:
        try:
            num_employees = int(input("Enter the number of employees: "))
            if num_employees < 1:
                print("Please enter a positive integer.")
                continue
            break  # Break the loop if a valid integer is entered
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Handle invalid input for employee names and salaries
    for _ in range(num_employees):
        employee = input("Enter employee name: ").strip().lower()  # Convert to lowercase
        while True:
            try:
                salary = float(input(f"Enter salary for {employee}: "))
                break  # Break the loop if a valid salary is entered
            except ValueError:
                print("Invalid input. Please enter a numeric value (without commas) for the salary.")
        dataset[employee] = salary
    
    return dataset
    

# User inputs for dataset
salaries = input_dataset()

# Convert the salaries to a list of values for processing
salary_values = list(salaries.values())

# Employees to normalize (Can be changed based on user input)
employees_min_max = input("Enter employees for Min-Max normalization (comma-separated): ").split(',')
employees_z_score = input("Enter employees for Z-score normalization (comma-separated): ").split(',')

# Task 1: Min-Max normalization
print("\nThis is Shahhill Islam's Min-Max Normalization Program.")
print("Min-Max Normalized Salaries:")
for emp in employees_min_max:
    emp = emp.strip().lower()  # Convert to lowercase
    if emp in salaries:
        normalized_salary = min_max_normalization(salary_values, salaries[emp])
        print(f"Employee {emp}: {normalized_salary:.4f}")
    else:
        print(f"Employee {emp} not found in the dataset.")

# Task 2: Z-score normalization
print("\nZ-score Normalized Salaries:")
for emp in employees_z_score:
    emp = emp.strip().lower()  # Convert to lowercase
    if emp in salaries:
        normalized_salary = z_score_normalization(salary_values, salaries[emp])
        print(f"Employee {emp}: {normalized_salary:.4f}")
    else:
        print(f"Employee {emp} not found in the dataset.")
