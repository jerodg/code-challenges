#!/usr/bin/env python3.10
"""
Validating Email Addresses With a Filter
Jerod Gawne, 2021.09.13 <https://github.com/jerodg/hackerrank>"""
import re

flgs = re.IGNORECASE
flgs |= re.MULTILINE
ere = re.compile(r'^[a-zA-Z0-9\-_]+@[A-Za-z0-9]+[.][a-zA-Z]{1,3}$', flags=flgs)


def fun(s):
    return True if re.fullmatch(ere, s) else False


def filter_mail(emails: list):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
