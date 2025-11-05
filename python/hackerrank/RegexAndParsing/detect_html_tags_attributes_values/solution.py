"""HackerRank Detect HTML, Tags, Attributes, Values.

This module is designed to parse HTML code snippets and extract HTML tags,
attributes, and attribute values. It processes HTML input line by line,
identifying tags and their associated attributes, and prints them in a
specific format as required by the HackerRank problem.

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).
"""
import re
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    """Custom HTML parser to extract tags, attributes and their values.

    This parser extends HTMLParser to override the handle_starttag method,
    allowing it to extract HTML tags and their attributes according to
    the specified format requirements.
    """

    def handle_starttag(self, tag: str, attrs: list) -> None:
        """Process start tags and their attributes.

        Prints the tag name and each attribute with its value in the required format.

        Parameters:
            tag (str): The name of the HTML tag
            attrs (list): List of (name, value) pairs containing the attributes
        """
        print(tag)
        for attr, value in attrs:
            print(f"-> {attr} > {value}")


def main() -> None:
    """Process HTML input and extract tags, attributes, and values.

    Reads the HTML code snippet from standard input, removes comments,
    and processes it using the custom HTML parser.
    """
    n = int(input())
    html = ""

    for _ in range(n):
        html += input() + "\n"

    # Remove HTML comments
    html = re.sub(r"<!--[\s\S]*?-->", "", html)

    # Parse the HTML
    parser = MyHTMLParser()
    parser.feed(html)


if __name__ == "__main__":
    main()