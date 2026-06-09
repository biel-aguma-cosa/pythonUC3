

clients = {}
#client structure | CPF : {name,account}
accounts = []

class Account:
    def __init__(self, index, holder):
        self.limit = None
        self.balance = 0
    def deposit(self,n):
        pass
    def withdraw(self,n):
        if self.limit and n > self.limit:
            # not allowed
            return
        else:
            self.balance -= n
    def __str__(self):
        pass

class CheckingAccount(Account):
    def __init__(self, index, holder, limit):
        super().__init__(index, holder)
        self.limit = limit
        #limit

class SavingsAccount(Account):
    def __init__(self, index, holder):
        super().__init__(index, holder)
        #no limit