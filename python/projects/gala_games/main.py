# function frame(str) {
#   return str;
# }

# console.log(frame('Gala Games is Hiring'));

# /*

# **********
# * Gala   *
# * Games  *
# * is     *
# * Hiring *
# **********

# */

text = 'Gala Games is Hiringggrgergergergerg'.split(' ')
mx = max(len(e) for e in text)
res = [f'* {x.ljust(mx, " ")} *' for x in text]

print('*' * int(mx + 4))
[print(''.join(x)) for x in res]
print('*' * int(mx + 4))

# ln_txt = len(mx)
# half = (mx - 2) / 2
# if mx % 2 == 0:
#     hlf0, hlf1 = half, half
# else:
#     hlf0, hlf1 = half, half + 1

# res = []
# for x in text:
#      res.append(f'* {x.ljust(mx, " ")} *')
#     # print('test', mx - 4 - len(x))
#     cnt = (mx + 4) -
#     y = ['* ', x, ' ' * cnt, ' *']
#     res.append(y)
