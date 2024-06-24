import pandas as pd
import texthero

df = pd.read_csv('clean.csv')


ob_cols = df.select_dtypes(include='object').columns

for column in ob_cols:
    df[column] = texthero.preprocessing.lowercase(df[column])



df.info()