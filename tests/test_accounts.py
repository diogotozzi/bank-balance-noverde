import csv
import unittest

from src.accounts import Accounts
from src.account import Account

class TestAccounts(unittest.TestCase):

    def setUp(self):
        self.accounts_list = self.set_accounts_file()
        self.transfers_list = self.set_transfers_file()

    def tearDown(self):
        pass

    def set_accounts_file(self):
        with open('tests/test_accounts.csv') as f:
            reader = csv.reader(f, delimiter = ',')
            accounts_list = list(reader)

        return accounts_list

    def set_transfers_file(self):
        with open('tests/test_transfers.csv') as f:
            reader = csv.reader(f, delimiter = ',')
            return list(reader)

    def test_accounts_id(self):
        accounts = Accounts(self.accounts_list)
        self.assertIsInstance(accounts.get(345), Account)

    def test_accounts_wrong_id(self):
        accounts = Accounts(self.accounts_list)
        self.assertRaises(KeyError, lambda: accounts.get(000))

    def test_account_funds_before_trasfers(self):
        accounts = Accounts(self.accounts_list)

        self.assertEqual(accounts.get(345).funds, 14428)

    def test_batch_transfers(self):
        accounts = Accounts(self.accounts_list)
        accounts.batch_transfers(self.transfers_list)

        self.assertEqual(accounts.get(345).funds, 12428)

    def test_print_all(self):
        accounts = Accounts(self.accounts_list)
        accounts.batch_transfers(self.transfers_list)

        self.assertEqual(accounts.all(), [[345, 12428], [346, 0], [347, -600]])

if __name__ == '__main__':
    unittest.main()
