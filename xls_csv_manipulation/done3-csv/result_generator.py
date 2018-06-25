open_size_res = open('P_size.csv').readlines()
open_all_des = open('P_all.csv').readlines()

dd = {}
for row in open_size_res:
    g_name, g_size = row.split(',')
    for sb in g_name.split(" "):
        dd[sb.strip()] = g_size

write_result = open('result.csv','w')
for n, row in enumerate(open_all_des):
    a, b, c, d = row.split(",")
    a = a.strip()
    e = dd.get(a)
    if e == None:
        e = '0'
    write_result.write("%s,%s,%s,%s,%s" % (a, b, c, d.strip(), e.strip()) + '\n')
