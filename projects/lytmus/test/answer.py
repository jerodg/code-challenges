"""
This is the file with your answer, do not rename or move it.
Write your code in it, and save it before submitting your answer.
"""


class Rectangle:
    """Auxiliary class representing a window.

    Attributes:
        x: An integer representing the X coordinate of the window's 
            lower-left corner, in pixels.
        y: An integer representing the Y coordinate of the window's 
            lower-left corner, in pixels.
        w: An integer representing the width of the window, in pixels.
        h: An integer representing the height of the window, in pixels.
    """

    def __init__(self, window_string):
        """Initialize window from a string of properties.

        Args:
            window_string: A string with the properties of the window, 
                eg, 'X=10 Y=20 W=30 H=40'.
        """
        parts = window_string.split()
        parts.sort()
        self.valid = True

        try:
            assert (len(parts) == 4 and
                    parts[0].startswith('H=') and
                    parts[1].startswith('W=') and
                    parts[2].startswith('X=') and
                    parts[3].startswith('Y='))

            self.h = int(parts[0][2:])
            self.w = int(parts[1][2:])
            self.x = int(parts[2][2:])
            self.y = int(parts[3][2:])

            assert (self.h >= 0 and self.w >= 0)
        except AssertionError:
            self.valid = False


def answer(window_string):
    """Obtain the area of the window specified as a string of properties. 

    This function declaration must be kept unmodified.
 
    Args:
        window_string: A string with the properties of the window, eg, 
            'X=10 Y=20 W=30 H=40'.
    Returns:
        An integer with the area of the window if the input string is 
        valid, or -1 othewise.
    """
    try:
        window = Rectangle(window_string)
        if window.valid:
            return window.w * window.h

        return -1
    except ValueError:
        return -1
