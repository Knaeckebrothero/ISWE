"""
Assignment 3: Transformation
https://github.com/Knaeckebrothero/ISWE

Group 1
Iman Osman 1351664,
Niklas Riel 1253801,
Amine Amzil 1286865,
Dusan Milenkovic 1269073
"""

import pandas as pd
import datetime


def transform_date_to_american_format(df: pd.DataFrame):
    """
    Transforms Date column from any date format to %M/%D/%Y.
    :param df: Pandas Dataframe.
    :return: Pandas Dataframe with Date column formatted.
    """

    def format_date_to_american(date_mal_formatted: datetime.date):
        """
        Formats date format to %M/%D/%Y.
        :param date_mal_formatted: datetime.date value to be formatted.
        :return: datetime.date.
        """
        return date_mal_formatted.strftime('%m/%d/%y')

    df["Date"] = pd.to_datetime(df["Date"])
    df["Date"] = df["Date"].transform(format_date_to_american)
    print("Date has been formatted to american style. Here is a sample of 10 rows:")
    print(df["Date"].sample(10))
    return df
