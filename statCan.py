# Practice processing data from Stats Canada

# Importing numpy and gspread

import numpy as np

import gspread 

# Creating service account, opening spreadsheet.

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1Emsm4D7hXs3jSej4sqkDwp31nfLMoRY7liC8HkaMwcE')

worksheet = sh.sheet1

# Accessing data from Google Sheets

priceList = worksheet.get('B10:B237')

# Creating an empty list

newList = []

# Iterating through priceList and adding data to newList

for data in priceList:

    newList.append(int(data[0]))

# Spliting newList into 19 lists 

newarr = np.array_split(newList, 19)

# Presenting data with relevant year

year = 1999

for data in newarr:

    total = 0

    year += 1

    if year < 2021:

        for i in data:

            total = total + int(i)

        print('The total amount of canola exported in', year, 'was', total, 'tonnes')