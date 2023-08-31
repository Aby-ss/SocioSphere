import wbgapi as wb

from rich.traceback import install
install(show_locals=True)

inflation_data = wb.series.info(q="inflation")
expenses_data = wb.series.info(q="expenses")
gdp_data = wb.series.info(q="gdp")
gdpGrowth_data = wb.series.info(q="gdp growth")
grossSaving_data = wb.series.info(q="gross saving")
exports_data = wb.series.info(q="exports of goods and services")

print(inflation_data)
print(expenses_data)
print(exports_data)
print(gdp_data)
print(gdpGrowth_data)
print(grossSaving_data)
