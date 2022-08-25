class balanceislow():
    def __init__(self,accnum,name,type,balance):
        self.accnum=accnum
        self.name=name
        self.type=type
        self.balance=balance
    def details(self):
        return self.accnum + self.name + self.type + self.balance

