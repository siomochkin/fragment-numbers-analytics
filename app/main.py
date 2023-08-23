import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup
from database import connection

url1 = 'https://fragment.com/numbers?sort=price_asc&filter=sale'
url2 = 'https://coinmarketcap.com/en/currencies/toncoin/'

try:
    while True:   
        # For fragment.com
        fragment = requests.get(url1)
        soup1 = BeautifulSoup(fragment.text, 'html.parser')
        
        # For coinmarketcap.com
        coinmarket = requests.get(url2)
        soup2 = BeautifulSoup(coinmarket.text, 'html.parser')
        
        # Find first phone number
        phone_find = str(soup1)[str(soup1).find('tm-value'):]
        phone = str(phone_find[phone_find.find('>')+1:phone_find.find('<')])

        # Find number status
        status_find = str(soup1)[str(soup1).find('status-avail'):]
        status = status_find[status_find.find('>')+1:status_find.find('<')]

        # Find price in TON
        ton_find = str(soup1)[str(soup1).find('icon-ton'):]
        ton = ton_find[ton_find.find('>')+1:ton_find.find('<')]

        # Get price($)
        price_find = str(soup2)[str(soup2).find('The live Toncoin price today'):]
        price = float(price_find[price_find.find('$')+1:price_find.find('USD')]) * float(ton)

        # Find remaining time
        data_find = str(soup1)[str(soup1).find('"text" datetime='):]
        data = data_find[data_find.find('>')+1:data_find.find('<')]
        param1 = ['days', 'day', 'hours', 'hour']
        param2 = ['minutes', 'minute', ' ']
        for i in param2:
            data = data.replace(i, '')
            for i in param1:
                data = data.replace(i, ':')
                
        # Insert data into DB
        try:
            with connection.cursor() as cursor:
                query = """INSERT INTO numbers (date, price, ton, phone, status, remaining_time) VALUES(%s, %s, %s, %s, %s, %s);"""
                values = (datetime.now(), price, ton, phone, status, data)
                cursor.execute(query, values)
                connection.commit()
                print(values)
                time.sleep(56)
        except Exception as e:
            connection.rollback()
            print('Error: ', e)
        
except Exception as e:
    connection.close()
    print('Error:', e)
