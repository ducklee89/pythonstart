import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

dates = pd.date_range('20120101', periods=6)

print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

print(df)

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

print(df2)

print(df2.dtypes)

print(df.head())
print(df.tail(3))

print(df.index)
print(df.columns)

print(df2.to_numpy)

print(df.describe())
print(df.T)

print()
print(df.sort_index(axis=1, ascending=True))
print()
print(df.sort_values(by='B'))

print('\n')
print(df['A'])

print()
print(df[0:3])
print()
print(df['20120102':'20120105'])

print()
print(df.loc[dates[0]])

print(df.loc[:, ['A', 'C']]) # 'A', 'C' 열을 나타냄

print(df.loc['20120103':'20120105', ['A', 'B']])

print(df.loc['20120102', ['A', 'B']])

print(df.loc[dates[0], 'A'])

print(df.at[dates[0], 'A'])

print(df.iloc[3])
print()
print(df.iloc[3:5, 0:2])
print(df.iloc[[1, 2, 4], [0, 2]])

print(df.iloc[1:3, :])

print(df.iloc[:, 1:3])

print(df.iloc[1, 1])
print(df.iat[1, 1])

print(df[df.A > 0])
print(df[df > 0])

df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df2)

print(df2[df2['E'].isin(['two', 'four'])])

s1 = pd.Series([1, 2, 3, 4, 5, 6, 7], index=pd.date_range('20120102', periods=7))

print(s1)

df['F'] = s1
print(df['F'])

df.at[dates[0], 'A'] = 0

df.iat[0, 1] = 0
df.loc[:, 'D'] = np.array([5] * len(df))

print(df)

df2 = df.copy()
df2[df2 > 0] = -df2
print(df2)

df1 = df.reindex(index=dates[0:4], columns=list(df.columns)+['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1

print(df1)



