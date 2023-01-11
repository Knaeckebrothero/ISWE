"""
Assignment 3: Transformation
https://github.com/Knaeckebrothero/ISWE

Group 1
Iman Osman 1351664,
Niklas Riel 1253801,
Amine Amzil 1286865,
Dusan Milenkovic 1269073
"""

import datetime
import os.path as pt
import ast
import pandas as pd
import numpy as np

# Bons: Checks if File exists.
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

# Task 1: Extract the same data from the last assignment (FinancialSample.csv), but this time store it into a Pandas
# Dataframe. Return the last 10 entries.
print("\n----------------Task 1----------------\n")
def read_file(delim: str = ";"):
    """
    Reads a csv file and print last 10 rows if exists.
    :param delim: csv file delimiter, by default ';'
    :return: Pandas DataFrame or None.
    """
    exists = does_csv_exists('FinancialSample.csv')

    if not exists:
        return None

    data = pd.read_csv('FinancialSample.csv', delimiter=delim)
    data = data.rename(columns=lambda x: x.strip())

    return data

print("File read successfully! Here is a sample of 10 rows:")
print(read_file().tail(10))

# Task 2: Transform the column values of ”Date” to American format (MM/DD/YYYY) with datetime library.
print("\n----------------Task 2----------------\n")

def format_date_to_american(date_mal_formatted: datetime.date):
    """
    Formats date format to %M/%D/%Y.
    :param date_mal_formatted: datetime.date value to be formatted.
    :return: datetime.date.
    """
    return date_mal_formatted.strftime('%m/%d/%y')

def transform_date_to_american_format(df: pd.DataFrame):
    """
    Transforms Date column from any date format to %M/%D/%Y.
    :param df: Pandas Dataframe.
    :return: Pandas Dataframe with Date column formatted.
    """
    df["Date"] = pd.to_datetime(df["Date"])
    df["Date"] = df["Date"].transform(format_date_to_american)
    print("Date has been formatted to american style. Here is a sample of 10 rows:")
    print(df["Date"].sample(10))
    return df

raw_data = transform_date_to_american_format(read_file())

# Task 3: Create a new Pandas Dateframe with following columns and content (Product, Profit, COGS, Sales).
print("\n----------------Task 3----------------\n")

def get_sub_dataframe(df: pd.DataFrame):
    """
    Returns a subset of data frame containing "Product", "Profit", "COGS", "Sales".
    :param df: Dataframe.
    :return: Dataframe with 4 columns "Product", "Profit", "COGS", "Sales"
    """
    return df.loc[:, ["Product", "Profit", "COGS", "Sales"]]

print("A new Pandas Dateframe with the required columns and contents has been created. Here is a sample of 10 rows:")
print(get_sub_dataframe(raw_data).sample(10))

# Task 4: Read the columns ”Month Number, ”Month Name” and ”Year and create one single column out of it
# with a merged date.
print("\n----------------Task 4----------------\n")

# Imans way to read the csv (not compatible with Amines)
# On the list of things to be refactored later.
csv_file = open("FinancialSample.csv", 'r')

# collect the lines
file_lines = csv_file.readlines()

# add the values into lists
table = [line.replace("ï»¿", "").strip().split(';') for line in file_lines]  # --- .replace(" ", "")
table_no_title = table[1:]
new_table = (zip(*table_no_title))
new_table_list = list(new_table)
titles = table[0]

dict_l = {}
for ist, lnn in enumerate(new_table_list):
    trial_dict = {titles[ist]: new_table_list[ist]}
    dict_l.update(trial_dict)

data_frame_1 = pd.DataFrame(dict_l)

# rename the columns Year, Month Number, and Month Name to year, month, and day
# inplace=True determines that the changes occur in the current Dataframe
data_frame_1.rename(columns={'Year': 'year', 'Month Number': 'day', ' Month Name ': 'month'}, inplace=True)

# the month names are replaces with their respective month numbers
data_frame_1['month'] = data_frame_1['month'].replace([' January ', ' February ', ' March ', ' April ', ' May ', ' June ', ' July ',
                                                   ' August ', ' September ', ' October ', ' November ', ' December '],
                                                      ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])

# the to.datetime function is used to convert the year, month, and day data into a date format
merged_date = pd.to_datetime(data_frame_1[['year', 'month', 'day']])

# the columns year, month, and day are removed
data_frame_1 = data_frame_1.drop('year', axis=1)
data_frame_1 = data_frame_1.drop('month', axis=1)
data_frame_1 = data_frame_1.drop('day', axis=1)

# the merged date column is added to the Dataframe with the name "Merged Data"
data_frame_1['Merged Date'] = merged_date

print("Columns have been combined. Here is a sample of 10 rows:")
print(merged_date.sample(10))

# Task 5: Find the position of the ten biggest local max values. A local max value is a value, that is surrounded by
# two lower values. For example: [1, 3, 8, 5, 10, 4] → 8 and 10 are local max values, so the result would
# be position 2 and position 4
print("\n----------------Task 5----------------\n")

#Remove non char and non digit values from str
sample = []

for s in read_file().get("Sales"):
    v = s.replace("$", "")
    v = v.replace(".", "")
    v = v.replace(",", ".")
    v = v.replace(" ", "")
    v = v.replace("-", "0")
    v = v.replace("(", "")
    v = v.replace(")", "")
    sample.append(ast.literal_eval(v))

def findLocalMaxima(arr):
    # Empty lists to store points of
    # local maxima and minima
    mx = []
    n = len(arr)

    # Iterating over all points to check
    # local maxima and local minima
    for i in range(1, n - 1):

        # Condition for local maxima
        if (arr[i - 1] < arr[i] > arr[i + 1]):
            mx.append(i)

    return mx

print("The ten biggest local max values are:")
print(np.sort(findLocalMaxima(sample))[-10:])

# Task 6: Create a new dataframe with every X entry of the data, use panda specific functions to achieve this (pandas
# is mandatory to use). X is the group number.
print("\n----------------Task 6----------------\n")

# a new Dataframe is created with every 4th data entry with help of the iloc function.
# the reset_index function creates an index that starts at 0 and increments by 1, the drop=True statement removes the column with the old indexs
new_data_frame = pd.DataFrame(data_frame_1.iloc[::4, :].reset_index(drop = True))

print("A new Dataframe has been created with every 4th data entry. Here is a sample of 10 rows:")
print(new_data_frame.sample(10))

# Task 7: While reading in the csv change all values in the discount column (this means in the pandas.read csv
# function itself) and change the discount column values by the following logic:
# if ”-” and ≤ 200→”Low”
# elif > 200 and < 2000→”Medium”
# elif ≥ 2000→”High”
print("\n----------------Task 7----------------\n")

print(pd.read_csv('FinancialSample.csv', delimiter=";"))
