"""CodeWars Strip Comments.

Provides functionality to strip comments from multi-line strings.
It removes any text that follows specified comment markers and strips trailing
whitespace from each line.

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).
"""


def strip_comments(text: str, markers: list) -> str:
    r"""Strip comments and trailing whitespace from a multi-line string.

    Parameters:
        text (str): The input string with potential comments
        markers (list): A list of comment marker characters

    Returns:
        str: The input string with comments and trailing whitespace removed

    Example:
        >>> strip_comments("apples, pears # and bananas\\ngrapes\\nbananas !apples", ["#", "!"])
        'apples, pears\\ngrapes\\nbananas'
    """
    lines = text.split("\n")
    result = []

    for line in lines:
        # Find the earliest comment marker position
        earliest_pos = len(line)
        for marker in markers:
            pos = line.find(marker)
            if pos != -1 and pos < earliest_pos:
                earliest_pos = pos

        # Truncate line at the earliest marker position and remove trailing whitespace
        truncated_line = line[:earliest_pos].rstrip()
        result.append(truncated_line)

    return "\n".join(result)
