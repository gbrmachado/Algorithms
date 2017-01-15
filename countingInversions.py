# Counting Inversions in an Array
# An inversion is a pair (i,j) such that i<j and A[i] > A[j]
# This algorithm uses a modified version of mergeSort to count the number of inversions
#
# Goma: 01/15/2017

def countInversionAndSort(a):
    l = len(a)
    if l == 0:
        return 0, []
    if l == 1:
        return 0, a

    m = l/2              #middle

    countLeft, sortLeft   = countInversionAndSort(a[:m]) 
    countRight, sortRight = countInversionAndSort(a[m:])

    countSplitInversion, sortedArray = countInversion(sortLeft, sortRight)
    return (countLeft + countRight + countSplitInversion), sortedArray

def countInversion(a, b):
    d = []

    lenA = len(a)
    lenB = len(b)

    nInversions = 0
    while (a and b):
        if a[0] < b[0]:
            d.append(a.pop(0))
            lenA -= 1
        else:
            d.append(b.pop(0))
            nInversions += lenA

    while (a):
        d.append(a.pop(0))
    while (b):
        d.append(b.pop(0))
    return nInversions, d


# Test Cases
print countInversionAndSort([1,2,3,4,5,6])[0] == 0
print countInversionAndSort([6,5,4,3,2,1])[0] == 15
print countInversionAndSort([1,3,5,2,4,6])[0] == 3
