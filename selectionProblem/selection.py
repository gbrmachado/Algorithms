import random
random.seed()
def selection(array, l, r, k):
    print array, l, r, k
    p_index = random.randint(l, r)
    pivot = array[p_index]
    array[0], array[p_index] = array[p_index], array[0]

    i = l+1
    for j in range(l+1, r):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i += 1


    array[i-1], array[0] = array[0], array[i-1]
    pos = i-1

    if pos == k:
        return array[pos]
    elif pos > k:
        selection(array,pos+1, r, abs(k-l))
    else:
        selection(array, l, pos, abs(k - pos + 1))


ar = [5,3,7,2,4,1]
print selection(ar,0,len(ar), 3)
