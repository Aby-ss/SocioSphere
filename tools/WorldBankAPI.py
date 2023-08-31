import wbgapi as wb

from rich.traceback import install
install(show_locals=True)

# Search for inflation-related series information
data = wb.series.info(q="inflation")

# Extract numeric data from the response
numeric_data = {}
for entry in data:
    series_id = entry['id']
    series_name = entry['value']
    numeric_data[series_name] = wb.data.DataFrame(series_id, time="YR")

# Print the numeric data
for series_name, df in numeric_data.items():
    print(f"Numeric data for {series_name}:\n{df}\n")