from xlrd import open_workbook
from xlwt import easyxf
from xlutils.copy import copy

excel = open_workbook('2.xls',formatting_info=True)
sheet = excel.sheet_by_index(0)

wb = copy(excel)
ws = wb.get_sheet(0)

plain = easyxf('')
for i,cell in enumerate(sheet.col(1)):
    if not i:
        continue
    ws.write(i,3,111,plain)



wb.save('a.xls')
