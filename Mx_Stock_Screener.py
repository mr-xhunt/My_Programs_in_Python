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

def mx_int_scan(scan_type, range):
    if scan_type == "1":
        print("Scanning................................................................................")
        for company in nifty50:
            quote = nse.get_quote(str(company))
            company_name = str(quote['companyName'])
            curr_price = int(quote['closePrice'])
            highest_price = int(quote['high52'])
            if curr_price > highest_price or curr_price == highest_price:
                print(f"{company_name} : Current Price = {curr_price} : High52 = {highest_price} : Highest of All Time! \n")
            else:
                print("Sorry! No data found for your Request\n")
                break


    elif scan_type == "2":
        print("Scanning................................................................................")
        for company in nifty50:
            quote = nse.get_quote(str(company))
            company_name = str(quote['companyName'])
            curr_price = int(quote['closePrice'])
            highest_price = int(quote['high52'])
            if range == "10":
                if curr_price < (highest_price - highest_price*0.1):
                    print(f"{company_name} : Current Price = {curr_price} : High52 = {highest_price} : 10 Percent Lesser than High \n")
            elif range == "20":
                if curr_price < (highest_price - highest_price*0.2):
                    print(f"{company_name} : Current Price = {curr_price} : High52 = {highest_price} : 20 Percent Lesser than High\n")
            elif range == "30":
                if curr_price < (highest_price - highest_price*0.3):
                    print(f"{company_name} : Current Price = {curr_price} : High52 = {highest_price} : 30 Percent Lesser than High\n")
            elif range == "50":
                if curr_price < (highest_price - highest_price*0.5):
                    print(f"{company_name} : Current Price = {curr_price} : High52 = {highest_price} : 50 Percent Lesser than High\n")
            else:
                print("Invalid Command")
    else:
        print("Invalid Command")



while True:
    inp = input("What type of scan you want to perform!: \n1. Upward Scan \n 2. Lower Scan\n Type 'q' to quit or '-h' for help:  ")
    if inp == "q":
        break
    elif inp == "-h" or inp == 'help':
        print("Upward Scan: Scan Stocks which is at all time high\n Lower Scan: Scan Stocks Which are lower than all time high\n You can use 10, 20,30,50 to view Percentange difference.")
    elif inp == "1":
        mx_int_scan(inp,range)
    elif inp == "2":
        range = input("Type 10, 20, 30 or 50 to view Percentage Difference!\nEnter the Percent Difference to Scan: ")
        mx_int_scan(inp,range)
    else:
        print("Invalid")
        break
