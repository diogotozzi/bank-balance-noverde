from .account import Account

class Accounts():

    def __init__(self, accounts_list):
        self.accounts = {}
        self.initialize_accounts(accounts_list)

    def initialize_accounts(self, accounts_list):
        for i in accounts_list:
            account_number = i[0]
            account_fund = i[1]

            account = Account(account_number, account_fund)

            self.accounts[account_number] = account

    def id(self, account_number):
        return self.accounts[account_number]

    def batch_transfers(self, transfers_list):
        for i in transfers_list:
            account_number = i[0]
            amount = i[1]

            self.accounts[account_number].transfer(amount)
