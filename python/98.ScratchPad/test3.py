tmp = [28, 26, 11, 37, 27, 31, 24]


def max_temp(tmp):
    min = tmp[0]
    max = 0

    for i in range(len(tmp)):
        if tmp[i] < min:
            min = tmp[i]
        elif (tmp[i] - min) > max:
            max = tmp[i] - min

    return max


if __name__ == '__main__':
    print(max_temp(tmp))
