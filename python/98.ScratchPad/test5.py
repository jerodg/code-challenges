# Given a data set array.
# For each element in the array, find the sum of all the previous elements which are strictly greater than the current element.
# EX) array_previous_sum(data_set=[2, 6, 4, 1, 7]) would output:
#    0
#    0
#    6
#    12
#    0
# You may NOT edit the provided code.

data_set = [
        10,
        15,
        30,
        45,
        50,
        75,
        20,
        30,
        150,
        180,
        200,
        350,
        20,
        200,
        225,
        450
        ]


# data_set=[2, 6, 4, 1, 7]


# def greater(num: int, idx: int) -> list:
#     x = [x for x in data_set[:idx-1] if x > num]
#     print('x1', x)
#     return sum(x)


def array_previous_sum(lst: list):
    # for i, x in enumerate(lst):
        [print(sum([z for z in data_set[:i] if z > x])) for i, x in enumerate(lst)]


array_previous_sum(lst=data_set)
