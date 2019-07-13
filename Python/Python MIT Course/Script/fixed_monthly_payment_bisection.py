# -*- coding: utf-8 -*-
"""
THIS CODE COMPUTES THE FIXED MONTHLY PAYMENT THAT REQUIRED TO PAYOFF THE BALANCE WITHIN A YEAR
USING BYSECTION SEARCH
"""

def remainingBalance(balance,fixedPayment,annualInterestRatem,month):
    """
    Calculate the annual balance after a fixed monthly payment and anuual interest rate
    """
    for i in range(0,month):
       unpaidBalance = balance - fixedPayment
       if unpaidBalance >0:
           interest = unpaidBalance*annualInterestRate/12
       else:
           interest = 0
       balance = unpaidBalance+interest
    return balance


amortization = 25 # 25 years
month = amortization*12 # payment month
balance = 329900 # money you owe bank
annualInterestRate = 2.79
monthlyRate = annualInterestRate/12 

# set lo/up bounds
lobound = balance/month
upbound = (balance*(1+monthlyRate)**month)/month

# start bisection search
mid = (lobound + upbound)/2
New_balance = remainingBalance(balance,mid,annualInterestRate,month)

while abs(New_balance)> 1000:
    if New_balance > 0:
        lobound = mid
    else:
        upbound = mid
    mid = (lobound + upbound)/2
    New_balance = remainingBalance(balance,mid,annualInterestRate,month)
    print("Code is stilling running! ")

mid = round(mid,2)

print("Lowest Payment: "+ str(mid))



      
      