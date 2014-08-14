def merge(a, b):
    c=[]
    if a[-1] < b[0]:
        c = shortmerge(a)
        c = copy(b,0,c)
    elif b[-1] < a[0]:
        c = shortmerge(b)
        c = copy(a,0,c)
    else:
        if a[-1] < b[-1]:
            c,n = mergecopy(a,b)
            c = copy(b,n,c)
        else:
            c,n = mergecopy(b,a)
            c = copy(a,n,c)
    print c
    

def shortmerge(l1):
    return l1

def mergecopy(l1,l2):
    c=[]
    i=0
    j=0
    while j < len(l2):
        if l1[i] < l2[j]:
            c.append(l1[i])
            i+=1
        else:
            c.append(l2[j])
            j+=1
    c.append(l1[i])
    return c,j


def copy(l1, n, c):
    for k in range(n,len(l1)):
        c.append(l1[k])
    return c
