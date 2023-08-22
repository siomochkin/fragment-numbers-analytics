import requests
from bs4 import BeautifulSoup

url = 'https://fragment.com/numbers?sort=price_asc&filter=sale'

r = requests.get(url, timeout=60)
soup = BeautifulSoup(r.text, 'html.parser')

print(soup)

# with open('parse.txt', 'w+') as file:
#     file.write(str(soup))
