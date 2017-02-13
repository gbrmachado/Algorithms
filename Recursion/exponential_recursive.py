""" Algorithm to calculate exponential in O(log n) """
def expo_recur(x, n):
    """ recursive exponential """
    print x, n
    if n == 0:
        return 1
    if n == 1:
        return x
    if x == 1 or x == 0:
        return x

    v = 0
    if n % 2 == 1:
        v = x
    else:
        v = 1

    next_object = expo_recur(x, n/2)
    return v * next_object * next_object


print expo_recur(5,5)

