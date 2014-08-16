""" Given a randomly ordered set of n integers,
sort them into non-descending order using the selection sort.
"""
def rselectionsort(a, n):
    i = 0 #first element in unsorted part of array
    j = 0 #index of unsorted part of array
    p = 0 #position of min
    max = 0 #current maximum

    assert n > 0

    for i in range(0,n-1):
        max = a[i]
        p = i
        for j in range(i+1 , n):
            if a[j] > max:
                max = a[j]
                p = j
        a[p] = a[i]
        a[i] = max
    return a
