# for n/2,n/4,....
def shellsort2(a):
    n = len(a)
    inc = 0 #steps at which elements are to be sorted
    current = 0 #position in chain where x is finally inserted
    previous = 0 #indexof elemnet currently begin compared with x
    j = 0 #index of lowest elemnt in current chan being sorted
    k = 0 #idex of current element bieng inserted
    x = 0 #curent value to be inserted
    inserted = True #true if insertion can be made
    ctr = 0

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

#for 2^p,...,31,15,7,3,1
def shellsort1(a):
    n = len(a)
    inc = 0 #steps at which elements are to be sorted
    current = 0 #position in chain where x is finally inserted
    previous = 0 #indexof elemnet currently begin compared with x
    j = 0 #index of lowest elemnt in current chan being sorted
    k = 0 #idex of current element bieng inserted
    x = 0 #curent value to be inserted
    inserted = True #true if insertion can be made
    ctr = 0

    assert n > 0
    inc = n
    while inc > 1:
        inc = inc / 2 - 1
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
                    ctr +=1
                a[current-1] = x
                k += inc
    print a
    print ctr

a = [1,2,4,54,32,42,4,5,3,2,2,4243,31,43,42,124,4,5,2,4,56,7,5,76]
print "with n/2,n/4..."
shellsort2(a)
print "with 2^p-1,....7,3,1"
shellsort1(a)

#we observe shellsort1 is better!!!!"
