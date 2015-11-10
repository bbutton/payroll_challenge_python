__author__ = 'bbutton'

class Department:
    def __init__(self):
        self.employees = []

    def pay(self):
        return sum(map(lambda employee: employee.pay(), self.employees))

    def add_employee(self, new_employee):
        self.employees.append(new_employee)
