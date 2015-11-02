__author__ = 'bbutton'

from nose.tools import *
import unittest
from payroll_challenge.qa import QA

class QAFixture(unittest.TestCase):
    def test_pay(self):
        qa = QA()

        amount_paid = qa.pay()

        self.assertEquals(500, amount_paid)


if __name__ == '__main__':
    unittest.main()
