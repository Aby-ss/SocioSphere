import wbgapi as wb

from rich import print
from rich.panel import Panel
from rich.traceback import install
install(show_locals=True)

# Define the indicators and country code
indicators = [
    "FP.CPI.TOTL.ZG",  # Inflation Rate
    "NE.EXP.GNFS.CD",  # Expenses
    "NY.GDP.MKTP.CD",  # GDP
    "NY.GDP.MKTP.KD.ZG",  # GDP Growth Rate
    "NY.GNS.ICTR.CD",  # Gross Savings
    "NE.EXP.GNFS.CD"  # Exports
]
country_code = "USA"

# Initialize an empty dictionary to store data
data_dict = {}

# Fetch data for each indicator and store it in the dictionary
for indicator in indicators:
    data = wb.data.DataFrame(indicator, country_code).transpose()
    data_dict[indicator] = data

# Print each data table
for indicator, data in data_dict.items():
    print(f"{indicator}")
    print(Panel.fit(data))
    print("\n")