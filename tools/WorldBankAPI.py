import wbgapi as wb
import pandas as pd
import matplotlib.pyplot as plt

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
    try:
        data = wb.data.DataFrame(indicator, country_code).transpose()
        data_frames.append(data)
    except KeyError:
        print(f"Data not available for indicator: {indicator}")

# Concatenate the DataFrames horizontally using the year as the index
combined_data = pd.concat(data_frames, axis=1)

# Print the combined data as a table
print(combined_data)

# Turn on interactive mode for Matplotlib
plt.ion()

# Create a function to plot and display data using Matplotlib
def plot_data(indicator_data, indicator_name):
    plt.figure(figsize=(10, 6))
    plt.plot(indicator_data.index, indicator_data.values, marker='o', linestyle='-')
    plt.title(f"{indicator_name} Over Time")
    plt.xlabel("Year")
    plt.ylabel(indicator_name)
    plt.grid(True)
    plt.show()

# Create and display line plots for each indicator using Matplotlib
for indicator in indicators:
    if indicator in combined_data.columns:
        indicator_data = combined_data[indicator]
        plot_data(indicator_data, indicator)