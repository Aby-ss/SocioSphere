import wbgapi as wb
import matplotlib.pyplot as plt

from rich.traceback import install
install(show_locals=True)

# Data Retrieval
indicators = [
    "FP.CPI.TOTL.ZG",     # Inflation
    "NE.EXP.GNFS.CD",     # Expenses
    "NY.GDP.MKTP.CD",     # GDP
    "NY.GDP.MKTP.KD.ZG",  # GDP Growth
    "NY.GNS.ICTR.CD",     # Gross Savings
    "NE.EXP.GNFS.CD"      # Exports
]

countries = "USA"

data = [wb.data.DataFrame(indicator, countries).transpose() for indicator in indicators]

# Set up colors
colors = ['b', 'g', 'r', 'c', 'm', 'y']

# Create a figure and axis
fig, ax = plt.subplots()

# Plot each indicator with a different color
for i, indicator_data in enumerate(data):
    ax.plot(indicator_data.index, indicator_data.values, label=indicators[i], color=colors[i])

# Set axis labels and title
ax.set_xlabel("Year")
ax.set_ylabel("Value")
ax.set_title("Multiple Indicators Over Time")

# Add a legend
ax.legend(loc='upper left')

# Rotate the x-axis labels by 90 degrees
ax.tick_params(axis='x', rotation=90)

# Show the plot
plt.show()