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

    html = BeautifulSoup(response, "html.parser")

    quote = html.find(id = "quote-summary")
    bid = quote.find(attrs={"data-test":"BID-value"}).getText()

    return [float(item) for item in bid.split('x')]


def get_market_caps(companies):
    stock_mkt_caps = {}

    for company in companies:
        mkt_cap = fetch_market_cap(company)
        print("The market cap of {} is {} ".format(company, mkt_cap))

        stock_mkt_caps[company] = {"Market Cap" : mkt_cap}

    return stock_mkt_caps


def fetch_market_cap(ticker):
    summary_url = 'https://finance.yahoo.com/quote/' + ticker + '?p=' + ticker
    response = urlopen(summary_url)

    html = BeautifulSoup(response, "html.parser")

    quote = html.find(id = "quote-summary")
    market_cap = quote.find(attrs={"data-test":"MARKET_CAP-value"}).getText()

    mkt_cap = parse_market_cap(market_cap)
    return mkt_cap

def parse_market_cap(string):
    multipliers = {'K':1000, 'M':1000000, 'B':1000000000}

    if string[-1].isdigit(): # check if no suffix
        return int(string)

    letter = string[-1]
    string = string[:-1]
    mult = multipliers[letter]

    return float(string) * int(mult)
