import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/summer/my-project/tips.csv")
df.fillna(500,inplace=True)
print(df)




# df = pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/summer/my-project/tips.json")
# print(df)

