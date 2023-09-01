import wbgapi as wb
import pandas as pd


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

# Create a Pandas DataFrame from the collected data
df = pd.DataFrame(data_dict)

# Print the Pandas DataFrame as a table
print(df)