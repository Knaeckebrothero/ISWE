"""
Assignment 2: Extract
https://github.com/Knaeckebrothero/ISWE

Group 1
Iman Osman 1351664,
Niklas Riel 1253801,
Amine Amzil 1286865,
Dusan Milenkovic 1269073
"""

# Task 1: Read the .csv by using open() and transform it in dictionary of
# the following form.
print("\n----------------Task 1----------------\n")

"""
First we create a list which contains the whole data from the csv file.
(Due to the fact that the dataset isn´t huge we can use this cheap solution.)
We also perform some basic cleanup actions. And later insert everything into a dictionary.
"""

data = []

# Load & clean the data
with open("FinancialSample.csv") as rawData:
    for d in rawData:
        # d = d.replace("\ufeff", "") For some reason the null charackter at the beginning of the file is "ï»¿" in
        # python 3.11.1 and "\ufeff" in 3.7 or lower.
        d = d.replace("ï»¿", "")
        d = d.replace("\n", "")
        d = d.split(";")
        data.append(d)

    rawData.close()

# Extract and clean the headlines for our dictionary
headlines = []

for d in data[0]:
    s = d.strip()
    s = s.replace(" ", "_")
    headlines.append(s)

# Create dictionary & print results
sample = dict.fromkeys(headlines)

for index, headline in enumerate(headlines):
    row = []

    for value in data:
        row.append((value[index]))

    row.pop(0)
    sample[headlines[index]] = row
    print(headlines[index], sample[headlines[index]])

# Task 2: Find the lowest, the highest and the average value of the column
# ”UNIT SOLD”.
print("\n----------------Task 2----------------\n")

'''
First we convert the data from string to float and put it into a list.
Then we calculate the minimum and maximum values using the corresponding functions (min()-max()).
Through sum() divided by len() we calculate the average value.
'''

# Convert values
units = []
i = len(units) - 1

for s in sample["Units_Sold"]:
    units.append(s.replace(",", "."))

units = list(map(float, units))

# Print results
print("Minumum value: ", min(units))
print("Maximum value: ", max(units))
print("Average vlaue:", sum(units) / len(units))

# Task 3: Convert all columns that have currency in dollar in a currency of your choice. Repeat for two other
# currencies.
print("\n----------------Task 3----------------\n")

"""
First we search for all the arrays that contain a dollar sign and put them in a list.
We then use the list of keys to convert the corresponding values (lists).
After cleaning them and converting the strings to floats, we rename the keys to represent the currency of the values.
Last we print the exchanged values by using exchange functions we declared above.
"""

# Check for dollar char
waehrung = []

for s in sample:
    for x in sample[s]:
        if "$" in x:
            waehrung.append(s)
            break

# Remove non char and non digit values from str
for x in waehrung:
    converted = []

    for s in sample[x]:
        v = s.replace("$", "")
        v = v.replace(".", "")
        v = v.replace(",", ".")
        v = v.replace(" ", "")
        # We chose to replace the -$ with 0, because it is easier to work with
        # (0% discount simply stands for no discount)
        v = v.replace("-", "0")
        v = v.replace("(", "")
        v = v.replace(")", "")
        converted.append(v)

    converted = list(map(float, converted))
    sample[x + "_in_Dollar"] = converted
    del sample[x]

# Conversion functions
# 1 USD = 1,05 Euro (05.12.22)


def usdToEuro(money):
    exchanged = []
    for x in money:
        exchanged.append(x * 1.05)
    # sample[w+"_in_Euro"] = exchanged
    # print(w+"$", "has been exchanged to Euro", sample[w+"_in_Euro"])
    return exchanged

# 1 USD = 136,55 Japanese Yen (05.12.22)


def usdToYen(money):
    exchanged = []
    for x in money:
        exchanged.append(x * 136.55)
    # sample[w + "_in_Yen"] = exchanged
    # print(w+"$", "has been exchanged to Yen", sample[w + "_in_Yen"])
    return exchanged

# 1 USD = 0,94 Swiss Franc (05.12.22)


def usdToSwissFranc(money):
    exchanged = []
    for x in money:
        exchanged.append(x * 0.94)
    # sample[w + "_in_Swiss_Franc"] = exchanged
    # print(w+"$", "has been exchanged to Swiss Franc", sample[w + "_in_Swiss_Franc"])
    return exchanged


# Convert to different currency
for x in waehrung:
    print(x, "in Dollar ist", sample[x + "_in_Dollar"])
    print(x, "in Euro ist", usdToEuro(sample[x + "_in_Dollar"]))
    print(x, "in Yen ist", usdToYen(sample[x + "_in_Dollar"]))
    print(x, "in Schweizer Franken ist", usdToSwissFranc(
        sample[x + "_in_Dollar"]), "\n")

# Task 4: Find the number of rows for the year 2013 and for the year 2014.
print("\n----------------Task 4----------------\n")

'''
We iterate through years and count the occurrences, so that we can then print the results.
'''

# Count number of rows
n13 = 0
n14 = 0

for year in sample["Year"]:
    if "2013" in year:
        n13 = n13 + 1
    if "2014" in year:
        n14 = n14 + 1

# Print the results
print("There are", n13, "entries for year 2013 and", n14, "for year 2014.")

# Task 5: Find the number of rows that have no Discounts.
print("\n----------------Task 5----------------\n")

'''
We iterate through discount and count the occurrences of 0, so that we can then print the cases where a 0% discount has ben given.
'''

# Count number of rows
noDiscount = 0

for y in sample["Discounts_in_Dollar"]:
    if 0 == y:
        noDiscount = noDiscount + 1

# Print the results
print("There are:", noDiscount, "entries without a discount.")

# Task 6: Change all Month Names to their corresponding numeric values
# (January = 1, February = 2, ...).
print("\n----------------Task 6----------------\n")

"""
We convert the month names into their corresponding number by using the in python 3.10 introduced switch case equevalent.
This could have also be done with nested if else cases but this approach is much better.
"""

# Initial value
converted = []

# Map every Month name to its number (only works in python 3.10 and above)
for s in sample["Month_Name"]:
    match s.strip():
        case "January":
            converted.append("1")
        case "February":
            converted.append("2")
        case "March":
            converted.append("3")
        case "April":
            converted.append("4")
        case "May":
            converted.append("5")
        case "June":
            converted.append("6")
        case "July":
            converted.append("7")
        case "August":
            converted.append("8")
        case "September":
            converted.append("9")
        case "October":
            converted.append("10")
        case "November":
            converted.append("11")
        case "December":
            converted.append("12")
        case _:
            print("Error at", len(converted), s, s.strip())
            break

# Print the results
print("The months converted to numbers:", converted)
