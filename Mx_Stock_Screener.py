from nsetools import Nse


nifty100 = ['ADANIPORTS', 'ASIANPAINT', 'AXISBANK', 'BAJAJ-AUTO', 'BAJFINANCE', 'BAJAJFINSV', 'BPCL', 'BHARTIARTL', 'BRITANNIA', 'CIPLA', 'COALINDIA', 'DIVISLAB', 'DRREDDY', 'EICHERMOT', 'GRASIM', 'HCLTECH', 'HDFCBANK', 'HDFCLIFE', 'HEROMOTOCO', 'HINDALCO', 'HINDUNILVR', 'HDFC', 'ICICIBANK', 'ITC', 'IOC', 'INDUSINDBK', 'INFY', 'JSWSTEEL', 'KOTAKBANK', 'LT', 'M&M', 'MARUTI', 'NTPC', 'NESTLEIND', 'ONGC', 'POWERGRID', 'RELIANCE', 'SBILIFE', 'SHREECEM', 'SBIN', 'SUNPHARMA', 'TCS', 'TATACONSUM', 'TATAMOTORS', 'TATASTEEL', 'TECHM', 'TITAN', 'UPL', 'ULTRACEMCO', 'WIPRO','ACC', 'ADANIENT', 'ADANIGREEN', 'ADANITRANS', 'AMBUJACEM', 'APOLLOHOSP', 'AUROPHARMA', 'DMART', 'BAJAJHLDNG', 'BANDHANBNK', 'BANKBARODA', 'BERGEPAINT', 'BIOCON', 'BOSCHLTD', 'CADILAHC', 'CHOLAFIN', 'COLPAL', 'DLF', 'DABUR', 'GAIL', 'GLAND', 'GODREJCP', 'HDFCAMC', 'HAVELLS', 'HINDPETRO', 'ICICIGI', 'ICICIPRULI', 'IGL', 'INDUSTOWER', 'NAUKRI', 'INDIGO', 'JINDALSTEL', 'JUBLFOOD', 'LTI', 'LUPIN', 'MARICO', 'MUTHOOTFIN', 'NMDC', 'PIIND', 'PIDILITIND', 'PEL', 'PGHH', 'PNB', 'SBICARD', 'SIEMENS', 'SAIL', 'TORNTPHARM', 'MCDOWELL-N', 'VEDL', 'YESBANK']

nse = Nse()


def nifty50_scanner(choice,range):
        if choice == '1':
            for company in nifty100[0:50]:
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
                    break

        elif choice == '2':
            print("Scanning................................................................................")
            for company in nifty100[0:50]:
                quote = nse.get_quote(str(company))
                company_name = str(quote['companyName'])
                curr_price = int(quote['closePrice'])
                highest_price = int(quote['high52'])
                if curr_price > highest_price or curr_price == highest_price:
                    print(f"{company_name} : Current Price = {curr_price} : High52 = {highest_price} : Highest of All Time! \n")
                else:
                    print("Sorry! No data found for your Request\n")
                    break

def nifty100_scanner(choice,range):
        if choice == '1':
            for company in nifty100:
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
                    break
                
        elif choice == '2':
            print("Scanning................................................................................")
            for company in nifty100:
                quote = nse.get_quote(str(company))
                company_name = str(quote['companyName'])
                curr_price = int(quote['closePrice'])
                highest_price = int(quote['high52'])
                if curr_price > highest_price or curr_price == highest_price:
                    print(f"{company_name} : Current Price = {curr_price} : High52 = {highest_price} : Highest of All Time! \n")
                else:
                    print("Sorry! No data found for your Request\n")
                    break

while True:
    print("\nThis Scanner is developed by:- Mayank Kaushik©\n")
    print("Type '1' or '2' as per your Choice!   or type 'q' to quit...")
    userinp = input("Do You Want to Scan Nifty50 or Nifty100:  ")
    if userinp == 'q':
        break
    elif userinp == '1':
        choice = input("Scan Type: \n1. Value below 52week high\n 2. All time high/52 week high\nWhat Scan do you wish to perform: ")
        if choice == '2':
            nifty50_scanner(choice, range)
        else:
            range = input("Input range to see Percentage difference: 10, 20, 30 or 50: ")
            nifty50_scanner(choice, range)

    elif userinp == '2':
        choice = input("Scan Type: \n1. Value below 52week high\n 2. All time high/52 week high\nWhat Scan do you wish to perform: ")
        if choice == '2':
            nifty50_scanner(choice, range)
        else:
            range = input("Input range to see Percentage difference: 10, 20, 30 or 50: ")
            nifty100_scanner(choice, range)
    else:
        break
