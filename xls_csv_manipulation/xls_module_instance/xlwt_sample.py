import xlwt

x=1
y=2
z=3
list1=[2.34,4.346,4.234]

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")

sheet1.write(0, 1, 3)
sheet1.write(1, 1, 4)
sheet1.write(2, 1, 5)

sheet1.write(4, 0, "Stimulus Time")
sheet1.write(4, 1, "Reaction Time")

i=4
for n in list1:
    i = i+1
    sheet1.write(i, 0, n)

book.save("trial.xls")
