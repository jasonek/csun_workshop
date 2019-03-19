from urllib.request import urlopen
from bs4 import BeautifulSoup

companies = ['TSLA', 'XOM', 'ORCL']
stock_bids = {}

for company in companies:
    summary_url = 'https://finance.yahoo.com/quote/' + company + '?p=' + company

    response = urlopen(summary_url)

    tsla_html = BeautifulSoup(response, "html.parser")

    qt = tsla_html.find(id = "quote-summary")
    bid = qt.find(attrs={"data-test":"BID-value"}).getText()

    bid_list = bid.split('x')
    new_list = []
    for item in bid_list:
        item = item.strip()
        item = float(item)
        new_list.append(item)
    price, volume = new_list

    print("The bid price is {} and current volume is {}".format(price, volume))

    stock_bids[company] = {"bid" : price, "volume": volume}

print(stock_bids)
