import hashlib
import pandas as pd
import json

datos=pd.read_csv('data.csv',header=None)
df=pd.DataFrame(data=datos)
archivojson=df.iloc[1,1]

