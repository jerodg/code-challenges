import json
import sys
from typing import List

def find_maximal_rectangle(matrix: List[List[str]]) -> int:
    """
    This function finds the maximal rectangle in a binary matrix.

    Args:
        matrix (List[List[str]]): A binary matrix represented as a list of lists.

    Returns:
        int: The area of the maximal rectangle.

    Examples:
        >>> find_maximal_rectangle([['1', '0', '1', '0', '0'], ['1', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']])
        6
        >>> find_maximal_rectangle([['0']])
        0
        >>> find_maximal_rectangle([['1']])
        1
        >>> find_maximal_rectangle([['1', '1', '1', '1'], ['1', '1', '1', '1'], ['1', '1', '1', '1']])
        12
        >>> find_maximal_rectangle([['1', '0', '1', '0'], ['1', '0', '1', '1'], ['1', '1', '1', '1'], ['1', '0', '1', '0']])
        4
    """
    m = len(matrix)
    n = len(matrix[0])
    heights = [0] * (n + 1)
    best = 0
    for row in matrix:
        for col in range(n):
            # Update the height of the current column
            heights[col] = heights[col] + 1 if row[col] == '1' else 0
        stack = [-1]
        for col in range(n + 1):
            # Pop the stack while the current height is less than the last one in the stack
            while heights[col] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = col - stack[-1] - 1
                # Update the best area
                best = max(best, h * w)
            stack.append(col)
    return best


if __name__ == '__main__':
    with open('user.out', 'w') as f:
        for matrix in map(json.loads, sys.stdin):
            result = find_maximal_rectangle(matrix)
            print(result, file=f)
    sys.exit()
