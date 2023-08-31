import wbgapi as wb

from rich.traceback import install
install(show_locals=True)

# Search for inflation-related series information
data = wb.data.DataFrame("FP.CPI.TOTL.ZG", "USA").transpose()
print(data)