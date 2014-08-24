def shellsort(a):
    n = len(a)
    inc = 0 #steps at which elements are to be sorted
    current = 0 #position in chain where x is finally inserted
    previous = 0 #indexof elemnet currently begin compared with x
    j = 0 #index of lowest elemnt in current chan being sorted
    k = 0 #idex of current element bieng inserted
    x = 0 #curent value to be inserted
    inserted = True #true if insertion can be made
    ctr=0

    assert n > 0
    inc = n
    while inc > 1:
        inc = inc / 2
        for j in range(1, inc + 1):
            k = j + inc
            while k <= n :
                inserted = False
                #print "in while"
                x = a[k-1]
                current = k
                previous = current - inc
                while (previous >= j) and not inserted:
                    if x < a[previous-1]:
                        a[current-1] = a[previous-1]
                        current = previous
                        previous -= inc
                        
                        #print "in while inner"
                    else:
                        inserted = True
                    ctr += 1
                a[current-1] = x
                k += inc
    print a
    print ctr

def insertionsort(a):
    n = len (a)
    i = 0 #increasig index of no. of element ordered at each stage
    j = 0 #decreasing index used in search for insertion
    first = 0 #smallest element in array
    p = 0 #original position of smallest element
    x = 0 #current element to be insertd
    ctr = 0

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
            ctr += 1
        a[j] = x

    print a
    print ctr


a=[23,45,2,3,4,5,6,77,6,7,5,6,5,4,3,5,6,7,5,5,546,6,4,4,4534,65,65,4,5]
print "inertion sort : "
insertionsort(a)
print "\n\n shell sort"
shellsort(a)
