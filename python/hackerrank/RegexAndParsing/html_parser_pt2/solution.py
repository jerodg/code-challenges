"""HackerRank - Regex and Parsing - HTML Parser (Part 2).

This code is part of the HackerRank Python track.
It is a solution to the problem of parsing HTML content and extracting specific data from it.
It uses regular expressions to find and extract the required information from HTML tags.
It handles nested tags and ensures that the output is formatted correctly.

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).
"""

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    """HTML Parser that extracts comments and data from HTML content."""

    def handle_comment(self, data):
        """Process HTML comments and format output based on whether they're single or multi-line."""
        if '\n' in data:
            print(">>> Multi-line Comment")
            print(data)
        else:
            print(">>> Single-line Comment")
            print(data)

    def handle_data(self, data):
        """Process text data, skipping empty or whitespace-only data."""
        if data.strip():  # Only print if data contains non-whitespace characters
            print(">>> Data")
            print(data)


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()