def bubblesort(a):
    i = 0 #index for no. of passes through the array
    j = 0 #indx of unsorted part of array
    t = 0 #temporary
    issorted = False #if true then array is sorted
    n = len(a)
    assert n > 0

    while (i < n) and not issorted :
        issorted = True
        i += 1

        for j in range(0, n-i):
            if a[j] > a[j+1] :
                t = a[j]
                a[j] =a[j+1]
                a[j+1] = t
                issorted = False
    return a
