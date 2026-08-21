class BankAccount :
    def __init__ (self,owner_name,balance=0) :
        self.owner_name = owner_name
        self.balance = balance
    def __str__ (self) :
        return f'حساب {self.owner_name}:{self.balance} تومان'
    def deposit(self,amount) :
        if amount < 0 :
            raise ValueError('مبلغ واریز نمیتونه منفی باشه')
        self.balance = self.balance + amount
    def withdraw (self,amount) :
        if amount > self.balance :
            raise ValueError ('موجودی کافی نیست')
        self.balance = self.balance - amount  
acc1 = BankAccount('ramin')
print(acc1)
acc2 = BankAccount('mahta',1000)
print(acc2)
acc1.deposit(500)
acc1.withdraw(200)
print(acc1)
try :
    acc1.withdraw(100)   
except ValueError as e :
    print(f'error :{e}')
print(acc1)





