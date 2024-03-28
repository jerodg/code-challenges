'''
  String Decoding

  We have an input string 'id', which is formatted as follows:
  x{value} -- where the string value inside the curly braces is repeated x number times.
  x is always a positive integer, x > 1,
  value consists of alphabet characters
  All open curly braces have matching closed braces

  For example, these strings would translate as follows:
  b2{o}2{k}2{e}per => bookkeeper
  2{ra}2{dz} => raradzdz
  5{a}2{b} => aaaaabb
  10{a} => aaaaaaaaaa

  Please write a function that will translate the input string.
'''
# from string import is_numeric
import pytest
import re
from string import ascii_letters as al

# bre = re.compile(r'\{(.*)\}')
bre = re.compile(r'[a-z]\d+\{.*\}')


def decodeContainerId(inpt):
    # x = inpt.strip('{')
    # x = x.strip('}')
    # print(re.findall(bre, inpt))
    # print(re.match(bre, inpt))
    # x = re.split(bre, inpt)
    sp1 = inpt.split('}')
    print(sp1)
    out = []

    for x in sp1:
        o = re.split(r'\{', x)
        # o = x.split('{')
        # print('o:', o)
        if list(o[0])[0] in al and len(o) > 1:
            out.append(list(o[0])[0])
            try:
                out.append((int(list(o[0])[1])) * o[1])
            except ValueError:
                out.append(list(o[0])[1])
        elif o[0].isnumeric():
            # print('numeric')
            # print(f'test: {int(o[0])}, {o[1][0]}')
            out.append(int(o[0]) * o[1][0])
        else:
            # print('else:')
            out.append(o[0])

    # print(out)
    # print(''.join(out))
    return ''.join(out)


# decodeContainerId('b2{o}2{k}2{e}per')
# TESTS


def test_bookkeeper():
    assert decodeContainerId('b2{o}2{k}2{e}per') == 'bookkeeper'


def test_raradzdz():
    assert decodeContainerId('2{ra}2{dz}') == 'raradzdz'


def test_aaaaabb():
    assert decodeContainerId('5{a}2{b}') == 'aaaaabb'


def test_aaaaaaaaaa():
    assert decodeContainerId('10{a}') == 'aaaaaaaaaa'


pytest.main()
