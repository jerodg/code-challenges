"""
This module provides a solution to the problem of counting the number of islands in a 2D grid map.
It reads the grid map from the standard input, counts the number of islands, and writes the results to a file.
"""

from json import loads as l


def dfs(g: list[list[str]], i: int, j: int) -> list[list[str]]:
    """
    This function performs a depth-first search (DFS) on the grid map to find all the cells that belong to the same island.

    Args:
        g (List[List[str]]): A 2D grid map of '1's (land) and '0's (water).
        i (int): The row index of the current cell.
        j (int): The column index of the current cell.

    Returns:
        List[List[str]]: The updated grid map after marking the visited cells.

    Example:
        >>> dfs(
        ...     [
        ...         ['1', '1', '1', '1', '0'],
        ...         ['1', '1', '0', '1', '0'],
        ...         ['1', '1', '0', '0', '0'],
        ...         ['0', '0', '0', '0', '0'],
        ...     ],
        ...     0,
        ...     0,
        ... )
        [['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0']]

    Doctest:
        >>> dfs(
        ...     [
        ...         ['1', '1', '0', '0', '0'],
        ...         ['1', '1', '0', '0', '0'],
        ...         ['0', '0', '1', '0', '0'],
        ...         ['0', '0', '0', '1', '1'],
        ...     ],
        ...     0,
        ...     0,
        ... )
        [['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]
        >>> dfs(
        ...     [
        ...         ['1', '1', '0', '0', '0'],
        ...         ['1', '1', '0', '0', '0'],
        ...         ['0', '0', '1', '0', '0'],
        ...         ['0', '0', '0', '1', '1'],
        ...     ],
        ...     2,
        ...     2,
        ... )
        [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['0', '0', '0', '1', '1']]
        >>> dfs(
        ...     [
        ...         ['1', '1', '0', '0', '0'],
        ...         ['1', '1', '0', '0', '0'],
        ...         ['0', '0', '1', '0', '0'],
        ...         ['0', '0', '0', '1', '1'],
        ...     ],
        ...     3,
        ...     3,
        ... )
        [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '0', '0']]
        >>> dfs(
        ...     [
        ...         ['1', '1', '0', '0', '0'],
        ...         ['1', '1', '0', '0', '0'],
        ...         ['0', '0', '1', '0', '0'],
        ...         ['0', '0', '0', '1', '1'],
        ...     ],
        ...     3,
        ...     4,
        ... )
        [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '0']]
        >>> dfs(
        ...     [
        ...         ['1', '1', '0', '0', '0'],
        ...         ['1', '1', '0', '0', '0'],
        ...         ['0', '0', '1', '0', '0'],
        ...         ['0', '0', '0', '1', '1'],
        ...     ],
        ...     0,
        ...     4,
        ... )
        [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]
    """
    g[i][j] = '0'
    if i + 1 < len(g) and g[i + 1][j] == '1':
        g = dfs(g, i + 1, j)
    if j + 1 < len(g[i]) and g[i][j + 1] == '1':
        g = dfs(g, i, j + 1)
    if i - 1 >= 0 and g[i - 1][j] == '1':
        g = dfs(g, i - 1, j)
    if j - 1 >= 0 and g[i][j - 1] == '1':
        g = dfs(g, i, j - 1)
    return g


with open('user.out', 'w') as file:
    for g in stdin:
        g = l(g)
        if not g or not g[0]:
            file.write('0' + '\n')
        else:
            c = 0
            for i in range(len(g)):
                for j in range(len(g[i])):
                    if g[i][j] == '1':
                        c += 1
                        g = dfs(g, i, j)
            file.write(str(c) + '\n')
exit()
