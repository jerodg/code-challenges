def fun(s):
    pass
    # return True if s is a valid email, else return False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)

4
pow 2 3
cmp 1 2
join_with coder best the are you ,
capitalize_first_and_join first second third

6
1
1
2
2
3
3
1

print('numbers:', numbers)
print('k:', k)
