# Changing the data type of each item in a list using the map() function

yearList = ['2017', '2018', '2019']

def strToNum(str):

    return int(str)

yearListFloat = map(strToNum,yearList)

print(list(yearListFloat))
