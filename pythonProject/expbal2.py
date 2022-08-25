from exceptionbal import balanceislow
def withdraw(amount,balance):
    if(balance < amount):
       raise "there is no sufficient balance"
    balance=balance-amount



