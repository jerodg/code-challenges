"""Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.

This program is free software: you can redistribute it and/or modify it under the terms of the
Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
for more details.

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software. You should have received a copy of the SSPL along with this
program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
"""
from code_wars.string_incrementer import increment_string


def test_strings_without_numbers() -> None:
    """Test incrementing strings that don't end with numbers."""
    assert increment_string("foo") == "foo1"
    assert increment_string("") == "1"
    assert increment_string("abc") == "abc1"


def test_strings_with_numbers() -> None:
    """Test incrementing strings that end with numbers."""
    assert increment_string("foobar23") == "foobar24"
    assert increment_string("foo9") == "foo10"
    assert increment_string("foobar0") == "foobar1"
    assert increment_string("foobar99") == "foobar100"
    assert increment_string("foobar999") == "foobar1000"


def test_strings_with_leading_zeros() -> None:
    """Test preserving leading zeros in the incremented numbers."""
    assert increment_string("foo0042") == "foo0043"
    assert increment_string("foo099") == "foo100"
    assert increment_string("foo00") == "foo01"
    assert increment_string("foo001") == "foo002"
    assert increment_string("foo0999") == "foo1000"


def test_strings_with_only_numbers() -> None:
    """Test incrementing strings that consist only of numbers."""
    assert increment_string("123") == "124"
    assert increment_string("999") == "1000"
    assert increment_string("0") == "1"
    assert increment_string("0001") == "0002"


def test_edge_cases() -> None:
    """Test edge cases for incrementing strings."""
    assert increment_string("foo0") == "foo1"
    assert increment_string("1") == "2"
    assert increment_string("009") == "010"
    assert increment_string("fo9fo") == "fo9fo1"  # Number not at the end