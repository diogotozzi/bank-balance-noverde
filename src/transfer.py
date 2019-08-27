class Transfer():

    def __init__(self):
        pass

    def process(self, account, amount = 0):
        amount = int(amount)

        interest = -1000
        if account.type == 'premium':
            interest = -500

        account.funds += amount
        if (amount < 0) and (account.funds < 0):
            account.funds += interest
