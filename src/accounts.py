from .account import Account

class Accounts():

    def __init__(self, accounts_list):
        self.accounts = {}
        self.initialize_accounts(accounts_list)

    def initialize_accounts(self, accounts_list =[]):
        for i in accounts_list:
            account_number = int(i[0])
            account_fund = int(i[1])

            account = Account(number = account_number, funds = account_fund)

            self.accounts[account_number] = account

    def id(self, account_number = 0):
        account_number = int(account_number)
        return self.accounts[account_number]

    def batch_transfers(self, transfers_list = []):
        for i in transfers_list:
            account_number = int(i[0])
            amount = int(i[1])

            self.accounts[account_number].transfer(amount)

    def all(self):
        total_list = []

        for i in self.accounts:
            account = self.accounts[i]
            total_list.append([account.id(), account.funds])

        return total_list
