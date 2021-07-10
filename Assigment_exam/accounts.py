# -*- coding: utf-8 -*-

## 
#  This module defines several classes that implement a banking account
#  class hierarchy.
#

## 
#
class BankAccount:
    """ A bank account has a balance and a mechanism for applying interest or fees at 
    the end of the month.
    """


    def __init__(self):
        """ Constructs a bank account with zero balance.
       
        Returns
        -------
        None.

        """
        self._balance = 0.0


    def deposit(self, amount):
        """ Makes a deposit into this account.
       
        Parameters
        ----------
        amount : float
            the amount of the deposit.

        Returns
        -------
        None.

        """
       
        self._balance = self._balance + amount

    
    def withdraw(self, amount):
        """ Makes a withdrawal from this account, or charges a penalty if
        sufficient funds are not available.

        Parameters
        ----------
        amount : float
            the amount of the withdrawal.

        Returns
        -------
        None.

        """
        self._balance = self._balance - amount

    
    def monthEnd(self):
        """ Carries out the end of month processing that is appropriate
        for this account. Must be implemented in the subclasses
        
        Returns
        -------
        None.

        """
        return

    
    def getBalance(self):
        """ Gets the current balance of this bank account.

        Returns
        -------
        float
            the current balance.

        """
        return self._balance
      
      
class SavingsAccount(BankAccount):
    """ A savings account earns interest on the minimum balance.
    """


    def __init__(self):
        """ Constructs a savings account with a zero balance.
        
        Returns
        -------
        None.

        """
        super().__init__()
        self._interestRate = 0.0
        self._minBalance = 0.0


    def setInterestRate(self, rate):
        """ Sets the interest rate for this account.
        
        Parameters
        ----------
        rate : float
            the monthly interest rate in percent.

        Returns
        -------
        None.

        """
        self._interestRate = rate


    def withdraw(self, amount):
        """ Overrides superclass method.

        Parameters
        ----------
        amount : float
            the amount of the withdrawal.

        Returns
        -------
        None.

        """
        super().withdraw(amount)
        balance = self.getBalance()
        if balance < self._minBalance:
            self._minBalance = balance


    def monthEnd(self):
        """ Overrides superclass method

        Returns
        -------
        None.

        """
        interest = self._minBalance * self._interestRate / 100
        self.deposit(interest)
        self._minBalance = self.getBalance()
      
      
class CheckingAccount(BankAccount):
    """ A checking account has a limited number of free deposits and 
    withdrawals.
    """


    def __init__(self):
        """ Constructs a checking account with a zero balance.
        
        Returns
        -------
        None.

        """
        super().__init__()
        self._withdrawals = 0


    def withdraw(self, amount):
        """ Overrides superclass method


        Parameters
        ----------
        amount : float
            the amount of the withdrawal.

        Returns
        -------
        None.

        """ 
        FREE_WITHDRAWALS = 3
        WITHDRAWAL_FEE = 1
      
        super().withdraw(amount)  
        self._withdrawals = self._withdrawals + 1
        if self._withdrawals > FREE_WITHDRAWALS:
            super().withdraw(WITHDRAWAL_FEE)  


    def monthEnd(self):
        """ Overrides superclass method

        Returns
        -------
        None.

        """
        self._withdrawals = 0
      


