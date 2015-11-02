from nose.tools import *
import unittest


from payroll_challenge.developer import Developer


class DeveloperFixture(unittest.TestCase):
    def test_pays_developer_1000(self):
        developer = Developer()

        amount_paid = developer.pay()

        self.assertEqual(1000, amount_paid)



