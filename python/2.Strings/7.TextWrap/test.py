import functools

s, w = input(), int(input())
print(*[_ for _ in iter(functools.partial(s.read, w), '')], sep='\n')
