from urllib.request import urlopen
from bs4 import BeautifulSoup

summary_url = 'https://finance.yahoo.com/quote/TSLA?p=TSLA'
print(summary_url)

response = urlopen(summary_url)
print(response)

print(response.code)
print(response.url)
