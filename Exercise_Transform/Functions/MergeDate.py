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

