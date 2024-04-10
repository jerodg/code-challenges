#!/bin/bash
# This script is used to provide feedback based on the input number.
# It takes one argument, an integer, and checks if it's greater than or equal to 10.
# If the number is greater than or equal to 10, it prints "Great, now move on to tricks".
# Otherwise, it prints "Keep at it until you get it".

# The input number is stored in the variable 'n'.
n=$1

# The 'if' statement checks if the number is greater than or equal to 10.
if [ $n -ge 10 ]
then
    # If the number is greater than or equal to 10, this message is printed.
    echo "Great, now move on to tricks"
else
    # If the number is less than 10, this message is printed.
    echo "Keep at it until you get it"
fi
