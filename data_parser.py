import pandas as pd


def get_data(path='slr01.csv', cols=['ListPrice', 'BestPrice'], n_rows=22):
    df = pd.read_csv(path)  # Reads in the CSV file specified
    df = df[cols]  # Gets only the specified columns
    df.fillna(0, inplace=True)  # Replaces missing values with 0.
    # returns the dataframe as a python array.
    arr = df.iloc[:n_rows].as_matrix()
    print(arr[:2, :])
    return arr


if __name__ == '__main__':
    get_data('slr01.csv')  # Driver to test the function.
