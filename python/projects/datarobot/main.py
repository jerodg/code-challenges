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
import numpy as np
import pandas as pd
import pickle
from fastapi import FastAPI, Form, Response
from os.path import realpath
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from typing import NoReturn, Optional, Union

from models.input_line import InputLine
from models.prediction import Prediction

"""Project Notes
It would seem that the /predict endpoint (ep) is missing a parameter (column_name) 
or something that we could use to try loading the existing model from.
At least that is what I understood as the /create ep has a column_name argument.

If I take a csv line as input how do I know which field matches the model?
- The model doesn't contain column names, It only contains the one columns data as per 'column_name'
- When I load the model again and feed it four columns of data it returns an error because it's 
  only expecting one column.

Or the column_name argument in create is not necessary. This seems the most logical to me as 
I imagine it would be hard to make a prediction using only one data field.

In the problem overview document you don't specify at all in the /predict ep which field from
the input_line to use. If you want this model cached you'll need to store the target column
as well as request it in the ep.

Ultimately I just picked a solution and went with it; It should still function close
enough to what is expected.
"""
app = FastAPI()


async def train(df: pd.DataFrame, target: str) -> NoReturn:
    # Separate features and target
    data = df.values
    loc = df.columns.get_loc(target)
    x = data[:, 0:loc + 1]
    y = data[:, 4]

    # Split the data to train and test the dataset
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    # Support vector machine algorithm
    svn = SVC()
    svn.fit(x_train, y_train)

    # Cache model to disk
    with open(realpath(f'./cache/iris_{loc}.rick'), 'wb') as f:
        pickle.dump(svn, f)


@app.post('/create', status_code=200)
async def create(column_name: str, dataset: Optional[str] = 'iris'):
    # Read source dataset
    df = pd.read_csv(realpath(f'./data/{dataset}.csv'), header=0)

    await train(df, column_name)

    return Response()


@app.post('/predict', status_code=200)
async def predict(target: int, input_line: str = Form(InputLine)) -> Union[Prediction, Response]:
    col = input_line.split(',')[target]

    # Try and load existing model
    try:
        with open(realpath(f'./cache/iris_{target}.rick'), 'rb') as f:
            model = pickle.load(f)

        return Prediction(species_prediction=model.predict(np.array([col]).reshape(-1, 1))[0])
    except FileNotFoundError:
        print('file not found')
        return Response(status_code=404)

    # Since we're using one column of 4; we need to reshape, so it fits the model
