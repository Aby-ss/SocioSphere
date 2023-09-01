import wbgapi as wb

from rich.traceback import install
install(show_locals=True)

inflation_data = wb.data.DataFrame("FP.CPI.TOTL.ZG", "USA").transpose()
expenses_data = wb.data.DataFrame("NE.EXP.GNFS.CD", "USA").transpose()
gdp_data = wb.data.DataFrame("NY.GDP.MKTP.CD", "USA").transpose()
gdpGrowth_data = wb.data.DataFrame("NY.GDP.MKTP.KD.ZG", "USA").transpose()
grossSaving_data = wb.data.DataFrame("NY.GNS.ICTR.CD", "USA").transpose()
exports_data = wb.data.DataFrame("NE.EXP.GNFS.CD", "USA").transpose()

print(inflation_data)
print(expenses_data)
print(exports_data)
print(gdp_data)
print(gdpGrowth_data)
print(grossSaving_data)
