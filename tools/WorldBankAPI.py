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

# Initialize empty lists to store data
data_lists = {indicator: [] for indicator in indicators}
years = []

# Fetch data for each indicator and store it in the lists
for indicator in indicators:
    data = wb.data.DataFrame(indicator, country_code).transpose()
    years = data.columns.tolist()
    data_lists[indicator] = data.values[0]

# Create a Pandas DataFrame from the collected data
df = pd.DataFrame(data_lists, index=years)

# Print the Pandas DataFrame as a table
print(df)