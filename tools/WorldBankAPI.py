import wbgapi as wb
import pandas as pd
import asciichartpy


from rich.traceback import install
install(show_locals=True)

# Create a Pandas DataFrame with economic data
data = {
    "Year": [2010, 2011, 2012, 2013, 2014],  # Replace with your years
    "Inflation Rate": [1.5, 2.0, 1.8, 2.2, 1.9],  # Replace with your inflation rate data
    "Expenses": [200000, 220000, 240000, 260000, 280000],  # Replace with your expenses data
    "GDP": [1500000, 1550000, 1600000, 1650000, 1700000],  # Replace with your GDP data
    "GDP Growth Rate": [3.0, 3.2, 3.5, 3.8, 4.0],  # Replace with your GDP growth rate data
    "Gross Savings": [30000, 32000, 35000, 38000, 40000],  # Replace with your gross savings data
    "Exports": [180000, 190000, 200000, 210000, 220000]  # Replace with your exports data
}

# Create a Pandas DataFrame
combined_data = pd.DataFrame(data)
combined_data.set_index("Year", inplace=True)

# Define a function to display ASCII charts
def display_chart(indicator_data, indicator_name):
    print(f"\n{indicator_name}:")
    chart_data = asciichartpy.plot(indicator_data.tolist(), {'height': 10})
    print(chart_data)

# List of indicators
indicators = [
    "Inflation Rate",
    "Expenses",
    "GDP",
    "GDP Growth Rate",
    "Gross Savings",
    "Exports"
]

# Create and display ASCII charts for each indicator
for indicator in indicators:
    if indicator in combined_data.columns:
        indicator_data = combined_data[indicator]
        display_chart(indicator_data, indicator)