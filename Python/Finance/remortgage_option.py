# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:23:08 2020

@author: User
"""

import mortgage

def currentValue(fixedPayment,term,monthlySavingRate):
    """
    fixedPyament: how much you pay every month
    term: mortgage term, ususally 5 years
    monthlySavingRate: inflation rate, ~2%/2
    """
    # Set initial condition
    moneyToday = 0
    # Find equivalent money at today's value 
    for i in range(0,term*12):
        moneyToday = moneyToday + mortgage.moneyBackToToday(fixedPayment,i,monthlySavingRate)
    return round(moneyToday,2)



"""
Our Main code here
"""
years = 25 # 25 years
term = 5; # a 5 years mortgage term
price = 322500 # house price ， 322500
downPaymentPercentage = 0.35 # downpayment percentage
loanRate = 0.0289 # annual loan rate
month = years*12
downPayment = price*downPaymentPercentage
savingRate = 0.02 # annual saving interest rate
monthlySavingRate = savingRate/12 # minimum monthly interest you can get
   
# recall the moortgage calculation function
fixedPayment = mortgage.mortgageCalculator(years,price,downPaymentPercentage,loanRate)
fiveYearPayment = currentValue(fixedPayment,term,monthlySavingRate)

print("With a monthly Payment of",str(fixedPayment)+", you can pay off you loan in",str(years), "years!!!")
print("In a term of ",str(term)+ " years, you actually will pay",str(fiveYearPayment), "In today's value !!!")


"""
Calculate what is interest rate you can get to even the penalty
"""
# mortgage repayment, refer to https://www.ratehub.ca/penalty-calculator
mortgagePenalty =1700

# Apply bisection algorithm to find the even new loan rate
upbound = loanRate
lobound = 0
mid = (upbound + lobound)/2

new_fixedPayment = mortgage.mortgageCalculator(years,price,downPaymentPercentage,mid)
new_fiveYearPayment = currentValue(new_fixedPayment,term,monthlySavingRate)

offset = fiveYearPayment-new_fiveYearPayment-mortgagePenalty

while abs(offset)> 0.2:
    if offset > 0:
        lobound = mid
    else:
        upbound = mid
    mid = (lobound + upbound)/2
    new_fixedPayment = mortgage.mortgageCalculator(years,price,downPaymentPercentage,mid)
    new_fiveYearPayment = currentValue(new_fixedPayment,term,monthlySavingRate)
    print(new_fiveYearPayment)
    offset = fiveYearPayment-new_fiveYearPayment-mortgagePenalty
 
print("With new loan rate of "+str(round(mid*100,4))+"%", "your cost of breaking a mortgage contract is 0")   
    