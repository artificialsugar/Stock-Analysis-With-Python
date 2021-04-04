# Defining function to calculate PEG Ratio

def pegRatio():

# While True loop to repeat prompt until appropriate user input is given

  while True:

    print("\nEnter exit if you want to end the program...")

    tickerSymbol = input("Enter the ticker symbol of the stock that you would like to analyze: ")

# Making sure user input string is letters only

    while not tickerSymbol.isalpha():

      print("\nPlease enter ticker symbols using only letters and in the following format: MFST")

      print("\nEnter exit if you want to end the program...")

      tickerSymbol = input("Enter the ticker symbol of the stock you are analyzing: ")

# Giving user an option to exit program

    if tickerSymbol == "exit":

# Ending function

      return

# Breaking first while loop

    break

# A second while true loop to repeat next prompt until appropriate user input is given

  while True:

    sharePrice = input("\nEnter the current share price: ")

# Giving user an option to exit program

    if sharePrice == "exit":

# Ending function

      return

# Using ASCII table to check if string from prompt contains only numbers or periods

    for char in sharePrice:

      if ord(char) is not range(47,58) or ord(46):

# Attempting to convert string to float

        try:

          sharePrice = float(sharePrice)

# Using an exception for incalculable values 

        except ValueError:

          print("\nPlease enter share price using only numbers greater than 0 and in the following format: 1.23")

          sharePrice = input("\nEnter the current share price: ")

# Breaking second while loop

    break

# A third while true loop to repeat next prompt until appropriate user input is given

  while True:

    eps = input("\nEnter earnings per share for the last year: ")

# Giving user an option to exit program

    if eps == "exit":

# Ending function

      return

# Using ASCII table to check if string from prompt contains only numbers or periods

    for char in eps:

      if ord(char) is not range(47,58) or ord(46):

# Attempting to convert string to float

        try:

          eps = float(eps)

# Using an exception for incalculable values 

        except ValueError:

          print("\nPlease enter share price using only numbers greater than 0 and in the following format: 1.23")

          eps = input("\nEnter earnings per share for the last year: ")

# PEG Ratio cannot be calculated if eps is 0 or less.

    if eps <= 0:

      print("\nThe PEG Ratio cannot be calculated")

# Calculating P/E Ratio

    else:

      priceToEarningsRatio = sharePrice / eps

# Breaking third while loop

      break

# A fourth while true loop to repeat next prompt until appropriate user input is given

  while True:
      
    expectedEPS = input("\nEnter in expected earnings per share for next year: ")

# Giving user an option to exit program

    if expectedEPS == "exit":

# Ending function

      return

# Using ASCII table to check if string from prompt contains only numbers or periods

    for char in expectedEPS:

      if ord(char) is not range(47,58) or ord(46):

# Attempting to convert string to float

        try:

          expectedEPS = float(expectedEPS)

# Using an exception for incalculable values 

        except ValueError:

          print("\nPlease enter share price using only numbers greater than 0 and in the following format: 1.23")

          expectedEPS = input("\nEnter in expected earnings per share for next year: ")

# Calculating EPS growth rate

        changeEPS1 = expectedEPS - eps

        changeEPS2 = changeEPS1 / eps

        epsGrowthRate = round((changeEPS2 * 100), 2)
        
        PEGRatio = round((priceToEarningsRatio / epsGrowthRate), 2)

# Printing results

      print("\nThe PEG Ratio for " + str(tickerSymbol) + " is: " + str(PEGRatio) + "\n")

# Ending function

      return

# Calling function

pegRatio()