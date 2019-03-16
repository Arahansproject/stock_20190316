from urllib.request import urlopen
from bs4 import BeautifulSoup

page = urlopen('https://finance.naver.com/marketindex/')
soup = BeautifulSoup(page, 'html.parser')
print(soup.prettify())

soup.find_all('span', 'value')[0].string

# '1,121.00'