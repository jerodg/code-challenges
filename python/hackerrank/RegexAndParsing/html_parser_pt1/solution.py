"""HackerRank HTML Parser Pt1.

This module provides an HTML parser that processes HTML code and outputs tag information
in a specific format, including start tags, end tags, and empty tags along with their attributes.

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).
"""

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    """Custom HTML parser that formats the output of HTML tags and attributes.

    This parser extends HTMLParser to print start tags, end tags, and empty tags
    along with their attributes according to the format specified in the problem statement.
    """

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        """Process opening HTML tags.

        Outputs the tag name prefixed with "Start : " and passes any attributes
        to the attribute printing helper method.

        Parameters:
            tag: The name of the HTML tag
            attrs: List of (name, value) pairs containing tag attributes

        Example:
            >>> parser = MyHTMLParser()
            >>> parser.feed('<div class="container">')
            Start : div
            -> class > container
        """
        print(f"Start : {tag}")
        self._print_attributes(attrs)

    def handle_endtag(self, tag: str) -> None:
        """Process closing HTML tags.

        Outputs the tag name prefixed with "End   : ".

        Parameters:
            tag: The name of the HTML tag

        Example:
            >>> parser = MyHTMLParser()
            >>> parser.feed('</div>')
            End   : div
        """
        print(f"End   : {tag}")

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        """Process empty HTML tags.

        Outputs the tag name prefixed with "Empty : " and passes any attributes
        to the attribute printing helper method.

        Parameters:
            tag: The name of the HTML tag
            attrs: List of (name, value) pairs containing tag attributes

        Example:
            >>> parser = MyHTMLParser()
            >>> parser.feed('<br data-test="value" />')
            Empty : br
            -> data-test > value
        """
        print(f"Empty : {tag}")
        self._print_attributes(attrs)

    def _print_attributes(self, attrs: list[tuple[str, str | None]]) -> None:
        """Print attributes in the required format.

        Helper method to format and print attributes of HTML tags.

        Parameters:
            attrs: List of (name, value) pairs containing tag attributes
        """
        for name, value in attrs:
            print(f"-> {name} > {value if value is not None else 'None'}")


def main() -> None:
    """Read input and parse HTML content.

    Reads the number of lines to process, collects the HTML code,
    and passes it to the parser for processing.
    """
    n = int(input())
    html_code = ""
    for _ in range(n):
        html_code += input()

    parser = MyHTMLParser()
    parser.feed(html_code)


if __name__ == "__main__":
    main()