import sys
import os
import requests
import time
from datetime import datetime
from pytz import timezone
from twilio.rest import Client


def main():
    api_key = os.environ['ALPHAVANTAGE_KEY']
    twilio_key = os.environ['TWILIO_KEY']
    ticker = 'MSFT'
    url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + ticker + '&apikey=' + api_key

    opening_value = get_global_quote(url)['Global Quote']['02. open']
    closing_time = get_closing_time()

    time.sleep(5)
    i = 0

    while get_eastern_timestamp() <  closing_time:
        print(i)
        time.sleep(7)

        try:
            current_price = get_global_quote(url)['Global Quote']['05. price']
        except KeyError as ke:
            print(ke)
            time.sleep(60)
            pass

        if float(current_price) < float(opening_value)*0.9:
            send_sms(twilio_key, ticker)

        i += 1


def get_global_quote(url):
    return requests.get(url).json()

def send_sms(twilio_key, ticker):
    account_sid = "ACc459d67f5cd24c3b70c39cefa7f003b9"
    client = Client(account_sid, twilio_key)
    message = client.messages.create(
        to="+16236288983",
        from_="+12094975129",
        body="Sell " + ticker + "now!")

def get_closing_time():
    tz = timezone('EST')
    timestamp = datetime.now(tz)
    day = int(timestamp.strftime('%d'))
    month = int(timestamp.strftime('%m'))
    year = int(timestamp.strftime('%Y'))
    dt = datetime(year, month, day, 17, 00, 00, tzinfo=tz)
    closing_timestamp = time.mktime(dt.timetuple())
    return int(closing_timestamp)

def get_eastern_timestamp():
    tz = timezone('EST')
    dt = datetime.now(tz)
    timestamp = time.mktime(dt.timetuple())
    return int(timestamp)


if __name__ == '__main__':
    sys.exit(main())
