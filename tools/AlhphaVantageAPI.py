import json
import requests
import asciichartpy

from rich.traceback import install
install(show_locals=True)

major_corporation_codes = [
    "AAPL",   # Apple Inc.
    "MSFT",   # Microsoft Corporation
    "AMZN",   # Amazon.com Inc.
    "GOOGL",  # Alphabet Inc. (Google)
    "FB",     # Facebook, Inc.
    "TSLA",   # Tesla, Inc.
    "BRK.B",  # Berkshire Hathaway Inc.
    "JPM",    # JPMorgan Chase & Co.
    "JNJ",    # Johnson & Johnson
    "V",      # Visa Inc.
    "BLK",    # BlackRock, Inc.
]

base_url = 'https://www.alphavantage.co/query'
function = 'TIME_SERIES_DAILY'
output_size = 'compact'

chart_params = {
    'function': function,
    'symbol': "MSFT",
    'outputsize': output_size,
    'apikey': "78H5RH2BRNG4G5Z6"
}

        
response = requests.get(base_url, params=chart_params)
data = response.json()

if 'Error Message' in data:
    print(f"Error: {data['Error Message']}")
else:
    time_series = data['Time Series (Daily)']
    dates = []
    close_prices = []

    for date, values in time_series.items():
        dates.append(date)
        close_prices.append(float(values['4. close']))

    # Create and display ASCII chart
    chart = asciichartpy.plot(close_prices, {"width": 5, "height": 10, "format": "{:8.2f}"})
    print(chart)