#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime
class Customer(object):
    def __init__(self, nric, name, accounts):
        self.nric = nric
        self.accounts = accounts
        self.name = name
    def __str__(self):
         return f'\n Customer details: NRIC= {self.nric}, name= {self.name}'
    def addaccount(self,acc):
        if acc not in self.accounts:
            self.accounts.append(acc)
        else:
            print ("account already exists")
            
    def removeaccount(self,acc):
        if acc in self.accounts:
            self.accounts.remove(acc)
        else:
            print ("account already got removed")
    
    def transaction_report(self, start_date, end_date):
        transaction_report = ''
        for acc in self.accounts:
            transaction_report += f"\n report for {acc.name}: \n"
            transaction_report += acc.transaction_report(start_date, end_date)
        return transaction_report
    
class Account(object):
   
    def __init__(self, account_number, balance, customer, branch):
        self.account_number = account_number
        self.customer = customer
        self.balance = balance
        self.transactions = []
        customer.accounts.append(self)
        branch.accounts.append(self)
    
    def __str__(x):
         return f'\n account details: Account number= {x.account_number}, customer info= {x.customer}, balance={x.balance}'

    def transaction_report(self, start_date, end_date):
        filtered_trans = filter(lambda x: x.date>=start_date and x.date<=end_date, self.transactions)
        transaction_report = ''
        for tran in self.transactions:
            transaction_report += str(tran)
        return transaction_report
            
class Bank:
    def __init__(self,name,branches=[]):
        self.name = name
        self.branches=branches
        
    def __str__(self):
        rep = ''
        for branch in self.branches:
            rep += str(branch)
        return "\n branches of this bank:{0}".format(rep)
    def transaction_report(self, start_date, end_date):
        transaction_report = ''
        for branch in self.branches:
            transaction_report += f"\n report for {branch.name}: \n"
            transaction_report += branch.transaction_report(start_date, end_date)
        return transaction_report
                 
class Branch(object):
    def __init__(self, branch_name,parent_bank,accounts=[]):
        self.accounts=accounts
        self.name = branch_name
        parent_bank.branches.append(self)

    def __str__(self):
        rep = ''
        for customer in self.accounts:
            rep += str(customer)
        return "\n accounts of this branch:{0}".format(rep)
    def transaction_report(self, start_date, end_date):
        transaction_report = ''
        for acc in self.accounts:
            transaction_report += f"\n report for account {acc.account_number}: \n"
            transaction_report += acc.transaction_report(start_date, end_date)
        return transaction_report
   
class Transaction(object):
    def __init__(self, amount, transaction_type, account, remarks=''):
        self.account=account
        self.amount=amount
        self.type = transaction_type
        self.remarks = remarks
        self.date=datetime.datetime.now()
        account.transactions.append(self)

    def __str__(self):
        return f'\n {self.account}, Amount= {self.amount}, Date={self.date}, Type={self.type}\n'

class Withdraw(Transaction):
    def __init__(self, amount, account, remarks=''):
        if account.balance < amount:
            raise Exception("insufficient fund")
        super().__init__(amount, 'debit', account, remarks)
        account.balance -= amount
    def __str__(self):
        return f'\n {self.account}, Amount= {self.amount}, Date={self.date}, Type={self.type}\n'
class Deposit(Transaction):
    def __init__(self, amount, account, remarks=''):
        super().__init__(amount, 'credit', account, remarks)
        account.balance += amount
    def __str__(self):
        return f'\n {self.account}, Amount= {self.amount}, Date={self.date}, Type={self.type}\n'
class Transfer(object):
    def __init__(self,acc1,acc2,amount, remarks):
        self.acc1=acc1
        withdraw = Withdraw(amount, acc1, remarks)
        self.acc2=acc2
        self.amount = amount
        self.remarks = remarks
        deposit =Deposit(amount, acc2, remarks)
        self.date=datetime.datetime.now()
        
       


# In[5]:


cust_list  = [Customer("S87654321Z","anusha", []),Customer("S81231231Z","anusha", []),Customer("S87454321Z","anusha", [])]
bank = Bank('DBS')
branch = Branch('main branch', bank)
acc1 = Account("2345679", 100000, cust_list[0], branch)
acc2 = Account("1234970", 100000, cust_list[0], branch)
acc3 = Account("2315678", 100000, cust_list[1], branch)
acc4 = Account("6345678", 100000, cust_list[1], branch)
acc5 = Account("7345678", 100000, cust_list[2], branch)
acc6 = Account("7935678", 100000, cust_list[2], branch)
       
acc1_withdrawl = Withdraw(10, acc1, "money for lunch")
acc1.balance

acc1_withdrawl = Withdraw(10, acc1, "money for lunch")
acc1.balance

start_time = datetime.datetime(2020, 1,1)
end_time = datetime.datetime.now()
print(acc1.transaction_report(start_time, end_time))
transfer = Transfer(acc2, acc1, 20, "treat him for lunch")

print(acc1.transaction_report(start_time, end_time))

print(bank.transaction_report(start_time, end_time))


# In[ ]:




