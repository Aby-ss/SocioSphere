import wbgapi as wb
import pandas as pd
import asciichartpy


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

# Initialize an empty list to store DataFrames
data_frames = []

# Fetch data for each indicator and store it in a DataFrame
for indicator in indicators:
    data = wb.data.DataFrame(indicator, country_code).transpose()
    data_frames.append(data)

# Concatenate the DataFrames horizontally using the year as the index
combined_data = pd.concat(data_frames, axis=1)

# Print the combined data as a table
print(combined_data)