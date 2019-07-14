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

def MoneyToday(payment,period,monthInterestRate):
    if period==0:
        return payment
    else:
        return payment/pow(1+monthInterestRate,period)
    

amortization = 25 # 25 years
month = amortization*12 # payment month
price = 329900 # money you owe bank
downPayment = 30/100*price # downpayment percentage
balance = price-downPayment

annualInterestRate = 5/100
monthlyRate = annualInterestRate/12 

# set lo/up bounds
lobound = balance/month
upbound = (balance*(1+monthlyRate)**month)/month

# start bisection search
mid = (lobound + upbound)/2
New_balance = remainingBalance(balance,mid,annualInterestRate,month)

while abs(New_balance)> 0.01:
    if New_balance > 0:
        lobound = mid
    else:
        upbound = mid
    mid = (lobound + upbound)/2
    New_balance = remainingBalance(balance,mid,annualInterestRate,month)
    print("Balance is ",New_balance)

mid = round(mid,2)

print("Monthly Payment: "+ str(mid))

interestRate = 1.8/100 # annual saving interest rate
monthInterestRate = interestRate/12 

moneyToday = 0

for i in range(0,month):
    moneyToday = moneyToday + MoneyToday(mid,i,monthInterestRate)

print("You need to spend ", moneyToday+downPayment, "at today's value!!!" )

      
      