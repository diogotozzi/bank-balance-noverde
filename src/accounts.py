from .account import Account

class Accounts():

    def __init__(self, accounts_list):
        self.accounts = {}
        self.initialize_accounts(accounts_list)

    def initialize_accounts(self, accounts_list =[]):
        for i in accounts_list:
            try:
                account_number = int(i[0])
                account_fund = int(i[1])
            except ValueError as e:
                raise Exception('The "account number" and/or "account fund" have an invalid value: ' + str(i))

            account = Account(number = account_number, funds = account_fund)

            self.accounts[account_number] = account

    def get(self, account_number = 0):
        try:
            account_number = int(account_number)
        except ValueError as e:
            raise Exception('The "account number" has an invalid value: ' + str(account_number))

        try:
            return self.accounts[account_number]
        except KeyError as e:
            raise Exception('Account not found: ' + str(account_number))

    def all(self):
        total_list = []

        for i in self.accounts:
            account = self.accounts[i]
            total_list.append([account.number, account.funds])

        return total_list

    def batch_transfers(self, transfers_list = []):
        for i in transfers_list:
            try:
                account_number = int(i[0])
                amount = int(i[1])
            except ValueError as e:
                raise Exception('The "account number" and/or "amount" have an invalid value: ' + str(i) )

            self.accounts[account_number].transfer(amount)
