#Abrir planilha do Excel

import openpyxl
wb = openpyxl.load_workbook('cata_logo.xlsx')
type(wb)
print(type(wb))
wb.get_sheet_names()