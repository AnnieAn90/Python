# -*- coding: utf-8 -*-
"""
THIS CODE COMPUTES THE FIXED MONTHLY PAYMENT THAT REQUIRED TO PAYOFF THE BALANCE WITHIN A YEAR
USING BYSECTION SEARCH
"""

def remainingBalance(balance,fixedPayment,annualInterestRate):
    """
    Calculate the annual balance after a fixed monthly payment and anuual interest rate
    """
    for i in range(0,12):
       unpaidBalance = balance - fixedPayment
       if unpaidBalance >0:
           interest = unpaidBalance*annualInterestRate/12
       else:
           interest = 0
       balance = unpaidBalance+interest
    return balance

balance = 999999 # money you owe bank
annualInterestRate = 0.18 
monthlyRate = annualInterestRate/12 

# set lo/up bounds
lobound = balance/12
upbound = (balance*(1+monthlyRate)**12)/12

# start bisection search
mid = (lobound + upbound)/2
yearBalance = remainingBalance(balance,mid,annualInterestRate)

while abs(yearBalance)> 0.01:
    if yearBalance > 0:
        lobound = mid
    else:
        upbound = mid
    mid = (lobound + upbound)/2
    yearBalance = remainingBalance(balance,mid,annualInterestRate)

mid = round(mid,2)

print("Lowest Payment: "+ str(mid))



      
      