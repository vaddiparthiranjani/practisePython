# Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department
# and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.
class Employee:
    def __init__(self, name, emp_id, salary, dept):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        self.dept = dept
    def calculate_salary(self,salary, hours_worked):
        overtime = 0
        if hours_worked > 50:
            overtime = hours_worked - 50
        self.salary = self.salary + (overtime * (self.salary/50))
    def assign_dept(self, emp_dept):
        self.dept = emp_dept

    def print_employee_details(self):
        print("\n Employee Name : ", self.name)
        print(" Employee id :", self.emp_id)
        print(" Employee salary : ",self.salary)
        print(" Employee Department :", self.dept)

emp1 = Employee("Ranjani","E001",50000,"sales")
emp2 = Employee("Ananya","E002",80000,"HR")
emp3 = Employee("Anagha","E003",34000,"sales")
emp4 = Employee("Samipya","E004",50000,"HR")

print("original list")
emp1.print_employee_details()
emp2.print_employee_details()
emp3.print_employee_details()
emp4.print_employee_details()

#change the department of 2nd and 4th employee
emp2.assign_dept("operations")
emp4.assign_dept("Purchase")

# calculate the overtime of the employees
emp1.calculate_salary(45000, 56)
emp3.calculate_salary(75000,67)

print("Updated employee list")
emp1.print_employee_details()
emp2.print_employee_details()
emp3.print_employee_details()
emp4.print_employee_details()



