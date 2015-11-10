__author__ = 'bbutton'


class Manager:
    def __init__(self):
        self.employees = []

    def pay(self):
        return 300 + sum(map(lambda employee: employee.pay(), self.employees))

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

