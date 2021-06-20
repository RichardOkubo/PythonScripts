import pandas as pd
from pingouin import ancova

dados = {}

df = pd.DataFrame(data=dados)

ancova(data=df, dv="x", covar="z", between="y")
