# -*- coding: utf-8 -*-
"""
THIS CODE COMPUTES THE FIXED MONTHLY PAYMENT THAT REQUIRED TO PAYOFF THE BALANCE 
USING BYSECTION SEARCH IN A 25 YEARS PERIOD
"""
def mortgageCalculator(years,price,downPaymentPercentage,loanRate):
    
    def remainingBalance(balance,fixedPayment,monthlyLoanRate,month):
        """
        RETURN THE BALANCE AFTER A FIXED MONTHLY PAYMENT AND MONTHLY LOAN RATE
        balance: money remaining
        fixedPayment: monthly payment
        monthlyLoanRate: monthly loan rate, annual rate divide by 12
        month: mortgage payment month
        """
        for i in range(0,month):
            # uppaids balance after a monthly payment
           unpaidBalance = balance - fixedPayment
           # still owe bank money, calcualte the interest before next payment
           if unpaidBalance >0:
               interest = unpaidBalance*monthlyLoanRate
           else:
               interest = 0
           # new balance is the remaining balnace plus the interest
           balance = unpaidBalance+interest
        return balance
        
    """
    CALCULATE THE MONTHLY PAYMENT
    """
    #years = 25 # 25 years
    month = years*12 # payment month
    #price = 322500 # house price ， 322500
    #downPaymentPercentage = 0.35 # downpayment percentage
    downPayment = downPaymentPercentage*price
    balance = price-downPayment # money you owe bank
    
    #loanRate = 0.0289 # annual loan rate
    monthlyLoanRate = loanRate/12 # monthly loan rate
    
    # set lo/up bounds for finding the fixed monthly payment
    lobound = balance/month
    upbound = (balance*(1+monthlyLoanRate)**month)/month
    
    # start bisection search
    mid = (lobound + upbound)/2
    # check the new balance after this "mid" fixed monthly payment for 25 years
    newBalance = remainingBalance(balance,mid,monthlyLoanRate,month)
    
    # Using the bisection method to find a fixed payment solution
    while abs(newBalance)> 0.001:
        if newBalance > 0:
            lobound = mid
        else:
            upbound = mid
        mid = (lobound + upbound)/2
        newBalance = remainingBalance(balance,mid,monthlyLoanRate,month)
        #print("Balance is ",newBalance)     
        
    # mid is out fixed payment solution, and print out our monthly payment
    return round(mid,2)

def moneyBackToToday(payment,monthBack,monthlySavingRate):
    """
    THIS FUNCITON RETURNS MONEY BACK TO TODAY'S VALUE
    payment: future money at a certain pay period
    monthBack: bring how many month back 
    monthlySavingRate: monthly rate you can earn
    """
    if monthBack==0:
        return payment
    else:
        return payment/pow(1+monthlySavingRate,monthBack)
    

"""
This condition prevents execution in this section unless this script is run as a
main program. The intepreter assins a name to the variable _name_ before it executes
the script. If the script is main, then the name _main_ is assigned to the _name_. 
If this file imported by other file, its own name "mortgage" is assigned to __name__
"""
if __name__ == '__main__':
    years = 25 # 25 years
    price = 965000 # house price ， 322500
    downPaymentPercentage = 0.414 # downpayment percentage
    loanRate = 0.065 # annual loan rate
    month = years*12
    # downPayment = price*downPaymentPercentage
    downPayment = 400000 
    
    # recall the moortgage calculation function
    fixedPayment = mortgageCalculator(years,price,downPaymentPercentage,loanRate)
    print("With a monthly Payment of",str(fixedPayment)+", you can pay off you loan in",str(years), "years!!!")
    
    
    """
    CALCULATE HOW MUCH MONEY YOU ACTUALLY SPEND FOR BUY THIS PORPERTY
    """
    savingRate = 0.02 # annual saving interest rate
    monthlySavingRate = savingRate/12 # minimum monthly interest you can get
    # Set initial condition
    moneyToday = 0
    
    # Find equivalent money at today's value 
    for i in range(0,month):
        moneyToday = moneyToday + moneyBackToToday(fixedPayment,i,monthlySavingRate)
    
    totalPropertyPayment =round(moneyToday+downPayment,2)
    print("We will pay in total",totalPropertyPayment, "at today's value!!!" )
    















