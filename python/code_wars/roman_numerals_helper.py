"""CodeWars Roman Numerals Helper.

This module provides functionality to convert between Roman numerals and integers.
It includes two main functions: one for converting integers to Roman numerals and
another for converting Roman numerals to integers. The module adheres to the modern
rules of Roman numeral representation (e.g., 4 is represented as IV, not IIII).

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).

Contents:
    - to_roman: Converts an integer to a Roman numeral.
    - from_roman: Converts a Roman numeral to an integer.
"""

# Mapping of Roman numeral symbols to their integer values
_ROMAN_TO_INT = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}


class RomanNumerals:
    """A utility class for converting between integers and Roman numerals.

    This class provides two static methods:
    - `to_roman`: Converts an integer to a Roman numeral.
    - `from_roman`: Converts a Roman numeral to an integer.

    The class adheres to the modern rules of Roman numeral representation.
    """

    @staticmethod
    def to_roman(n: int) -> str:
        """Convert an integer to a Roman numeral.

        This method takes an integer input and converts it to its Roman numeral
        representation. The input must be in the range 1 <= n < 4000.

        Parameters:
            n (int): The integer to convert to a Roman numeral.

        Returns:
            str: The Roman numeral representation of the input integer.

        Raises:
            ValueError: If the input integer is not in the range 1 <= n < 4000.

        Example:
            >>> RomanNumerals.to_roman(1990)
            'MCMXC'
            >>> RomanNumerals.to_roman(4)
            'IV'
        """
        if not (1 <= n < 4000):
            raise ValueError("Input must be in the range 1 <= n < 4000.")

        result = []
        for roman, value in _ROMAN_TO_INT.items():
            # Iteratively append the Roman numeral while reducing the integer value
            while n >= value:
                result.append(roman)
                n -= value  # Subtract the value from the number
        return "".join(result)

    @staticmethod
    def from_roman(roman: str) -> int:
        """Convert a Roman numeral to an integer.

        This method takes a Roman numeral string and converts it to its integer
        representation. The input must follow the modern Roman numeral rules.

        Parameters:
            roman (str): The Roman numeral to convert to an integer.

        Returns:
            int: The integer representation of the input Roman numeral.

        Raises:
            ValueError: If the input string is not a valid Roman numeral.

        Example:
            >>> RomanNumerals.from_roman("MCMXC")
            1990
            >>> RomanNumerals.from_roman("IV")
            4
        """
        index = 0
        result = 0
        roman_length = len(roman)

        while index < roman_length:
            # Check for two-character symbols (e.g., "CM", "IV")
            if index + 1 < roman_length and roman[index : index + 2] in _ROMAN_TO_INT:
                result += _ROMAN_TO_INT[roman[index : index + 2]]
                index += 2  # Skip the next character
            elif roman[index] in _ROMAN_TO_INT:
                result += _ROMAN_TO_INT[roman[index]]
                index += 1  # Move to the next character
            else:
                raise ValueError(f"Invalid Roman numeral: {roman}")

        return result
