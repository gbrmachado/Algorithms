# Longest Increasing Subsequence.
# Input is a sequence of numbers
# output is to find the increasing subsequence of greatest length.
#

import unittest

def longest_subsequence(array):
    """ It returns the longest subsequence of an array of integers """
    L = [[]] * len(array)   # It contains the longest subsequence until array[j]
    L[0] = [array[0]]       # The longest subsequence of array[0] is array[0]
    longest = []            # It contains the longest subsequence of the problem
    for i in range(1, len(array)):
        subarray = []
        for j in range(0, i):
            # It gets the biggest subsequence until the position i
            # The biggest subsequence at position i is the biggest until i-1 plus 1
            if array[j] < array[i] and len(L[i]) < len(L[j]):
                subarray = list(L[j])

        subarray.append(array[i])
        L[i] = list(subarray)
        if len(L[i]) > len(longest):
            longest = L[i]
    return longest

# Tests
ARRAY = [3, 2, 6, 4, 5, 1]
print longest_subsequence(ARRAY) == [2, 4, 5]
