from urllib.request import urlopen
from bs4 import BeautifulSoup

summary_url = 'https://finance.yahoo.com/quote/TSLA?p=TSLA'

response = urlopen(summary_url)

tsla_html = BeautifulSoup(response, "html.parser")

quote = tsla_html.find("div", {"id": "quote-summary"})
# OR you can do this more directly
qt = tsla_html.find(id = "quote-summary")
price, volume = bid.split('x')
print("The bid price is {} and current volume is {}".format(price, volume))
