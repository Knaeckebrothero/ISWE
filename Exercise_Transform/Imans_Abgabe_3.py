# TASK 1
import pandas
from datetime import datetime

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
# print(dict_l)

data_frame_1 = pandas.DataFrame(dict_l)


# TASK 4

# rename the columns Year, Month Number, and Month Name to year, month, and day
# inplace=True determines that the changes occur in the current Dataframe
data_frame_1.rename(columns={'Year': 'year', 'Month Number': 'day', ' Month Name ': 'month'}, inplace=True)

# the month names are replaces with their respective month numbers
data_frame_1['month'] = data_frame_1['month'].replace([' January ', ' February ', ' March ', ' April ', ' May ', ' June ', ' July ',
                                                   ' August ', ' September ', ' October ', ' November ', ' December '],
                                                      ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])

# the to.datetime function is used to convert the year, month, and day data into a date format
merged_date = pandas.to_datetime(data_frame_1[['year', 'month', 'day']])

# the columns year, month, and day are removed
data_frame_1 = data_frame_1.drop('year', axis=1)
data_frame_1 = data_frame_1.drop('month', axis=1)
data_frame_1 = data_frame_1.drop('day', axis=1)

# the merged date column is added to the Dataframe with the name "Merged Data"
data_frame_1['Merged Date'] = merged_date
#print(date_frame)


# TASK 6

# a new Dataframe is created with every 4th data entry with help of the iloc function.
# the reset_index function creates an index that starts at 0 and increments by 1, the drop=True statement removes the column with the old indexs
new_data_frame = pandas.DataFrame(data_frame_1.iloc[::4, :].reset_index(drop = True))
print(new_data_frame)