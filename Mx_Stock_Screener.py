import csv
from nsetools import Nse
import requests

'''
YOU MUST NEED TO DOWNLOAD NIFTY50 CSV FILE TO BEGIN WITH AND PLACE THE FILE IN SAME FOLDER AS YOU PLACE THIS PYTHON FILE

LINK TO DOWNLOAD FILE: https://www1.nseindia.com/content/indices/ind_nifty50list.csv 

NIFTY NEXT 50 : https://www1.nseindia.com/content/indices/ind_niftynext50list.csv 

'''


with open('ind_nifty50list.csv', "r") as s:    
    reader = csv.DictReader(s)
    for column in reader:
        nifty50 = column['Symbol']
        print(nifty50)
    
# nse = Nse()
# print(nse)

# nifty50 = nse.get_stock_codes('NIFTY 50')

# print(nifty50)

# quote = nse.get_quote('sbin')
# print(quote)

# print(quote['companyName'])
# print("52 week High: " +str(quote['high52']))
# print("52 week Low: " + str(quote['low52']))

# print("Current Price : " + str(quote['closePrice']))