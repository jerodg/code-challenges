"""HackerRank - XML 1 - Find the Score

This module provides functionality to parse and analyze XML documents.
It specifically calculates the score of an XML document based on the number of attributes present in its elements.

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).
"""
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node: etree.Element) -> int:
    """Calculate the total number of attributes in an XML document.

    This function recursively traverses the XML tree starting from the given node,
    counting the number of attributes in each element to accumulate the total score.

    Args:
        node: The root element of the XML tree.

    Returns:
        The total number of attributes in the XML document.

    Example:
        >>> import xml.etree.ElementTree as etree
        >>> xml_str = '<root attr1="val1"><child attr2="val2"/></root>'
        >>> tree = etree.ElementTree(etree.fromstring(xml_str))
        >>> get_attr_number(tree.getroot())
        2
    """
    # Initialize count with attributes of the current node to start accumulation.
    count = len(node.attrib)
    for child in node:
        # Recurse on children to include nested attributes, ensuring all elements are covered.
        count += get_attr_number(child)

    return count


if __name__ == '__main__':
    # Skip the first line as it indicates the number of XML lines, which is not needed for parsing.
    sys.stdin.readline()
    # Read the entire remaining input as the XML string to handle multi-line documents.
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))