class BankAccount:
  def __init__(self, accountNo, balance, accountHolder, dateOpened):
    self.accontNo = int(accountNo)
    self.balance = float(balance)
    self.accountHolder = str(accountHolder)
    self.dateOpened = str(dateOpened)

  def getAccountNo(self):
    return self.accountNo 

  def getBalance(self):
    return self.balance

  def getAccountHolder(self):
    return accountHolder

  def getDateOpened(self):
    return dateOpened 

  def setAccountNo(self, newAccountNo):
    self.accountNo = newAccountNo

  def setBalance(self, newBalance):
    self.balance = newBalance

  def setDateOpened(self, newDateOpened):
    self.dateOpened = newDateOpened

  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    self.balance -= amount

  def transfer(self, amount, otherBankAccount):
    try:
      self.withdraw(amount)
      otherBankAccount.deposit(amount)
    except BalanceError:
      print(BalanceError.value % self.balance)

  def __str__(self):
    return "Bank balance: " + self.balance 


class SavingsAccount(BankAccount):
  def __init__(self, interestRate, dateLastInterestAdded, interestAccrued):
    self.interestRate = float(interestRate)
    self.dateLastInterestAdded = str(dateLastInterestAdded)
    self.interestAccrued = float(interestAccrued)

  def getInterestRate(self):
    return self.interRate

  def getDateLastInterestAdded(self):
    return self.dateLastInterestAdded

  def getInterestAccrued(self):
    return self.interestAccrued

  def setInterestRate(self, newInterestRate):
    self.interestRate = newInterestRate

  def setDateLastInterestAdded(self, newDateLastInterestAdded):
    self.dateLastInterestAdded = newDateLastInterestAdded

  def setInterestAccrued(self, newInterestAccrued):
    self.interestAccrued = newInterestAccrued

  def addInterest(self, date):
    #finish interest class first
    
  def __str__(self):
    return "Savings account balance: " + str(self.balance)

  
class NoticeDepositAccount(SavingsAccount):
  def __init__(self, noticePeriod):
    self.noticePeriod = noticePeriod

  def getNoticePeriod(self):
    return self.noticePeriod

  def setNoticePeriod(self, newNoticePeriod):
    self.noticePeriod = newNoticePeriod

  
class BalanceError(Exception):
  value = "Sorry, you only have " + str(self.balance) + "in your account."


class OurDate(self, dayOfMonth, month, year):
  def __init__(self, dayOfMonth, month, year):
    self.dayOfMonth = int(dayOfMonth)
    self.month = int(month)
    self.year = int(year)

  def getOurDate(self):
    return str(self.year) + str(self.month) + str(self.dayOfMonth)

  def setOurDate(self, newDayOfMonth, newMonth, newYear):
    self.dayOfMonth = newDayOfMonth

  def numberOfDaysBetween(self, date1, otherDate):
    
