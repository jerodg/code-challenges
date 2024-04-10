def hoop_count(n):
    """
    This function determines the feedback for a hula hoop performer based on the number of hoops they can handle.

    Parameters:
    n (int): The number of hoops the performer can handle.

    Returns:
    str: Encouraging message for the performer. If the performer can handle 10 or more hoops, they are encouraged to move on to tricks.
         Otherwise, they are encouraged to keep practicing.
    """
    return "Great, now move on to tricks" if n >= 10 else "Keep at it until you get it"
