import pandas as pd

import sys

arg = sys.argv[1]

df = pd.read_csv(arg, sep=";", encoding='latin_1')

df = df.drop(df.columns[6], axis=1)

df = df.rename(columns=df.loc[1])

df = df.drop([0,1], axis=0)

df = df.reset_index(drop='True')

df.to_csv(arg, index="False")