"""Write your solution in this file.

You can execute and test your answer by pressing 'Try Answer' in the side panel,
or by running `python test_answer.py <test_case_path>` on the command line.

For example:
    python test_answer.py inputs/first_last.json
"""

from __future__ import print_function


def answer(name):
    """Implement your solution here.

    Arguments:
        name: A string with the full name of the person.

    Returns:
         A string with the abbreviated name.
    """
    names = name.split()
    first = names.pop(0)
    last = names.pop(-1)

    abbv = ["{}.".format(n[0]) for n in names]
    out = [first]
    for n in abbv:
        out.append(n)
    out.append(last)

    return " ".join(out)
