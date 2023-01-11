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
import os.path as pt

def read_file(path ,delim: str = ";"):
    """
    Reads a csv file and print last 10 rows if exists.
    :param delim: csv file delimiter, by default ';'
    :return: Pandas DataFrame or None.
    """

    # Checks if File exists.
    def does_csv_exists(path: str):
        """
        Checks if a csv file exists in the location.
        :param filepath: the location of the csv file.
        :return: false if the file doesn't exist or the file type is not csv
        """
        filepath = path.strip()

        if filepath == '':
            return False

        if pt.exists(filepath):
            return pt.splitext(filepath)[1] == '.csv'

        return False

    exists = does_csv_exists(path)

    if not exists:
        return None

    data = pd.read_csv('FinancialSample.csv', delimiter=delim)
    data = data.rename(columns=lambda x: x.strip())

    return data
