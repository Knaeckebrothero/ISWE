import datetime
import os.path as pt

import pandas as pd


def does_csv_exists(filepath: str):
    """
    Checks if a csv file exists in the location.
    :param filepath: the location of the csv file.
    :return: false if the file doesn't exist or the file type is not csv
    """
    filepath = filepath.strip()

    if filepath == '':
        return False

    if pt.exists(filepath):
        return pt.splitext(filepath)[1] == '.csv'

    return False


# task 1
def read_file_and_print_tail(delim: str = ";"):
    """
    Reads a csv file and print last 10 rows if exists.
    :param delim: csv file delimiter, by default ';'
    :return: Pandas DataFrame or None.
    """
    exists = does_csv_exists('../FinancialSample.csv')

    if not exists:
        return None

    data = pd.read_csv('../FinancialSample.csv', delimiter=delim)
    data = data.rename(columns=lambda x: x.strip())

    print("File read successfully. The last 10 rows:")
    print(data.tail(10))
    return data


def format_date_to_american(date_mal_formatted: datetime.date):
    """
    Formats date format to %M/%D/%Y.
    :param date_mal_formatted: datetime.date value to be formatted.
    :return: datetime.date.
    """
    return date_mal_formatted.strftime('%m/%d/%y')


# task 2
def transform_date_to_american_format(df: pd.DataFrame):
    """
    Transforms Date column from any date format to %M/%D/%Y.
    :param df: Pandas Dataframe.
    :return: Pandas Dataframe with Date column formatted.
    """
    df["Date"] = pd.to_datetime(df["Date"])
    print("formatting date to american style.")
    df["Date"] = df["Date"].transform(format_date_to_american)
    print("Date formatting is done. Here is a sample of 10 rows:")
    print(df["Date"].sample(10))
    return df


raw_data = transform_date_to_american_format(read_file_and_print_tail())


# task 3
def get_sub_dataframe(df: pd.DataFrame):
    """
    Returns a subset of data frame containing "Product", "Profit", "COGS", "Sales".
    :param df: Dataframe.
    :return: Dataframe with 4 columns "Product", "Profit", "COGS", "Sales"
    """
    return df.loc[:, ["Product", "Profit", "COGS", "Sales"]]


print(get_sub_dataframe(raw_data).sample())
