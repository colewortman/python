import pytest
from account import *

class Test:
    def setup_method(self):
        self.account1 = Account('John')
        self.account1.deposit(1)

        self.account2 = Account('Jane')
        self.account2.deposit(1)
    
    def teardown_method(self):
        del self.account1
        del self.account2

    def test_init(self):
        assert self.account1.get_name() == 'John'
        assert self.account1.get_balance() == 1

        assert self.account2.get_name() == 'Jane'
        assert self.account2.get_balance() == 1

    def test_deposit(self):
        assert self.account1.deposit(-1) == False
        assert self.account1.deposit(0) == False
        assert self.account1.deposit(1) == True

        assert self.account2.deposit(-1) == False
        assert self.account2.deposit(0) == False
        assert self.account2.deposit(1) == True

    def test_withdraw(self):
        assert self.account1.withdraw(-1) == False
        assert self.account1.withdraw(0) == False
        assert self.account1.withdraw(2) == False
        assert self.account1.withdraw(1) == True

        assert self.account2.withdraw(-1) == False
        assert self.account2.withdraw(0) == False
        assert self.account2.withdraw(2) == False
        assert self.account2.withdraw(1) == True