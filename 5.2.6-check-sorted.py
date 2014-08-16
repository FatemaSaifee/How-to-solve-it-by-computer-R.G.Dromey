""" Given a randomly ordered set of n integers,
sort them into non-descending order using the selection sort.
"""
def sort(a):
    i = 0 #first element in unsorted part of array
    j = 0 #index of unsorted part of array
    p = 0 #position of min
    min = 0 #current minimum
    flag = 0
    
    n = len(a)
    assert n > 0
    for i in range(0,n-1):
        min = a[i]
        p = i
        for j in range(i+1 , n):
            
            if a[j] < min:
                min = a[j]
                p = j
                flag = 1
                break
        if flag == 1:
            break
        a[p] = a[i]
        a[i] = min
    if flag == 1 :
        return False
    return True
