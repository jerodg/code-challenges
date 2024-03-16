def solve(expression: str) -> str:
    """
    This function removes all parentheses from a mathematical expression and adjusts the signs accordingly.

    Args:
        expression (str): The mathematical expression to simplify.

    Returns:
        str: The simplified mathematical expression.

    Doctest:
        >>> solve("x-(y+z)")
        'x-y-z'
        >>> solve("x-(y-z)")
        'x-y+z'
        >>> solve("u-(v-w-(x+y))-z")
        'u-v+w+x+y-z'
        >>> solve("x-(-y-z)")
        'x+y+z'
    """
    result = []
    stack = []
    operator = '+'
    for char in expression:
        if char.isalpha():
            result.append(operator + char)
        elif char == '(':
            stack.append(operator)
            operator = '+'
        elif char == ')':
            operator = stack.pop()
        else:  # char is an operator
            operator = char

    return ''.join(result)
