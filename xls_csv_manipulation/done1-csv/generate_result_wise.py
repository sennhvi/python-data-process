family_size = open('family_size.csv').readlines()
fucker = open('xls_source_converted.csv').readlines()

dd = {}
for row in family_size:
    num, foo = row.split(",")
    bar = foo.split(" ")
    for i in bar:
        dd[i.strip()] = num


shitter = open('result.csv', 'w')
for n, row in enumerate(fucker):
    a,b,c = row.split(",")
    e = dd.get(a, 0)
    shitter.write(("%s,%s,%s,%s" % (a,b,c.strip(),e)) + '\n')
#    print n, 'done', e

# print 'dd', len(dd.keys())

