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

print countInversionAndSort([9,12,3,1,6,8,2,5,14,13,11,7,10,4,0])[0]==56

print countInversionAndSort([37,7,2,14,35,47,10,24,44,17,34,11,16,48,1,39,6,33,43,26,40,4,28,5,38,41,42,12,13,21,29,18,3,19,0,32,46,27,31,25,15,36,20,8,9,49,22,23,30,45])[0]==590

print countInversionAndSort([4,80,70,23,9,60,68,27,66,78,12,40,52,53,44,8,49,28,18,46,21,39,51,7,87,99,69,62,84,6,79,67,14,98,83,0,96,5,82,10,26,48,3,2,15,92,11,55,63,97,43,45,81,42,95,20,25,74,24,72,91,35,86,19,75,58,71,47,76,59,64,93,17,50,56,94,90,89,32,37,34,65,1,73,41,36,57,77,30,22,13,29,38,16,88,61,31,85,33,54])[0]==2372
