from .transfer import Transfer

class Account():

    def __init__(self, number = 0, funds = 0, type = 'premium', transferClass = Transfer()):
        try:
            self.number = int(number)
            self.funds = int(funds)
        except ValueError as e:
            raise Exception('The "account number" and/or "account fund" have an invalid value')

        if not isinstance(transferClass, Transfer):
            raise  Exception('transferClass must be an instance of Transfer')

        self.type = type
        self.transferClass = transferClass

    def transfer(self, amount = 0):
        self.transferClass.process(self, int(amount))
