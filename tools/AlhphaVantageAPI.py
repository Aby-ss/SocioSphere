import json
import requests
import asciichartpy

from rich.traceback import install
install(show_locals=True)

# List of major corporation codes
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

# Alpha Vantage API configuration
base_url = 'https://www.alphavantage.co/query'
function = 'TIME_SERIES_DAILY'
output_size = 'compact'

# Common chart parameters
chart_params = {
    'function': function,
    'symbol': "",  # Symbol will be updated in the loop
    'outputsize': output_size,
    'apikey': "YOUR_API_KEY_HERE",  # Replace with your Alpha Vantage API key
}

# Iterate through corporation codes and fetch data
for code in major_corporation_codes:
    chart_params['symbol'] = code  # Set the symbol to the current corporation code
    response = requests.get(base_url, params=chart_params)
    data = response.json()

    if 'Error Message' in data:
        print(f"Error for {code}: {data['Error Message']}")
    else:
        time_series = data['Time Series (Daily)']
        dates = []
        close_prices = []

        for date, values in time_series.items():
            dates.append(date)
            close_prices.append(float(values['4. close']))

        # Create and display ASCII chart for the current corporation
        print(f"Stock Prices for {code}:")
        chart = asciichartpy.plot(close_prices, {"width": 50, "height": 10, "format": "{:8.2f}"})
        print(chart)