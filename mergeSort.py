# Count the number of inversions of an array
# an inversion is (i,j) such that i<j and A[i] > A[j]

def mergeSort(a):
    l = len(a)
    if l == 0:
        return []
    if l == 1:
        return a

    m = l/2              #middle

    sortLeft = mergeSort(a[:m]) 
    sortRight = mergeSort(a[m:])
    return merge(sortLeft, sortRight)

def merge(a, b):
    d = []

    while (a and b):
        if a[0] < b[0]:
            d.append(a.pop(0))
        else:
            d.append(b.pop(0))

    while (a):
        d.append(a.pop(0))
    while (b):
        d.append(b.pop(0))
    return d

print mergeSort([1,2,3,4,5,6])
print mergeSort([6,5,4,3,2,1])
print mergeSort([9,4,2,12,1,7,23,5])
