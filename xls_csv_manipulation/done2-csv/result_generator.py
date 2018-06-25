open_exp_res = open('exp.csv').readlines()
open_all_des = open('all.csv').readlines()

exp_dict = {}
for row in open_exp_res:
    gene_name, gene_num = row.split(',')
    exp_dict[gene_name] = gene_num

write_result = open('result.csv','w')
for n, row in enumerate(open_all_des):
    a, b, c, d = row.split(",")
    e = exp_dict.get(a)
    write_result.write("%s,%s,%s,%s,%s" % (a, b, c, d.strip(), e))
