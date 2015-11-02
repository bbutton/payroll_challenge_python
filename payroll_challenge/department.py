__author__ = 'bbutton'

class Department:
    def __init__(self):
        self.employees = []

    def pay(self):
        payments = map(lambda employee: employee.pay(), self.employees)
        return reduce(lambda x,y: x + y, payments, 0)

    def add_employee(self, new_employee):
        self.employees.append(new_employee)
