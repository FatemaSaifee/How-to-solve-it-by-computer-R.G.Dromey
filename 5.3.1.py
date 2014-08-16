def countselectionsort(a):
    i = 0 #first element in unsorted part of array
    j = 0 #index of unsorted part of array
    p = 0 #position of min
    n = len(a)
    ctr = 0
    min = 0 #current minimum

    assert n > 0

    for i in range(0,n-1):
        min = a[i]
        p = i
        for j in range(i+1 , n):
            if a[j] < min:
                min = a[j]
                p = j
                ctr += 1
        a[p] = a[i]
        a[i] = min
    return ctr

def countbubblesort(a):
    i = 0 #index for no. of passes through the array
    j = 0 #indx of unsorted part of array
    t = 0 #temporary
    ctr = 0 
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
                ctr += 1
                issorted = False
    return ctr

def compare(a):
    print "selection sort: "+ str(countselectionsort(a)) + "\n bubblesort : " + str(countbubblesort(a))
