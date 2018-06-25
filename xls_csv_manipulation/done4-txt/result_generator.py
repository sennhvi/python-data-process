open_res = open('ath.txt').readlines()
open_des = open('des.txt','w')

for line in open_res:
    a = line.split(";")[-1]
    open_des.write(a)


