import pandas as pd

df = pd.DataFrame({'a': [10, 20 , 30], 'b': [20, 30, 40]})
def my_sq(x):
    return x ** 2



def my_exp(x, n):
    return x ** n


# print(my_sq(4))

# print(my_exp(2, 4))
print(df)

print(df['a']**2)

sq = df['a'].apply(my_sq)
print(sq)

ex = df['a'].apply(my_exp, n=2)
print(ex)

ex = df['a'].apply(my_exp, n=3)
print(ex)

def print_me(x):
    print(x)

print(df.apply(print_me, axis=0))

print(df['a'])

print(df['b'])

def avg_3(x, y, z):
    return (x + y + z) / 3

def avg_3_apply(col):

    # x = col[0]
    # y = col[1]
    # z = col[2]
    # return (x + y + z) / 3

    sum = 0
    for item in col:
        sum += item
    
    return sum / df.shape[0]
print(df.apply(avg_3_apply))

#행 방향

def avg_2_apply(row):
    sum = 0
    for item in row:
        sum += item
    return sum / df.shape[1]
print(df.apply(avg_2_apply, axis=1))










