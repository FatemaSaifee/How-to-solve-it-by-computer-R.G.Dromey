def shellsort(a):
    n = len(a)
    inc = 0 #steps at which elements are to be sorted
    current = 0 #position in chain where x is finally inserted
    previous = 0 #indexof elemnet currently begin compared with x
    j = 0 #index of lowest elemnt in current chan being sorted
    k = 0 #idex of current element bieng inserted
    x = 0 #curent value to be inserted
    inserted = True #true if insertion can be made

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
                a[current-1] = x
                k += inc
    print a
