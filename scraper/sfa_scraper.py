from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_stock_bids(companies):
    stock_bids = {}

    for company in companies:
        price, volume = fetch_bid(company)
        print("The bid price is {} and current volume is {}".format(price, volume))

        stock_bids[company] = {"bid" : price, "volume": volume}

    return stock_bids


def fetch_bid(ticker):
        summary_url = 'https://finance.yahoo.com/quote/' + ticker + '?p=' + ticker
        response = urlopen(summary_url)

        tsla_html = BeautifulSoup(response, "html.parser")

        qt = tsla_html.find(id = "quote-summary")
        bid = qt.find(attrs={"data-test":"BID-value"}).getText()

        return [float(item) for item in bid.split('x')]
