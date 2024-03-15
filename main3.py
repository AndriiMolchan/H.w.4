# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from datetime import datetime


class Employee:
    def __init__(self, name, surname, department, start_year):
        if not isinstance(name, str) or not isinstance(surname, str) or not isinstance(department, str):
            raise ValueError("Name, surname, and department must be strings")
        if not isinstance(start_year, int) or start_year < 1900 or start_year > datetime.now().year:
            raise ValueError("Invalid start year")

        self.name = name
        self.surname = surname
        self.department = department
        self.start_year = start_year


employees = []

while True:

    print("Enter employee details:")
    name = input("Name: ")
    surname = input("Surname: ")
    department = input("Department: ")

    try:
        start_year = int(input("Start year: "))
        employee = Employee(name, surname, department, start_year)
        employees.append(employee)
        print("Employee added successfully!")
    except ValueError as e:
        print("Error:", e)

    continue_input = input("Do you want to add another employee? (yes/no): ").lower()
    if continue_input != 'yes':
        break

current_year = datetime.now().year
print("\nEmployees hired after the beginning of the current year:")
count = 0
for employee in employees:
    if employee.start_year >= current_year:
        print(f"{employee.name} {employee.surname} ({employee.department}) - Hired in {employee.start_year}")
        count += 1
if count == 0:
    print("No one")
