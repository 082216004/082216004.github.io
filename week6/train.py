import pandas as pd

#pd.set_option('display.max_rows', 10)
# pd.set_option('display.max_columns', 10)
df = pd.read_csv('./dataset/train.csv')
print(df)
xx = df["Survived"]
print(xx)