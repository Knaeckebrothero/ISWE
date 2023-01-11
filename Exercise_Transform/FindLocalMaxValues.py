# Function to find the indices for specific number of the biggest local maxima´s in the given array
import numpy as np

def findLocalMaxima(n, sample):
    # Empty lists to store points of local maxima
    indices = np.zeros((2, n))

    indices = []
    size = []

    # Function to check for local maxima
    def check(x, arr):
        if (arr[x-1] < arr[x] & arr[x+1] < arr[x]):
            indices.insert (0,arr[x] - arr[x-1] + arr[x] - arr[x+1], x)

    # Checking whether the first point is local maxima
    if (sample[0] < sample[1]):
        indices.append(0)
        size.append(0)

    # Iterating over all points to check for local maxima
    for i in range(1, n - 1):

        # Condition for local maxima
        if (sample[i - 1] < sample[i] > sample[i + 1]):
            indices.append(i)
            size.append(0)

    return indices