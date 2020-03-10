# my_lambdata/my_mod.py

# Functions


def enlarge(n):
    '''
    Param n is a number
    '''
    return n * 100


def list_to_column(df, li):
    '''
    Param df is a dataframe
    Param li is a list
    '''
    import pandas as pd

    x = pd.Series(li)
    df = pd.concat(df, x, axis=1)
    return df


def return_nulls(df):
    '''
    return nulls
    '''
    output = df.isnull().sum()
    return print(output)


if __name__ == "__main__":
    # Only run the code below if this script is invoked from the command-line
    # not if it is imported from another

    print("")
    # y = int(input('Please choose a number'))
    # print(y, enlarge(y))
