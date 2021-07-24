# Jone Huan Chong, 201533109

import random 
import datetime
class BasicAccount:

    numAc = 0 #initial number of accounts 
    
    """Initialise all variables in BasicAccount class and their appropriate forms"""
    def __init__ (self, accountName: str, openingBalance: float):
        self.acName: str = (accountName)
        self.actualBalance: float = (openingBalance) #balance of account is written as actual.Balance to differentiate from availableBalance
        BasicAccount.numAc += 1 
        self.acNum: int = (BasicAccount.numAc)
        self.cardnum : str = ""
        self.cardexp : tuple = ()
        self.availableBalance = self.actualBalance
        

    def __str__(self): #returns the account name. and available balance
        """
        __str__ will return the Account name, and available balance for the basic Account

        Parameters:
            Nothing

        Return:
            Account name and available balance of account as a string
        """
        return 'Account name: {self.acName}\nAccount available balance: £ {self.availableBalance}'.format(self=self)
    
    #deposit and withdraw of BasicAccount does not include overdraft numbers
    def deposit(self, depositAmount):
        """
        deposit will add the deposit amount to the balance of the account as long as deposit amount is valid

        Parameters:
            depositAmount : amount of deposit

        Return:
            Nothing
        """
        if depositAmount > 0:
            self.actualBalance += depositAmount
            print("Balance: £", self.actualBalance)
        else:
            print("Invalid deposit amount")

    def withdraw(self, withdrawAmount):
        """
        withdraw will deduct the withdraw amount from the balance of the account as long as withdraw amount is valid and the account balance is sufficient

        Parameters:
            withdrawAmount: amount of withdrawal

        Return:
            Nothing
        """
        if withdrawAmount > 0 and withdrawAmount <= self.actualBalance:
            self.actualBalance -= withdrawAmount
            print(self.acName, " has withdrew £", withdrawAmount," New balance is £", self.actualBalance)
        else:
            print("Cannot withdraw £", withdrawAmount)

    def getAvailableBalance(self):
        """
        getAvailableBalance will return the available balance of the account. 
        For a basic account, getAvailableBalance and getBalance are essentially the same as the actual balance and available balance are the same due to no overdraft factor.

        Parameters:
            Nothing

        Returns:
            available balance of account
        """
        print("Available Balance: £",self.availableBalance)
        return float(self.availableBalance)

    def getBalance(self):
        """
        getBalance will return the actual balance of the account. 
        For a basic account, getAvailableBalance and getBalance are essentially the same as the actual balance and available balance are the same due to no overdraft factor.

        Parameters:
            Nothing

        Returns:
            actual balance of account
        """
        print("Balance: £", self.actualBalance)
        return float(self.actualBalance)

    def printBalance(self):
        """
        printBalance will print the balance information of the account. 
        For a basic account, due to no overdraft factor, just balance of the account will be printed

        Parameters:
            Nothing

        Returns:
            nothing
        """
        print("Balance: £", self.actualBalance)

    def getName(self):
        """
        getName will return the account holder name information
        
        Parameters:
            Nothing

        Returns:
            account name as a string
        """
        return str((self.acName))

    def getAcNum(self):
        """
        getAcNum will return the account number information of the account. 
        
        Parameters:
            Nothing

        Returns:
            account number as a string
        """
        print("Account Number: ", self.acNum)
        return (str(self.acNum))

    def issueNewCard(self):
        """
        issueNewCard will generate new card information of card number, card expiry month and card expiry year for the account.

        Parameters:
            nothing

        Returns:
            card number as string, card expiry date as tuple
        """
        today = datetime.datetime.now() #get current date and time
        cardyear = (int(today.year) + 3) #set expiry year to 3 years from present
        self.cardnum = str(random.randint(10**15,10**16)) #ensures a range of 16 digits
        self.cardexp = (today.month, int(str(cardyear)[-2:])) #converted to last two digit year form
        print("Card Number: " , self.cardnum)
        print("Card Expiry Date: ", self.cardexp)
        return str(self.cardnum), tuple(self.cardexp)

    def closeAccount(self): #returns boolean
        """
        closeAccount will withdraw the remaining balance of the account if balance is sufficient, then return True/False 

        Parameters:
            nothing
        
        Returns:
            boolean
        """
        if self.actualBalance >= 0:
            self.withdraw(self.actualBalance)
            print("Account has been withdrawn of its balance and closed")
            return True
        else:
            print("Insufficient Balance for closure of account")
            return False

class PremiumAccount(BasicAccount):
    """in PremiumAccount class, the methods of __str__, withdraw, deposit, printBalance  differs from
        the BasicAccount class due to the consideration of overdraft and negative balances"""
    
    def __init__ (self, accountName: str, openingBalance: float, initialOverdraft:float):
        super().__init__(accountName,openingBalance)
        self.overdraftLimit: float = initialOverdraft
        self.availableBalance: float = openingBalance + initialOverdraft
        self.overdraftAvailable: float = self.overdraftLimit
        self.overdraft = False
    
    def __str__(self):
        """
        __str__ will return the Account name, and available balance for the premium Account

        Parameters:
            Nothing

        Return:
            Account name, available balance, overdraft boolean, overdraft available and limit of account as a string
        """
        return 'Account name: {self.acName}\nAccount available balance: £{self.availableBalance}\nAccount in Overdraft: {self.overdraft}\nOverdraft available: £{self.overdraftAvailable} out of £{self.overdraftLimit} '.format(self=self)

    def overdraftUpdate(self):
        """
        overdraftUpdate will update the overdraft and available balance, and used when a deposit/withdrawal/new overdraft limit is carried out.
        This function is added to prevent writing repetitive code.

        Parameters:
            Nothing

        Returns:
            overdraft as true if the account has an overdraft, and false if not
        """
        self.availableBalance = self.actualBalance + self.overdraftLimit
        if self.actualBalance < 0:
            self.overdraftAvailable = self.overdraftLimit + self.actualBalance     
            return self.overdraft == True           
        else:
            self.overdraftAvailable = self.overdraftLimit
            return self.overdraft == False

    def setOverdraftLimit(self, newOverdraftLimit):
        """
        setOverdraftLimit will update a new overdraft limit for the premium account

        Parameters:
            newOverdraftLimit: amount of new overdraft limit

        Returns:
            New overdraft limit as a float

        """
        self.overdraftLimit = newOverdraftLimit 
        print("New overdraft limit: £",self.overdraftLimit)
        self.overdraftUpdate() #updates ovedraft and available balance
        return float(self.overdraftLimit)

    def withdraw(self, withdrawAmount):
        """
        withdraw will deduct the withdraw amount from the balance of the account as long as withdraw amount is valid, and the balance and overdraft is sufficient

        Parameters:
            withdrawAmount: amount of withdrawal

        Return:
            Nothing
        """
        if withdrawAmount > 0 and (self.actualBalance - withdrawAmount > -self.overdraftLimit): #ensure withdraw amount does not exceed overdraft limit and balance
            self.actualBalance -= withdrawAmount
            self.overdraftUpdate() #updates ovedraft and available balance
            print(self.acName, " has withdrew £", withdrawAmount," New balance is £", self.actualBalance) 

        else:
            print("Cannot withdraw £", withdrawAmount,)

    def deposit(self, depositAmount):
        """
        deposit will add the deposit amount to the balance of the account as long as deposit amount is valid

        Parameters:
            depositAmount : amount of deposit

        Return:
            Nothing
        """
        if depositAmount > 0:
            self.actualBalance += depositAmount
            self.overdraftUpdate() #updates ovedraft and available balance
            print("Balance: £", self.actualBalance)

        else:
            print("Invalid deposit amount")

    def printBalance(self):
        """
        printBalance will print the balance information of the account. 
        For a premium account, due to overdraft factor, the actual balance, available balance, and overdraft available and limit of the account will be printed

        Parameters:
            Nothing

        Returns:
            nothing
        """
        print("Balance: £", self.actualBalance, ", Available Balance: £", self.availableBalance, ", Account in Overdraft: ", self.overdraft, ", Overdraft Available: £", self.overdraftAvailable, "out of £", self.overdraftLimit)


def main():
    # p3 = PremiumAccount("tuff", 1000, 1)
    # print(p3.overdraft)
    # print(p3.acNum) 
    # print(p3)
    # p3.deposit(100)
    # print(p3.getAvailableBalance())
    # p3.setOverdraftLimit(500)
    # p3.printBalance()
    # p3.withdraw(1300)
    # p3.deposit(1)
    # print(p3.getAvailableBalance())
    # print(p3.overdraft)
    # print(p3)
    # print()
    # p1= BasicAccount("tufferino", 1000)
    # print(p1)
    # print(p1.acNum) 
    # p1.withdraw(100)
    # p1.deposit(10000)
    # p1.issueNewCard()
    # p1.closeAccount()
    # p3.closeAccount()

    PremiumAccount("chicken", 1000, 1)
    print(PremiumAccount.acName == "chicken")

if __name__=="__main__": #ensures test code does not run when imported
    main()

