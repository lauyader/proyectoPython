# Ejemplo de modificacion de hoja Excel
from xlrd import open_workbook
from xlutils.copy import copy
rb = open_workbook('example.xls',formatting_info=True)
wb = copy(rb)
ws = wb.get_sheet(0)
ws.write(0,0,"I'm only changing cell A1")
wb.save('example2.xls')