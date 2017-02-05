# QuickSort algorithm
# Goma 03/02/2016


# It uses the first element as the partition
def partitionFirst(a, l, r):
    p = a[l]
    i = l+1
    for j in range(l+1, r):
        if a[j] < p:
            a[j], a[i] = a[i], a[j]
            i = i+1

    a[l], a[i-1] = a[i-1], a[l]
    return i-1

# It uses the last element as the partition
def partitionLast(a, l, r):
    a[r-1], a[l] = a[l], a[r-1]
    p = a[l]
    i = l+1
    for j in range(l+1, r):
        if a[j] < p:
            a[j], a[i] = a[i], a[j]
            i = i+1

    a[l], a[i-1] = a[i-1], a[l]
    return i-1

# It uses the median among l, r and the element in the middle
def partitionMedian(a, l, r):
    dist = len(a[l:r])

    if dist % 2 == 0:
        size = l + ((dist)/2 - 1)
    else:
        size = l + ((dist)/2)

    c = [a[l], a[size], a[r-1]]
    d = sorted(c)[1]
    pos = m.index(d)

    a[l], a[pos] = a[pos], a[l]
    p = a[l]
    i = l+1
    for j in range(l+1, r):
        if a[j] < p:
            a[j], a[i] = a[i], a[j]
            i = i+1

    a[l], a[i-1] = a[i-1], a[l]
    return i-1

# Quicksort method
def quicksort(a,l,r, part):
    if l < r:
        p = part(a,l,r)
        count = r-l-1
        
        l1 = quicksort(a, l, p, part)
        l2 = quicksort(a, p+1, r, part)
        
        return count + l1 + l2
    
    else:
        return 0
