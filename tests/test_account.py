import csv
import unittest

from src.account import Account

class TestAccount(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_account(self):
        account = Account(999, 10000)

        self.assertEqual(account.number, 999)
        self.assertEqual(account.funds, 10000)

    def test_transfer_deposit(self):
        account = Account(999, 10000)
        account.transfer(1000)

        self.assertEqual(account.funds, 11000)

    def test_transfer_debit(self):
        account = Account(999, 10000)
        account.transfer(-1000)

        self.assertEqual(account.funds, 9000)

    def test_transfer_negative_deposit(self):
        account = Account(999, -10000)
        account.transfer(1000)

        self.assertEqual(account.funds, -9000)

    def test_transfer_negative_debit(self):
        account = Account(999, -10000)
        account.transfer(-1000)

        self.assertEqual(account.funds, -11500)

    def test_transfer_zero_deposit(self):
        account = Account(999, -1000)
        account.transfer(1000)

        self.assertEqual(account.funds, 0)

    def test_transfer_zero_debit(self):
        account = Account(999, 10000)
        account.transfer(-10000)

        self.assertEqual(account.funds, 0)

    def test_wrong_transfer_class(self):
        self.assertRaises(Exception, lambda: Account(999, -1000, transferClass = 'Transfer'))

if __name__ == '__main__':
    unittest.main()
