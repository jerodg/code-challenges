"""

Input: an array of integers, e.x. [-1, 0, 1, -1, 5, 10, -5]

Output: shuffle (reordered output) the array so that any elements in even indices are no larger than any elements in odd indices.
One possible solution for the
above example is [-1, 5, -1, 10, 0, 1, -5]

another example:
INPUT:  [2, 5, 1, 3, 4]
OUTPUT: [1, 5, 2, 4, 3]
"""

inp = [-1, 0, 1, -1, 5, 10, -5]
# -1 1 5 -5
# 0 -1 10
#
inp.sort()
print('inp:', inp)
e = len(inp) // 2

odd = inp[:e + 1]
evn = inp[e:]

print(f'even: {evn}')
print(f'odd: {odd}')

out = []
for i in range(len(inp)):
    try:
        if i % 2:
            out.append(evn.pop())
        else:
            out.append(odd.pop())
    except:
        pass

# print('out:',)
# for i in range(len(inp)):
#     if i % 2:
#         evn.append(inp[i])
#     else:
#         odd.append(inp[i])

print('out:', out)  # evn.sort()  # odd.sort()


# # test
# if any(evn) > any(odd):
#     print('larger')

# out = []
# for i in range(len(inp)):
#     # print('i:', i)
#     if i % 2 != 0:
#         out.append(odd.pop())
#     else:
#         out.append(evn.pop())

# print('out:', out)

# odd = []
# evn = []
# for i in range(len(out)):
#     if i % 2:
#         odd.append(out[i])
#     else:
#         evn.append(out[i])

# evn.sort()
# odd.sort()

# print(f'even: {evn}')
# print(f'odd: {odd}')

# out = []
# for i in range(len(inp)):
#     if i % 2:
#         print('i:', i)
#         try:
#             o = evn.pop()
#             print('out_evn:', o)
#             out.append(o)
#         except:
#             pass
#     else:
#         try:
#             o = odd.pop()
#             print('out_odd:', o)
#             out.append(o)
#         except:
#             pass


# print(out)

# -5  5. 1  -1
#
