import sys
from sfa_scraper import fetch_bids

def main():
    tickers = ['TSLA', 'XOM', 'ORCL']
    bids = fetch_bids(tickers)
    print(bids)

    # it is cleaner code to break up operations into
    # well-named, descriptive/contextual variables. but we could do:
    # print(fetch_bids('TSLA', 'XOM', 'ORCL']))

if __name__ == '__main__':
    sys.exit(main())
