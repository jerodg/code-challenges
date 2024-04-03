#!/usr/bin/env python3.9
"""DataRobot Technical Assessment: Machine Learning Server
Copyright ©2022 Jerod Gawne <https://github.com/jerodg/>

Had to use Python3.9 as scipy doesn't support newer versions

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>."""
from os.path import realpath
from pathlib import Path

import pytest
from requests import post


@pytest.mark.asyncio
async def test_create():
    uri = 'http://127.0.0.1:8000/create'
    args = {'column_name': 'Sepal.Length'}
    resp = post(uri, params=args)

    assert resp.json() == {}
    assert resp.status_code == 200
    assert Path(realpath('./cache/iris_0.rick'))  # Check to see if the model was saved
