# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 17:08:40 2019

@author: Zipeng
THIS SCRIPT COMPARES THE COSTS OF BUYING AND RESALING A CONDO 
TO RENTING AN APARTMENT
"""
# laod the mortgage script
import mortgage 

def costOfBuyingAndSaling(salePrice,balanceOweBank,moneyPaidBank,maintainanceFee,buyingFee,carCost,mortgage):
    """
    Note WE CAN DIRECTLY PASS mortgage File TO THIS FUNCTION S.T. THIS FUNCTION CAN
    ACCESS ALL THE VARIBALES/FUNCTIONS DEFINED IN mortgage File.
    THIS FUNCTION IS DEFINED FOR USING BISECTION METHOD TO FIND THE NEUTRAL SELLING PRICE
    """
    agentFeePercent = 0.025 # agent fee percent, future
    agentFee = agentFeePercent*salePrice 
    saleGain = salePrice-agentFee-balanceOweBank # money gain from selling the property, sale-agentFee-bankBalance, future
    saleGainToday = mortgage.moneyBackToToday(saleGain,month,mortgage.monthlySavingRate) # Bring money back, today
    # Calulate the total cost of buying a property, today
    buyCost = mortgage.downPayment + moneyPaidBank + maintainanceFee + buyingFee + carCost - saleGainToday
    return buyCost

                     
"""
CALCULATE YOUR RENT COST OVER THE YEARS
"""
monthlyRent = 1885 # include parking
years = 4 # renting years
month = years*12

# Set initial rent
rentCost = 0
# Find equivalent money at today's value 
for i in range(0,month):
    rentCost = rentCost + mortgage.moneyBackToToday(monthlyRent,i,mortgage.monthlySavingRate)

print("We will spend",round(rentCost,2),"at today's money value for renting in",years,"years!!!")

"""
CALCUALTE THE COST OF BUYING AND SELLING A PROPERTY
"""
# Fees associated with cars, all in today's value
annualParking = 356.57 # parking fee 
moneyPerKm = 0.15 # gas money per Km
milagePerDay = 18 # 18 Km per day
daysPerMonth = 25 # drive 25 days
monthGasMoney = milagePerDay*daysPerMonth*moneyPerKm # gas money per month
carCost = annualParking*years + monthGasMoney*12*years # money assoicated with cars (years), today
# print("We will spend",carCost,"in parking and gas with buying a condo!!!" )

# Fees associated with buying a property
buyingFee = 2000 # lawyer and inspection fee in buying the property, today

# Fees associated with the fixed payment to bank over the years
moneyPaidBank = 0 # accumulated fixed payment to bank
for i in range(0,month): # bring money back to today's value 
    moneyPaidBank = moneyPaidBank + mortgage.moneyBackToToday(mortgage.fixedPayment,i,mortgage.monthlySavingRate)

# Fees asscoiated with property maintainence, today
monthlyCondoFee = 350 
annualPropertyTax = 3500
condoFee = month*monthlyCondoFee
propertyTax = annualPropertyTax*years
maintainanceFee = condoFee+propertyTax

# Remaining bank balance
balanceOweBank = mortgage.remainingBalance(mortgage.balance,mortgage.fixedPayment,mortgage.monthlyLoanRate,month) # money owe bank, future
# print("We still owe bank",round(balanceOweBank,2),"in future!!!")


"""
HERE WE USE BISECTION METHOD TO CALCULATE THE DEISRED SALEPRICE
"""

# USING THE BISECTION METHOD TO FIND THE NEUTRAL SALE PRICE OF THIS PROPERTY
salePriceUp = 1000000 # up bound ,future, 322500 (Buying price)
salePriceLow = 200000 # low bound
earnMoney = 0 # deisred earning from buying a property

salePirceMid = (salePriceUp+salePriceLow)/2
buyCost = costOfBuyingAndSaling(salePirceMid,balanceOweBank,moneyPaidBank,maintainanceFee,buyingFee,carCost,mortgage)
costDifference = rentCost-buyCost-earnMoney

while (abs(costDifference)>0.1):
    if costDifference>0:
        salePriceUp = salePirceMid
    else:
        salePriceLow = salePirceMid
    salePirceMid = (salePriceUp+salePriceLow)/2
    buyCost = costOfBuyingAndSaling(salePirceMid,balanceOweBank,moneyPaidBank,maintainanceFee,buyingFee,carCost,mortgage)
    costDifference = rentCost-buyCost-earnMoney
        
salePrice = salePirceMid      

print("With a selling price of",round(salePrice,2),", renting is equivalent to buying!!!")    
print("The cost in buying and selling a property is",round(buyCost,2),"at today's money value!!!")


















