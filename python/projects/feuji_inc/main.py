"""
Given a string with employee id, name and manager id, print the employees in an org chart fashion.

Input:
"1:Max:4, 4:Ann:0, 2:Jim:4, 3:Tom:1"
1 -> employee id
Max -> name
4 -> manager id

Output:
Ann
- Max
-- Tom
- Jim
"""
from collections import defaultdict

# emps = {}
# mgrs = {}

ls = '1:Max:4, 4:Ann:0, 2:Jim:4, 3:Tom:1'.split(',')

ls = [x.lstrip() for x in ls]

print(ls)

res = defaultdict(list)
for x, y, z in ls:
    res[x].append(v)

print(res)  #  # for x in ls:
#     id, name, manager = x.split(':')
#     # print(id, name, manager)
#     emps[int(id.lstrip())] = (name, int(manager))

# out = dict(sorted(emps.items()).sort(key = lambda x: x[0]))
# emps = sorted(emps.items(), key=lambda x: x[1])
# print(sorted(emps.items(), key=lambda x: x[1]))

# out[id][name] = manager

# print(out.items())

# m0 = [x for x in out.items() if x['manager'] == 0]
# print(m0)

# for k, v in emps.items():
#     # print(v[0])
#     print(k, v)
#     subs = [x for x in emps.items() if x == v[1]]
#     for x in subs:
#         print('- ', subs[0])

# print(emps)
# y = max(out.keys())
# for i in range(y):
#   print()
