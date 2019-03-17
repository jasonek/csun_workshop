from urllib.request import urlopen
from bs4 import BeautifulSoup

summary_url = 'https://finance.yahoo.com/quote/TSLA?p=TSLA'

response = urlopen(summary_url)

tsla_html = BeautifulSoup(response, "html.parser")
