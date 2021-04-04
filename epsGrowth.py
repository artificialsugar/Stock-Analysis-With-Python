#CALCULATES EARNINGS PER SHARE (EPS) Growth

# Lists entered as strings as an example of data coming from Google Sheets
# Empty lists are needed for both strToNum() and calcEPSGrowth() functions 
# It is possible to add more years to yearList and more annual EPS to epsList.
# Positions of EPS should corrospond to positions of respective years.  
# Example: In 2017, company abc had a loss (-0.32) of earnings per share 

yearList = ['2017', '2018', '2019']
yearListFloat = []
epsList = ['-0.32', '0.25', '-0.09']
epsListFloat = []
epsListRounded = []

# Defining a function that changes list data types from strings to integers and floats 

def strToNum():

# For loops iterate over lists and add a changed data type to a new list

    for string in yearList:
        yearListFloat.append(int(string))

    for string in epsList:
        epsListFloat.append(float(string))


# Defining a function that calculates EPS growth using a counter to cycle through lists

def calcEPSGrowth():
    
    j = 1

# Creating a for loop for epsListFloat list

    for i in epsListFloat:

# If statement setting conditions for counter.  Loop will continue twice until length of epsListFloat is reached (3 elements - 1 element = twice)

            if j <= len(epsListFloat)-1:

# Creating variable that holds j (value of 1st position which is 0.25 to start) minus i (value of index 0 which is -0.32).

                unRounded = (epsListFloat[j] - i)

# Using calculation in unRounded and dividing by i, (abs() function turns i positive).
                
                growth = unRounded / abs(i)

# Multiplying growth by 100, rounding it to 2 decimal places, and changing it to an integer (storing answer in roundPercent)

                roundPercent = int(round((growth * 100), 2))

# Creating a new list by adding roundPercent to an empty list called epsListRounded
            
                epsListRounded.append(roundPercent)

# Inceasing counter by 1, 

                j += 1

# Defining a function that neatly displays information from new lists 
                
def presentation():
    
    j = 1

# For loop controlling for how many years information is given

    for i in epsListRounded:

# Creating easily understood output for each year 

        print("EPS growth in " + str(yearListFloat[j]) + ": " + str(i) + "%")

# Inceasing counter by 1, 

        j += 1

# Calling functions

strToNum()

calcEPSGrowth()

presentation()

