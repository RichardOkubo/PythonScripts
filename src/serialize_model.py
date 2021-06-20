"""Serializing and deserializing Logistic Regression models in JSON."""

import json

import numpy as np
from sklearn.linear_model import LogisticRegression


def logistic_regression_to_json(model, file):
    data = {}
    data['init_params'] = model.get_params()
    data['model_params'] = mp = {}

    for p in ('coef_', 'intercept_','classes_', 'n_iter_'):
        mp[p] = getattr(model, p).tolist()

    with open(file, "w") as f:
        json.dump(data, f)


def logistic_regression_from_json(filename):
    with open(filename, "r") as f:
        data = json.load(f)

    model = LogisticRegression(**data['init_params'])

    for name, p in data['model_params'].items():
        setattr(model, name, np.array(p))

    return model


if __name__ == "__main__":

    import pandas as pd
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import LabelEncoder

    path_db = 'db/risco_credito2.csv'

    df = pd.read_csv(path_db)

    X = df.iloc[:, :4].values
    Y = df.iloc[:, 4].values

    labelencoder = LabelEncoder()
    for i in range(X.shape[1]):
        X[:, i] = labelencoder.fit_transform(X[:, i])

    model = LogisticRegression()
    model.fit(X, Y)

    x = [
        [0, 0, 1, 2],  # história boa, dívida alta, garantias nenhuma, renda > 35
        [3, 0, 0, 0]   # história ruim, dívida alta, garantias adequada, renda < 15
    ]

    y_1 = model.predict(x)
    y_2 = model.predict_proba(x)

    filename = 'model.json'
    #logistic_regression_to_json(model, filename)
    #new_model = logistic_regression_from_json(model, filename)
