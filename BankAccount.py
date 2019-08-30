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
    return self.accountHolder

  def getDateOpened(self):
    return self.dateOpened 

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


class BalanceError(Exception):
  value = "Sorry, you only have " + str(BankAccount.balance) + "in your account."


class SavingsAccount(BankAccount):
  def __init__(self, interestRate, dateLastInterestAdded, interestAccrued):
    self.interestRate = float(interestRate)
    self.dateLastInterestAdded = str(dateLastInterestAdded)
    self.interestAccrued = float(interestAccrued)

  def getInterestRate(self):
    return self.interestRate

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

  #def addInterest(self, date):
    #super().balance += OurDate.numberOfDaysBetween(date1, otherDate) * 0.03
    
#  def __str__(self):
#    return "Savings account balance: " + str(self.balance)

  
class NoticeDepositAccount(SavingsAccount):
  def __init__(self, noticePeriod):
    self.noticePeriod = noticePeriod

  def getNoticePeriod(self):
    return self.noticePeriod

  def setNoticePeriod(self, newNoticePeriod):
    self.noticePeriod = newNoticePeriod



class OurDate:
  def __init__(self, dayOfMonth, month, year):
    self.dayOfMonth = int(dayOfMonth)
    self.month = int(month)
    self.year = int(year)

  def getOurDate(self):
    return str(self.year) + str(self.month) + str(self.dayOfMonth)

  def setOurDate(self, newDayOfMonth, newMonth, newYear):
    self.dayOfMonth = newDayOfMonth

  @staticmethod
  def numberOfDaysBetween(date1, otherDate):
    months = [30, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leapyears = [1992, 1996, 2000, 2004, 2008, 2012]
    leapyearsbetween = []

    year1 = int(date1[:4])
    month1 = int(date1[4:6])
    day1 = int(date1[6:8])

    otherYear = int(otherDate[:4])
    otherMonth = int(otherDate[4:6])
    otherDay = int(otherDate[6:8])

    for i in range(year1, otherYear-1, -1):
        if i in leapyears:
            leapyearsbetween.append(i)

    numofdays1 = year1*365 + sum(months[:month1]) + day1
    numofdays2 = otherYear*365 + sum(months[:otherMonth]) + otherDay

    totaldays = numofdays1 - numofdays2 + len(leapyearsbetween)
    print("Calculating number of days between", date1, "and", otherDate)
    return totaldays

class InterestAccount(BankAccount):
    def deposit(self, amount):
        BankAccount.deposit(self, amount)
        self.balance *= 1.03
