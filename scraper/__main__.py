import sys
from sfa_scraper import get_stock_bids, get_market_caps

def main():
    company_info = {}

    tickers = ['TSLA', 'XOM', 'ORCL']
    bids = get_stock_bids(tickers)
    market_caps = get_market_caps(tickers)

    company_info.update(bids)
    for ticker in tickers:
        company_info[ticker]['Market Cap'] = market_caps[ticker]['Market Cap']

    print(company_info)


if __name__ == '__main__':
    sys.exit(main())
