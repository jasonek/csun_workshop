import sys
import os
import json
import requests

def main():
    api_key = os.environ['ALPHAVANTAGE_KEY']
    ticker = 'MSFT'
    summary_url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + ticker +'&apikey=' + api_key
    response = requests.get(summary_url)
    json_data = json.loads(response.text)
    print(json_data)


if __name__ == '__main__':
    sys.exit(main())
