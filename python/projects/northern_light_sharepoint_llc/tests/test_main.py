"""
Northern Light Sharepoint LLC -> File Comparitor -> Tests

Copyright ©2024 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
"""
import pytest

from interview_projects.northern_light_sharepoint_llc.main import compare_files


def test_compare_files_happy_path():
    compare_files('./data/test_input_0.txt', './data/test_input_1.txt', './data/test_output_0.txt', './data/test_output_1.txt')
    with open('./data/test_output_0.txt') as f:
        assert f.read() == 'unique to input1\n'
    with open('./data/test_output_1.txt') as f:
        assert f.read() == 'unique to input2\n'


def test_compare_files_with_empty_files():
    compare_files('empty.txt', 'empty.txt', './data/test_output_0.txt', './data/test_output_1.txt')
    with open('./data/test_output_0.txt') as f:
        assert f.read() == ''
    with open('./data/test_output_1.txt') as f:
        assert f.read() == ''


def test_compare_files_with_nonexistent_files():
    with pytest.raises(IOError):
        compare_files('nonexistent0.txt', 'nonexistent1.txt', './data/test_output_0.txt', './data/test_output_1.txt')


def test_compare_files_with_large_files(benchmark):
    result = benchmark(compare_files, 'large1.txt', 'large2.txt', './data/test_output_0.txt', './data/test_output_1.txt')
    assert result is None


def test_compare_files_with_random_order():
    compare_files('random1.txt', 'random2.txt', './data/test_output_0.txt', './data/test_output_1.txt')
    with open('./data/test_output_0.txt') as f:
        assert sorted(f.readlines()) == ['unique to input1\n']
    with open('./data/test_output_1.txt') as f:
        assert sorted(f.readlines()) == ['unique to input2\n']


def test_compare_files_with_special_characters():
    compare_files('special1.txt', 'special2.txt', './data/test_output_0.txt', './data/test_output_1.txt')
    with open('./data/test_output_0.txt') as f:
        assert f.read() == 'unique to input1\n'
    with open('./data/test_output_1.txt') as f:
        assert f.read() == 'unique to input2\n'


def test_compare_files_with_duplicates():
    compare_files('duplicates1.txt', 'duplicates2.txt', './data/test_output_0.txt', './data/test_output_1.txt')
    with open('./data/test_output_0.txt') as f:
        assert f.read() == 'unique to input1\n'
    with open('./data/test_output_1.txt') as f:
        assert f.read() == 'unique to input2\n'


def test_compare_files_with_no_duplicates():
    compare_files('no_duplicates1.txt', 'no_duplicates2.txt', './data/test_output_0.txt', './data/test_output_1.txt')
    with open('./data/test_output_0.txt') as f:
        assert f.read() == ''
    with open('./data/test_output_1.txt') as f:
        assert f.read() == ''


def test_compare_files_with_order_preservation():
    compare_files('order1.txt', 'order2.txt', './data/test_output_0.txt', './data/test_output_1.txt')
    with open('./data/test_output_0.txt') as f:
        assert f.read() == 'unique to input1\n'
    with open('./data/test_output_1.txt') as f:
        assert f.read() == 'unique to input2\n'
