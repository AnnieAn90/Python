# -*- coding: utf-8 -*-
"""
PLOTTING 
"""
# allows me to reference any library procedures as plt.<procName>
import pylab as plt # plt -> plot, imported pylab into the name plt

# generate some example data
mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0,30):
    mySamples.append(i) # x values
    myLinear.append(i) # y values　
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
    
# ALL PLOTS ON ONE GRAPH
#plt.plot(mySamples,myLinear) # x,y
#plt.plot(mySamples,myQuadratic)
#plt.plot(mySamples,myCubic)
#plt.plot(mySamples,myExponential)

# PLOTS ONSEPARATE GRAPHS / PROVIDEING LABELS
plt.figure('lin')
plt.xlabel('sample points') # labels
plt.ylabel('linear function')
plt.plot(mySamples,myLinear) 

plt.figure('quad')
plt.plot(mySamples,myQuadratic)

plt.figure('cube')
plt.xlabel('sample points')
plt.ylabel('cubic function')
plt.plot(mySamples,myCubic)

plt.figure('expo')
plt.xlabel('sample points')
plt.ylabel('exponential function')
plt.plot(mySamples,myExponential)

plt.figure('quad') # open the quad figure and we add label inside of it
plt.xlabel('sample points')
plt.ylabel('quadratic function')

# ADDING TITLES/ CHANGE SCALES
plt.figure('lin')
plt.clf() # clear the previous windows, such as x, y labels
plt.ylim(0,1000) # set limits on the axis or axes
plt.plot(mySamples,myLinear) 
plt.title('Linear')

plt.figure('quad')
plt.clf()
plt.ylim(0,1000)
plt.plot(mySamples,myQuadratic)
plt.title('Quadratic')

plt.figure('cube')
plt.clf()
plt.plot(mySamples,myCubic)
plt.title('Cubic')

plt.figure('expo')
plt.clf()
plt.plot(mySamples,myExponential)
plt.title('Exponential')

# OVERLAYING PLOTS/ ADD LABELS / COLOR AND STYLE / LINE WIDETH
# very similar to matlab, see documentation for choices of color and style
plt.figure('lin quad')
plt.clf()
plt.plot(mySamples,myLinear,'b-',label = 'linear', linewidth=2.0) # add legend
plt.plot(mySamples,myQuadratic,'ro', label = 'quadratic', linewidth=3.0)
plt.yscale('log') # change to log scale
plt.legend(loc = 'upper left') # specify label location
plt.title('Linear vs. Quadratic')
 
plt.figure('cube exp')
plt.clf()
plt.plot(mySamples,myCubic,'g^',label = 'cubic', linewidth=4.0 )
plt.plot(mySamples,myExponential,'r--', label = 'exponential', linewidth=5.0)
plt.legend() # let python decides what is the best location, necessary
plt.title('Cubic vs. Exponential')


# USING SUBPLOTS
plt.figure('lin quad')
plt.clf()
plt.subplot(211) # 2 rows 1 column 1st location
plt.ylim(0,900)
plt.plot(mySamples,myLinear,'b-',label = 'linear', linewidth=2.0) # add legend
plt.subplot(212)
plt.ylim(0,900)
plt.plot(mySamples,myQuadratic,'ro', label = 'quadratic', linewidth=3.0)
plt.legend(loc = 'upper left') # specify label location
plt.title('Linear vs. Quadratic')
 

plt.figure('cube exp')
plt.clf()
plt.subplot(121) # 1 row 2 columns 1st location
plt.ylim(0,140000)
plt.plot(mySamples,myCubic,'g^',label = 'cubic', linewidth=4.0 )
plt.subplot(122)
plt.ylim(0,140000)
plt.plot(mySamples,myExponential,'r--', label = 'exponential', linewidth=5.0)
plt.legend() # let python decides what is the best location, necessary
plt.title('Cubic vs. Exponential')

"""
AN EXAMPLE
"""
def retire(monthly,rate, terms):
    savings = [0]
    base = [0]
    mRate = rate/12
    for i in range(terms):
        base += [i] # addition in list
        savings += [savings[-1]*(1+mRate)+monthly]
    return base, savings # returning two elements

# constant rate, varying monthlies
def displayRetireWMonthlies(monthlies, rate, terms):
    plt.figure('retireMonth')
    plt.clf() # clear frame for reuse
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label = 'retire:'+str(monthly))
        plt.legend(loc = 'upper left')

displayRetireWMonthlies([500,600,700,800,900,1000,1100], 0.05, 40*12)

# constant monthly, varying rates
def displayRetireWRates(month, rates, terms):
    plt.figure('retireRate')
    plt.clf() # clear frame for reuse
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals, yvals, label = 'retire:'+str(month)+ ':'+str(int(rate*100)))
        plt.legend(loc = 'upper left')
        
displayRetireWRates(800,[.03, .05, .07], 40*12)


def displayRetireWMonthsAndRates(monthlies, rates, terms):
    plt.figure('retireBoth')
    plt.clf()
    plt.xlim(30*12, 40*12) # focus on last 10 years
    # we can use in Matlab plot
    monthLabels = ['r','b','g','k'] 
    rateLabels = ['-','o','--']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        monthLabel = monthLabels[i%len(monthLabels)] # nice trick, remainder func cycle those labels
        for j in range(len(rates)):
            rate = rates[j]
            rateLabel = rateLabels[j%len(rateLabels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals,yvals, monthLabel+rateLabel, label = 'retire:'+str(monthly)+ ':'+str(int(rate*100)))
            plt.legend(loc = 'upper left')
            
displayRetireWMonthsAndRates([500,700,900,1100],[.03, .05, .07], 40*12)













