from urllib.request import urlopen
from bs4 import BeautifulSoup

companies = ['TSLA']

summary_url = 'https://finance.yahoo.com/quote/' + companies[0] + '?p=' + companies[0]

response = urlopen(summary_url)

tsla_html = BeautifulSoup(response, "html.parser")

quote = tsla_html.find("div", {"id": "quote-summary"})
# OR you can do this more directly
qt = tsla_html.find(id = "quote-summary")
bid = qt.find(attrs={"data-test":"BID-value"}).getText()
price, volume = bid.split('x')
print("The bid price is {} and current volume is {}".format(price, volume))

stock_bids = {}

stock_bids[companies[0]] = {"bid" : price, "volume": volume}
