from .transfer import Transfer

class Account():

    def __init__(self, number = 0, funds = 0, type = 'premium', transfer = Transfer()):
        self.number = int(number)
        self.funds = int(funds)
        self.type = type
        self.transferClass = transfer

    def id(self):
        return self.number

    def transfer(self, amount = 0):
        self.transferClass.process(self, int(amount))
