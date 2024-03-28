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
import pytest
from os import remove
from os.path import realpath
from requests import post


@pytest.mark.asyncio
async def test_predict_success():
    uri = 'http://127.0.0.1:8000/predict'
    args = {'target': '0'}
    resp = post(uri, params=args, data={'input_line': '5.7,2.8,4.1,1.3,versicolor'})

    assert resp.json() == {'species_prediction': 'versicolor'}
    assert resp.status_code == 200


@pytest.mark.asyncio
async def test_predict_failure():
    try:
        remove(realpath('./cache/iris_0.rick'))  # Deleting the cached model so we can prove the failure
    except FileNotFoundError:  # If it's not there we can continue with the test
        pass

    uri = 'http://127.0.0.1:8000/predict'
    args = {'target': '0'}
    resp = post(uri, params=args, data={'input_line': '5.7,2.8,4.1,1.3,versicolor'})

    assert resp.status_code == 404
