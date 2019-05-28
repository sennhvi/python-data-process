# -*- coding:utf-8 -*-
# editor: sennhvi
from itertools import combinations

member_dict = {}
weekday = "一二三四五六七"
weekday_index = [1,2,3,4,5,6,7]

with open('input', 'r', encoding='UTF8') as f:
    open_input_res = f.readlines()

for row in open_input_res[1:]:
    row = row.replace("\xa0", "").strip()
    for index, char in enumerate(row):
        if char.isdigit():
            power_i = index
        if char in weekday:
            limit_i = index
            break
    member_dict[row[:power_i].strip()] = [row[power_i], list(row[limit_i:])]  # 初始化字典
print(member_dict)
member_set = set(member_dict.keys())
print("成员集合：{}".format(member_set))

count = 0
possible_list = []
for i in combinations(member_set, 2):  # 组合，一天排两个人
    if int(member_dict[i[0]][0]) + int(member_dict[i[1]][0]) != 0:  # 资格之和不等于0
        possible_list.append(i)
        count += 1

print("一天排俩人一共有：{}种可能".format(count))
print("排班组合列表：{}".format(possible_list), end="\n\n")  # 排班组合列表，待按照以下要求处理的数据输入
# 同一个人不能连着两天值班
# 周末排班不可怼着来，尽可能均匀不重复
# 任何一个人排班相差不能超过1（3-4个）

weekday_count, day_index, result = 1, 0, []
# weekday = "一二三四五六七"
# weekday_index = [1,2,3,4,5,6,7] # 0 1 2 3 4 5 6
# result = []

cc = 0
# 可反复调用，产生新的排列可能
while cc <= 7: # 尽量让产生排列长度大于7，这样连续按照生成模式排班，即可使得周末不会总是同一组人值班
    for poss in possible_list[:]:
        # print(poss[0], poss[1]) # 俩人姓名
        # print(member_dict[poss[0]][1], member_dict[poss[1]][1]) # 俩人禁止排班的时间
        forbid_day_set = set(member_dict[poss[0]][1] + member_dict[poss[1]][1])
        for day_count in forbid_day_set:
            if weekday[weekday_index.index(weekday_count)] == day_count:
                break
        else:
            if day_index != 0:
                for member in result[day_index-1][1]:
                    if member in poss:
                        break
                else:
                    result.insert(day_index, [weekday_count, poss])
                    # print(poss)
                    possible_list.remove(poss)
                    weekday_count = (weekday_count % 7) + 1
                    day_index += 1
                    cc += 1
            else:
                result.insert(day_index, [weekday_count, poss])
                possible_list.remove(poss)
                weekday_count = (weekday_count % 7) + 1
                day_index += 1
                cc += 1


print("预测组合结果序列为：",result) # 数据组织实例：[1, ('A', 'B')]。 1代表星期一，括号内为排班成员


# 以下为测验内容，检测产生排班序列的人次差异不超过1
check_members = []
check_members_dict = {}
for res in result:
    for name in res[1]:
        check_members.append(name)

for i in check_members:
    check_members_dict[i] = check_members.count(i)

# print(check_members_dict) # 成员出现次数字典
ckmd_count = []
doable = False
for k,v in check_members_dict.items():
    ckmd_count.append(v)
if max(ckmd_count) - min(ckmd_count) > 1:
    print("Invalid Combinations")
else:
    doable = True
    print("Valid Combinations")

if doable:
    with open("out.csv", "w+") as outfile:
        for res in result:
            n1, n2 = res[1]
            outfile.write(("%s,%s" % (n1,n2)) + '\n')




