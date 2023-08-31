import wbgapi as wb

from rich.traceback import install
install(show_locals=True)

inflation_data = wb.series.info(q="inflation")
expenses_data = wb.series.info(q="expenses")
gdp_data = wb.series.info(q="gdp")
gdpGrowth_data = wb.series.info(q="gdp growth")
grossSaving_data = wb.series.info(q="gross saving")
exports_data = wb.series.info(q="exports")

print(inflation_data)
print(expenses_data)
print(exports_data)
print(gdp_data)
print(gdpGrowth_data)
print(grossSaving_data)

print(" ")
print("-" * 150)
print(" ")

inflation_data = wb.data.DataFrame("FP.CPI.TOTL.ZG").transpose()
expenses_data = wb.data.DataFrame("NE.EXP.GNFS.CD").transpose()
gdp_data = wb.data.DataFrame("NY.GDP.MKTP.CD").transpose()
gdpGrowth_data = wb.data.DataFrame("NY.GDP.MKTP.KD.ZG").transpose()
grossSaving_data = wb.data.DataFrame("NY.GNS.ICTR.CD").transpose()
exports_data = wb.data.DataFrame("NE.EXP.GNFS.CD").transpose()

print(inflation_data)
print(expenses_data)
print(exports_data)
print(gdp_data)
print(gdpGrowth_data)
print(grossSaving_data)
