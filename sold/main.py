import requests
from datetime import datetime
from bs4 import BeautifulSoup

# Parsing values that we need
def get_data_between_markers(data, start_marker, end_marker):
    start_index = data.find(start_marker)
    if start_index == -1:
        return None
    end_index = data.find(end_marker, start_index)
    if end_index == -1:
        return None
    content = data[start_index + len(start_marker):end_index]
    return content

# Get parsed data from url
def get_parsed_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

# Get phone number from parsed data
def get_phone_number(soup):
    phone_find = str(soup)[str(soup).find('tm-value'):]
    phone = get_data_between_markers(phone_find, '>', '<')
    return phone

# Get number status
def get_number_status(soup):
    status_find = str(soup)[str(soup).find('tm-status'):]
    status = get_data_between_markers(status_find, '>', '<')
    return status

# Get price 
def get_price_in_ton(soup):
    ton_find = str(soup)[str(soup).find('icon-ton'):]
    ton = get_data_between_markers(ton_find, '>', '<')
    return ton

# Get time
def get_sold_time(soup):
    data_find = str(soup)[str(soup).find('datetime='):]
    data = get_data_between_markers(data_find, '>', '<')
    data = data.replace('at ', '')
    return data

def get_remaining_time(soup):
    data_find = str(soup)[str(soup).find('data-relative="text"'):]
    data = get_data_between_markers(data_find, '>', '<')
    param1 = ['days', 'day', 'hours', 'hour']
    param2 = ['minutes', 'minute', ' ']
    for i in param2:
        data = data.replace(i, '')
        for i in param1:
            data = data.replace(i, ':')
    return data

# Get converted time
def convert_to_datetime_and_format(date_string):
    data_datetime = datetime.strptime(date_string, '%d %b %Y %H:%M')
    formatted_data = data_datetime.strftime('%Y-%m-%d %H:%M')
    return formatted_data
