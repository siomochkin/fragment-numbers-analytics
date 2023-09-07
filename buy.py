import time
import csv
from sold.main import *
from datetime import datetime

def main():
    url_fragment = 'https://fragment.com/numbers?sort=price_asc&filter=sale'
    url_coinmarket = 'https://coinmarketcap.com/en/currencies/toncoin/'
    
    while True:   
        try:
            # For fragment.com
            fragment = get_parsed_data(url_fragment)
                
            # For coinmarketcap.com
            coinmarket = get_parsed_data(url_coinmarket)
                
            phone = get_phone_number(fragment)
            status = get_number_status(fragment)
            ton = get_price_in_ton(fragment)

            price_data = get_price_in_dollars(coinmarket)
            price = float(price_data) * float(ton)

            data = get_remaining_time(fragment)
            
            values = (str(datetime.now()), str(data), round(price, 2), ton, str(phone), str(status))

            with open('buy-numbers.csv', 'a+') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(values)
                print(values)
            
            time.sleep(55)
        
        except Exception as e:
            print(e)
            
        finally:
            continue
       
if __name__ == '__main__':
    main()
