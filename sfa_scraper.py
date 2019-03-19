from urllib.request import urlopen
from bs4 import BeautifulSoup

def fetch_bids(companies):
    stock_bids = {}

    for company in companies:
        summary_url = 'https://finance.yahoo.com/quote/' + company + '?p=' + company

        response = urlopen(summary_url)

        tsla_html = BeautifulSoup(response, "html.parser")

        qt = tsla_html.find(id = "quote-summary")
        bid = qt.find(attrs={"data-test":"BID-value"}).getText()

        price, volume = [float(item) for item in bid.split('x')]

        print("The bid price is {} and current volume is {}".format(price, volume))

        stock_bids[company] = {"bid" : price, "volume": volume}
        return stock_bids
