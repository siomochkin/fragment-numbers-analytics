import time
import csv
from main import *


def main():
    url_fragment = 'https://fragment.com/numbers?sort=ending&filter=sold'
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

            price_data = str(coinmarket)[str(coinmarket).find('The live Toncoin price today'):]
            price = float(price_data[price_data.find('$')+1:price_data.find('USD')]) * float(ton)

            sold_time = get_sold_time(fragment)
            formatted_sold_time = convert_to_datetime_and_format(sold_time)
            
            values = (formatted_sold_time, round(price, 2), ton, phone, status)

            with open('sold-numbers.csv', 'a+') as file:
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
