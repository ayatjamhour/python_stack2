class BankAccount:
    def __init__(self, int_rate=.01, balance=0):
        self.balance =balance
        self.int_rate=int_rate
        
    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance-=amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
            return self       
    def display_account_info(self):
        print( f" balance {self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance*=self.int_rate
        return self    
            
account1=BankAccount(.2,500)
account2=BankAccount(.5,8900)

account1.deposit(500).deposit(500).deposit(500).withdraw(500).display_account_info()

account2.deposit(2000).deposit(1000).withdraw(500).withdraw(500).withdraw(500).withdraw(500).display_account_info()   
