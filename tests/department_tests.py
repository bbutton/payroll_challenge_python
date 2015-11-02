__author__ = 'bbutton'
from nose.tools import *
import unittest
from payroll_challenge.manager import Manager
from payroll_challenge.developer import Developer
from payroll_challenge.qa import QA
from payroll_challenge.department import Department

class DepartmentFixture(unittest.TestCase):
    def test_empty_department_pays_nothing(self):
        department = Department()

        amount_paid = department.pay()

        self.assertEqual(0, amount_paid)

    def test_department_with_single_employee_pays_correctly(self):
        department = Department()
        department.add_employee(Developer())

        amount_paid = department.pay()

        self.assertEqual(1000, amount_paid)

    def test_department_with_all_kinds_of_employees(self):
        department = Department()
        department.add_employee(Developer())
        department.add_employee(QA())

        manager = Manager()
        manager.add_employee(QA())
        manager.add_employee(Developer())
        manager.add_employee(Manager())

        manager2 = Manager()
        manager2.add_employee(Developer())

        manager.add_employee(manager2)

        department.add_employee(manager)

        amount_paid = department.pay()

        self.assertEqual(4900, amount_paid)


if __name__ == '__main__':
    unittest.main()
