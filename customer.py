
class Customer:
    def __init__(self, id, custPin = 1234, custBalance = 100000):
        self.id = id
        self.custPin = custPin
        self.custBalance = custBalance

    def checkId(self):
        return self.id

    def checkPin(self):
        return self.custPin

    def checkBal(self):
        return self.custBalance

    def withdrawBal(self, nominal):
        self.custBalance -= nominal

    def depositBal(self, nominal):
        self.custBalance += nominal


