#!/usr/bin/python3.6
"""Jerod Gawne, 2017-10-04

Find a String

https://www.hackerrank.com/challenges/find-a-string/

Editorial:
Approach 1
Slice an x amount of string in each iteration of the loop.

Approach 2
This can be solved by using a regex.

Approach 1
A = raw_input().strip()
x = raw_input().strip()

count = 0
for i in range(len(A) - len(x) + 1):
    if A[i:i+len(x)] == x:
        count += 1
print count

Approach 2
import re
a = raw_input()
b = raw_input()
match = re.findall('(?='+b+')',a)
print len(match)
"""


def count_substring(string, sub_string):
    """Jerod Gawne, 2017-10-04

    Counts the number of occurences of sub_string in string

    Attribution: https://stackoverflow.com/a/2970542/4434405

    :param string:
    :param sub_string:
    :return:
    """
    count = start = 0
    while True:
        start = string.find(sub_string, start) + 1
        if start > 0:
            count += 1
        else:
            return count


def count_substring2(string, sub_string):
    """Jerod Gawne, 2017-10-04

    Counts the number of occurences of sub_string in string

    Attribution: https://stackoverflow.com/a/46311005/4434405

    :param string:
    :param sub_string:
    :return:
    """
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count


def count_substring3(string, sub_string):
    """Jerod Gawne, 2017-10-04

    Counts the number of occurences of sub_string in string

    Attribution: https://stackoverflow.com/a/40317123/4434405

    :param string:
    :param sub_string:
    :return:
    """
    count = 0
    while sub_string in string:
        count += 1
        string = string[string.find(sub_string) + 1:]
    return count


def count_substring4(string, sub_string):
    """Jerod Gawne, 2017-10-04

    Counts the number of occurences of sub_string in string

    Attribution: https://www.hackerrank.com/rsurana?hr_r=1

    In a list comprehension, we slide through bigger string by one position at a time with the
    sliding window of length of smaller string. We can compute the sliding count by substracting
    the length of smaller string from bigger string. For each slide, we compare that part of bigger
    string with our smaller string and generate 1 in a list if match found. Sum of all of these 1's
    in a list will give us total number of matches found.

    :param string:
    :param sub_string:
    :return:
    """
    return sum([1 for _ in range(len(string) - len(sub_string) + 1) if string[_:_ + len(sub_string)] == sub_string])


def count_substring5(string, sub_string):
    """Jerod Gawne, 2017-10-04

    Counts the number of occurences of sub_string in string

    Attribution: https://stackoverflow.com/a/11706065/4434405

    re.escape makes sure the substring doesn't interfere with the regex

    This loads the entire list into memory

    :param string:
    :param sub_string:
    :return:
    """
    import re
    return len(re.findall(f'(?={re.escape(sub_string)})', string))


def count_substring6(string, sub_string):
    """Jerod Gawne, 2017-10-04

    Counts the number of occurences of sub_string in string

    Attribution: https://stackoverflow.com/a/11706065/4434405

    re.escape makes sure the substring doesn't interfere with the regex

    alternative to in-memory count_substring5()

    This computes occurances which requires cpu cycles but doesn't hold list in memory

    :param string:
    :param sub_string:
    :return:
    """
    import re
    return sum(1 for _ in re.finditer(f'(?={re.escape(sub_string)})', string))


def main():
    """
    Main/Tests

    Sample Input
    ABCDCDC
    CDC

    Sample Output
    2
    """
    string = input().strip()
    sub_string = input().strip()

    print(count_substring(string, sub_string))
    print(count_substring2(string, sub_string))
    print(count_substring3(string, sub_string))
    print(count_substring4(string, sub_string))
    print(count_substring5(string, sub_string))
    print(count_substring6(string, sub_string))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
