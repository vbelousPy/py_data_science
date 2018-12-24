import pandas as pd

pd.DataFrame({
    'x': [1, 2, 3],
    'y': [True, False, False]
})

df = pd.read_csv("shots.csv", sep=",")
# print(df.describe())
print(df.info())
print(list(df.head()))

print(df.loc[(df['angle'] < -60) & (df['is_goal'].values == 1)])
