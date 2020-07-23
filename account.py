
class BankAcount:
  
  def __init__(self, first_name, last_name,phone_number,bank):
    self.first_name=first_name
    self.last_name=last_name
    self.bank=bank
    self.balance=0
    self.phone_number=phone_number
    self.deposits=[]
    self.withdrawals=[]
    self.loans=0
    
  def account_name(self):
    name="{} account for {} {}".format(self.bank, self.first_name, self.last_name )
    return name
    
  def deposit (self, amount):
      if amount <=0:
          print("Sorry that amount is less")
      else:
        self.balance += amount
        self.deposits.append(amount)
        print("You have deposited {} to your {}".format(amount,self.account_name())) 
    
     
  def get_balance(self, amount):
      return "Balance for {} is {}".format(self.account_name(),self.balance)
      
    
  def withdraw(self, amount):
    if amount <= 0:
        print("You can not withdraw that amount")

    elif amount > self.balance:
        print("You dont have enough balance")
    else:
        self.balance-=amount
        self.withdrawals.append(amount)
        print("You have withdrawn {} from {}".format(amount,self.account_name()))

      
  def get_balance(self):
      return"The balance for {} is {}".format(self.account_name(),self.balance)

  def withdraw_stementst(self):
     for withdrawal in self.withdrawals:
      print(withdrawal)

  def deposit_stementst(self):
     for deposit in self.deposits:
      print(deposit)

  
  def loans(self,amount):
      if amount<=0:
          print("you cant request a loan of that amount")
      else:
         self.loans = amount
      print("you have been given a loan of{}".format(amount))

      
  def loan_repayment(self,amount):
      if amount <= 0:
          print("you cannot repay with that amount")
      elif self.loans == 0:
              print("You dont have a loan at the moment")
      elif amount > self.loan:
            print("your loan is{},please enter an amount that is less or equal".format(self.loan))
      else:
            self.loan == amount
      print("You have repaid your loan with{}.Your loan balance is{}".format(amount,self.loan))
          