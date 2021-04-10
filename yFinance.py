# Importing libraries.

import matplotlib.pyplot as plt

import yfinance as yf

# Defining function to graph revenue.

def graphRevenue():

    plt.figure(figsize=(8,7))
    rects1 = plt.bar(quarter,qRevenue)
    plt.title('Quarterly Revenue')
    plt.xlabel('Quarter')
    plt.ylabel('Quarterly Revenue (thousands)')

# Adding labels.

    def autolabel(rects):
            
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width()/2., height + 5, height, ha='center', va='bottom')

    autolabel(rects1)
    plt.show()

# Accessing general data for PTQ.V from Yahoo Finance.

ptq = yf.Ticker("PTQ.V")

# Creating quarterly earnings database.

qHist = ptq.quarterly_earnings

# Creating empty lists.

quarter = []

qRevenue = []

# Accessing desired information from quarterly earnings database and adding to empty lists.

for index, row in qHist.iterrows():
    qRevenue.append(int(row['Revenue']/1000))

for index, row in qHist.iterrows():
    quarter.append(index)  

# Calling function.

graphRevenue()




