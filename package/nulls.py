import pandas as pd 

def nulls(df):
    desc = df.describe()
    null_desc = pd.concat([df.isna().sum(), desc.T],
     axis=1, sort=True).set_axis(['Nulls']+list(desc.index), axis=1, inplace=False)
    return null_desc

