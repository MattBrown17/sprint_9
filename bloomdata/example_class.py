import pandas as pd

# Builds my class of type DataFrame
# df holds a DataFrame 'object'
# when I create a new object and save it to a variable
#     I say that I have "instantiated" that object
df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

if __name__ == '__main__':
    # Variables in the object are called "attributes"
    # can be accessed by using dot notation
    print(df.shape)
    print(df.dtypes)
    print(df.index)
    print(df.columns)

    # Functions that are part of an object are called "methods"
    # 

    print(df.head())
    print(df.describe())
    print(df.isnull())
    print(df['a'].value_counts()) # Method of the Series assocated with column 'a' of the Data Frame
