import numpy as np
import csv
import pandas as pd

df=pd.read_csv("../Data/write.csv")

chro_disea=df[['date_confirmation','date_death_or_discharge','outcome','chronic_disease']].dropna()
print(chro_disea)