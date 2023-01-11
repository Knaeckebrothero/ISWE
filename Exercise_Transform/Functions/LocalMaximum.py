"""
Assignment 3: Transformation
https://github.com/Knaeckebrothero/ISWE

Group 1
Iman Osman 1351664,
Niklas Riel 1253801,
Amine Amzil 1286865,
Dusan Milenkovic 1269073
"""


# Function to locate the local maximums
def find(arr):
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
