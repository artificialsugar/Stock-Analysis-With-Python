# Defining function 

def revenuePerShare():

  while True:

    try:

# Getting company revenue as user input, converting to float

      companyRevenue = float(input("\nEnter company revenue: "))

# Getting outstanding shares as user input, converting to float

      outstandingShares = float(input("\nEnter outstanding shares: "))

# Calculating revenue per share annd rounding it to 2 decimals
      
      revenuePerShare = round((companyRevenue / outstandingShares), 2)

# If statements and exceptions for faulty user input

      if companyRevenue and outstandingShares > 0:

        print("\nRevenue per share: " + "$" + str(revenuePerShare) + "\n")

# Ending while loop

        break

      elif companyRevenue == 0:

        print("\nRevenue per share: 0")

    except ZeroDivisionError:

      print("\nPlease enter numbers greater than 0")
        
    except ValueError:

      print("\nPlease enter numbers only")

# Continuing while loop

      continue

# Calling revenuePerShare function

revenuePerShare()