from nsetools import Nse
import pandas as pd

'''
YOU MUST NEED TO DOWNLOAD NIFTY50 CSV FILE TO BEGIN WITH AND PLACE THE FILE IN SAME FOLDER AS YOU PLACE THIS PYTHON FILE

LINK TO DOWNLOAD FILE: https://www1.nseindia.com/content/indices/ind_nifty50list.csv 

NIFTY NEXT 50 : https://www1.nseindia.com/content/indices/ind_niftynext50list.csv 

'''


data = pd.read_csv("ind_nifty50list.csv")
df = data.head(50)
  
nifty50 = df["Symbol"].tolist()


nse = Nse()

def mx_int_scan():
    for company in nifty50:
        quote = nse.get_quote(str(company))
        company_name = str(quote['companyName'])
        curr_price = str(quote['closePrice'])
        highest_price = str(quote['high52'])
        lowest_price = str(quote['low52'])
        print(f"{company_name} : Current Price = {curr_price} : High52 = {highest_price} : Low52 = {lowest_price} ")


mx_int_scan()
