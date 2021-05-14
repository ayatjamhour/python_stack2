class User :
    def __init__ (self,name,account_num,amount,email):
        self.name=name
        self.email=email
        self.no=account_num
        self.balance=0

    def Deposit (self):
        self.balance += amount

    def Withdrawal (self):
        self.balance -= amount
        
    def  Display_user_balance(self): (self):
        print("User:",self.name , "Balance :", self.balance)
    def transfer_money(self,other_user, amount):
        self.balance -=amount
        other_user.Deposit(amount)
    
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
mechail = User("mechail", "mechail@python.com")
guido.Deposit(100)
guido.Deposit(300)
guido.Deposit(300)
guido.Withdrawl(100)
monty.Deposit(1000)
monty.Withdrawl(50)
monty.Withdrawl(50)
monty.Withdrawl(50)
print(monty.balance)
mechail.Deposit(1000)
mechail.Withdrawl(50)
mechail.Withdrawl(50)
mechail.Withdrawl(50)
guido.transfer_money(mechail,100)
print(guido.balance)
print(mechail.abalance)
guido.Display_user_balance()
monty.Display_user_balance()

    

