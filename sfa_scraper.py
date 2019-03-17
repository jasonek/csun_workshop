from urllib.request import urlopen
from bs4 import BeautifulSoup

summary_url = 'https://finance.yahoo.com/quote/TSLA?p=TSLA'
print(summary_url)

response = urlopen(summary_url)
print(response)

for key, value in response.headers.items():
    print(key + ": " + value)
# Notice how similar it is to:  `curl -I -XGET https://finance.yahoo.com/quote/TSLA?p=TSLA`
