""" Given a randomly ordered set of n integers,
sort them into non-descending order using the selection sort.
"""
def selectionsort(a, n):
    i = 0 #first element in unsorted part of array
    j = 0 #index of unsorted part of array
    p = 0 #position of min
    min = 0 #current minimum

    assert n > 0

    for i in range(0,n-1):
        min = a[i]
        p = i
        for j in range(i+1 , n):
            if a[j] < min:
                min = a[j]
                p = j
        a[p] = a[i]
        a[i] = min
    return a
