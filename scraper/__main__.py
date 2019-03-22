import sys
from sfa_scraper import get_stock_bids, get_market_caps

def main():
    tickers = ['TSLA', 'XOM', 'ORCL']
    market_caps = get_market_caps(tickers)
    print(market_caps)

    # it is cleaner code to break up operations into
    # well-named, descriptive/contextual variables. but we could do:
    # print(get_stock_bids('TSLA', 'XOM', 'ORCL']))


if __name__ == '__main__':
    sys.exit(main())
