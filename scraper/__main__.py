import sys
from sfa_scraper import get_stock_bids, fetch_bid

def main():
    tickers = ['TSLA', 'XOM', 'ORCL']
    bids = get_stock_bids(tickers)
    print(bids)

    # it is cleaner code to break up operations into
    # well-named, descriptive/contextual variables. but we could do:
    # print(get_stock_bids('TSLA', 'XOM', 'ORCL']))

    print(fetch_bid('AAPL'))

if __name__ == '__main__':
    sys.exit(main())
