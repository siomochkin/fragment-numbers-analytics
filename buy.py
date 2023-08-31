import time
import csv
from sold.main import *
from datetime import datetime

def main():
    url_fragment = 'https://fragment.com/numbers?sort=price_asc&filter=sale'
    url_coinmarket = 'https://coinmarketcap.com/en/currencies/toncoin/'

    while True:   
        # For fragment.com
        fragment = get_parsed_data(url_fragment)
            
        # For coinmarketcap.com
        coinmarket = get_parsed_data(url_coinmarket)
            
        phone = get_phone_number(fragment)
        status = get_number_status(fragment)
        ton = get_price_in_ton(fragment)

        price_data = str(coinmarket)[str(coinmarket).find('The live Toncoin price today'):]
        price = float(price_data[price_data.find('$')+1:price_data.find('USD')]) * float(ton)

        data = get_remaining_time(fragment)
        
        values = (str(datetime.now()), str(data), str(price), str(ton), str(phone), str(status))

        with open('numbers.csv', 'a+') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(values)
            print(values)
        
        time.sleep(60)
       
if __name__ == '__main__':
    main()
