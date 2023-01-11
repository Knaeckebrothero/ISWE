"""
Assignment 3: Transformation
https://github.com/Knaeckebrothero/ISWE

Group 1
Iman Osman 1351664,
Niklas Riel 1253801,
Amine Amzil 1286865,
Dusan Milenkovic 1269073
"""

import ast
import pandas as pd
import numpy as np

from Functions import ReadCSV as read
from Functions import ReformateDate as reformate
from Functions import MergeDate as merge
from Functions import LocalMaximum as locMax

# Task 1: Extract the same data from the last assignment (FinancialSample.csv), but this time store it into a Pandas
# Dataframe. Return the last 10 entries.
print("\n----------------Task 1----------------\n")

print("File read successfully! Here is a sample of 10 rows:")
print(read.read_file("FinancialSample.csv").tail(10))

# Task 2: Transform the column values of ”Date” to American format (MM/DD/YYYY) with datetime library.
print("\n----------------Task 2----------------\n")

raw_data = reformate.transform_date_to_american_format(read.read_file("FinancialSample.csv"))

# Task 3: Create a new Pandas Dateframe with following columns and content (Product, Profit, COGS, Sales).
print("\n----------------Task 3----------------\n")

df: pd.DataFrame = raw_data

print("A new Pandas Dateframe with the required columns and contents has been created. Here is a sample of 10 rows:")
print(df.loc[:, ["Product", "Profit", "COGS", "Sales"]].sample(10))

# Task 4: Read the columns ”Month Number, ”Month Name” and ”Year and create one single column out of it
# with a merged date.
print("\n----------------Task 4----------------\n")

print("Columns have been combined. Here is a sample of 10 rows:")
print(merge.merged_date.sample(10))

# Task 5: Find the position of the ten biggest local max values. A local max value is a value, that is surrounded by
# two lower values. For example: [1, 3, 8, 5, 10, 4] → 8 and 10 are local max values, so the result would
# be position 2 and position 4
print("\n----------------Task 5----------------\n")

# Remove non char and non digit values from str
sample = []

for s in read.read_file("FinancialSample.csv").get("Sales"):
    v = s.replace("$", "")
    v = v.replace(".", "")
    v = v.replace(",", ".")
    v = v.replace(" ", "")
    v = v.replace("-", "0")
    v = v.replace("(", "")
    v = v.replace(")", "")
    sample.append(ast.literal_eval(v))

# Call the function and print the ten largest results
print("The ten biggest local max values are:")
print(np.sort(locMax.find(sample))[-10:])

# Task 6: Create a new dataframe with every X entry of the data, use panda specific functions to achieve this (pandas
# is mandatory to use). X is the group number.
print("\n----------------Task 6----------------\n")

# a new Dataframe is created with every 4th data entry with help of the iloc function.
# the reset_index function creates an index that starts at 0 and increments by 1, the drop=True statement removes the column with the old indexs
new_data_frame = pd.DataFrame(merge.data_frame_1.iloc[::4, :].reset_index(drop=True))

print("A new Dataframe has been created with every 4th data entry. Here is a sample of 10 rows:")
print(new_data_frame.sample(10))

# Task 7: While reading in the csv change all values in the discount column (this means in the pandas.read csv
# function itself) and change the discount column values by the following logic:
# if ”-” and ≤ 200→”Low”
# elif > 200 and < 2000→”Medium”
# elif ≥ 2000→”High”
print("\n----------------Task 7----------------\n")

print(pd.read_csv('FinancialSample.csv', delimiter=";"))
