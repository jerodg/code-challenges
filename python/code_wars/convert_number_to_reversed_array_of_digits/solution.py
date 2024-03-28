def digitize(num):
        # Convert the number to a string
    num_str = str(num)

    # Create an empty list
    digit_list = []

    # Iterate over the string in reverse order
    for char in reversed(num_str):
        # Convert each character to an integer and append to the list
        digit_list.append(int(char))

    return digit_list
