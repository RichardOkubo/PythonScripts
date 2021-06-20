from pickle import dump, load

import pandas as pd
from statsmodels.tsa.ar_model import AR

link = "arquivo.csv"
df.data = pd.to_datetime(df.data)
df.set_index("data", inplace=True)

ar = AR(df.valor, freq="MS").fit(2)
# ar.predict(start='2020-05-01', end='2020-05-01')

dump(ar, open("ar.sav", "wb"))
# ar_carregado = load(open('<caminho?>ar.sav', 'rb'))
