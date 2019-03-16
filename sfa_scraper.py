from urllib.request import urlopen

summary_url = 'https://finance.yahoo.com/quote/TSLA?p=TSLA'
print(summary_url)

summary_page = urlopen(summary_url)
print(summary_page)
