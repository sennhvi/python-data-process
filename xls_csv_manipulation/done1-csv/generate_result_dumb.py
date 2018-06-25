from xlrd import open_workbook
from xlutils.copy import copy
from xlwt import easyxf
import csv

# open file as a xlrd object
excel = open_workbook('xls_source_origin.xls',formatting_info=True)

# get working sheet,default to 0
# sheet = excel.sheets()[0]
sheet = excel.sheet_by_index(0)

wb = copy(excel)
ws = wb.get_sheet(0)

plain = easyxf('')

# open csv
with open('family_size.csv', 'r') as csvfile:

    # read data as spamreader
    spamreader = csv.reader(csvfile)

    # traverse each line in spamreader.i.e,each line in csv file
    for line in spamreader:

        # split line as list using space,get the data in 2nd column.i.e,line[1]
        # traverse each member in line[1] for searching it in excel file
        for member in line[1].split(' '):

            # traverse each cell of same column in all rows(i.e,col_values(0))
            # using member to query into xls,using line[0] to write into xls cells
            for index, iters in enumerate(sheet.col_values(0)):
                if member in iters:
                    ws.write(index, 3, line[0], plain)
wb.save('2.xls')
