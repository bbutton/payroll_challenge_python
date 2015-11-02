__author__ = 'bbutton'

from nose.tools import *
import unittest
from payroll_challenge.manager import Manager
from payroll_challenge.developer import Developer
from payroll_challenge.qa import QA

class ManagerFixture(unittest.TestCase):
    def test_manager_lone_pays_300(self):
        manager = Manager()

        amount_paid = manager.pay()

        self.assertEqual(300, amount_paid)

    def test_manager_with_single_employee_calculates_total_pay(self):
        manager = Manager()
        developer = Developer()
        manager.add_employee(developer)

        amount_paid = manager.pay()

        self.assertEquals(1300, amount_paid)

    def test_manager_with_multiple_employees_no_managers_calculates_total_pay(self):
        manager = Manager()
        manager.add_employee(Developer())
        manager.add_employee(QA())

        amount_paid = manager.pay()

        self.assertEquals(1800, amount_paid)

    def test_manager_with_multiple_manager_levels_calculates_total_pay(self):
        manager = Manager()

        manager2 = Manager()
        manager2.add_employee(Developer())
        manager2.add_employee(QA())

        manager.add_employee(manager2)

        amount_paid = manager.pay()

        self.assertEquals(2100, amount_paid)

if __name__ == '__main__':
    unittest.main()
