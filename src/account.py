class Account():

    def __init__(self, number = 0, total_funds = 0):
        self.number = int(number)
        self.total_funds = int(total_funds)

    def id(self):
        return self.number

    def transfer(self, amount = 0):
        amount = int(amount)

        interest = -500

        if amount > 0:
            self.total_funds += amount
        elif amount < 0:
            self.total_funds += amount

            if self.total_funds < 0:
                self.total_funds += interest

    def funds(self):
        return self.total_funds
