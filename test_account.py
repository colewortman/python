import unittest
from account import *

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.account1 = Account('John')
        self.account2 = Account('Jane')
    
    def tearDown(self):
        del self.account1
        del self.account2

    def test_init(self):
        self.assertEqual(self.account1.get_name(), 'John')
        self.assertEqual(self.account1.get_balance(), 0)

        self.assertEqual(self.account2.get_name(), 'Jane')
        self.assertEqual(self.account2.get_balance(), 0)

    def test_deposit(self):
        self.assertFalse(self.account1.deposit(-1))
        self.assertFalse(self.account1.deposit(0))
        self.assertTrue(self.account1.deposit(1))

        self.assertFalse(self.account2.deposit(-1))
        self.assertFalse(self.account2.deposit(0))
        self.assertTrue(self.account2.deposit(1))

    def test_withdraw(self):
        self.assertFalse(self.account1.withdraw(-1))
        self.assertFalse(self.account1.withdraw(0))
        self.assertTrue(self.account1.withdraw(1))

        self.assertFalse(self.account2.withdraw(-1))
        self.assertFalse(self.account2.withdraw(0))
        self.assertTrue(self.account2.withdraw(1))

if __name__ == '__main__':
    unittest.main()