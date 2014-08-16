def insertionsort(a):
    n = len (a)
    i = 0 #increasig index of no. of element ordered at each stage
    j = 0 #decreasing index used in search for insertion
    first = 0 #smallest element in array
    p = 0 #original position of smallest element
    x = 0 #current element to be insertd

    #begin

    assert n > 0

    #find minimum
    first = a[0]
    p=0
    for i in range(1,n):
        if a[i] < first:
            first = a[i]
            p = i
        a[p] = a[0]
        a[0] = first

    #insert the element
    for i in range(2,n):
        x = a[i]
        j = i
        #search for insertion position n move up elements
        while x < a[j-1] :
            a[j] = a[j-1]
            j -= 1
        a[j] = x

    return a
