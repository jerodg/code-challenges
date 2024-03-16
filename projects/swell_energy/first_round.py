def method_4(sentence: str) -> str:
    """Method 4:
        Changes word order only
    Args:
        sentence: (str)

    Returns:
        result: (str)"""
    s = sentence.split()
    l = []
    for i in s:
        l.append(i)

    res = [ii for n, ii in enumerate(l) if ii not in l[:n]]
    return ' '.join(res[::-1])


str = 'This is a coding test, I like coding because it is fun'
print(method_4(str))
