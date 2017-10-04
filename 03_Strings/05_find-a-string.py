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
    """
    Counts the number of occurences of sub_string in string

    Credit: https://stackoverflow.com/questions/2970520/string-count-with-overlapping-occurrences

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
    """
    Counts the number of occurences of sub_string in string

    Credit: https://www.hackerrank.com/rsurana?hr_r=1

    In a list comprehension, we slide through bigger string by one position at a time with the
    sliding window of length of smaller string. We can compute the sliding count by substracting
    the length of smaller string from bigger string. For each slide, we compare that part of bigger
    string with our smaller string and generate 1 in a list if match found. Sum of all of these 1's
    in a list will give us total number of matches found.

    :param string:
    :param sub_string:
    :return:
    """
    return sum([1 for i in range(len(string) - len(sub_string) + 1) if string[i:i + len(sub_string)] == sub_string])


def main():
    """
    Main/Tests
    """
    string = input().strip()
    sub_string = input().strip()

    print(count_substring(string, sub_string))
    print(count_substring2(string, sub_string))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
