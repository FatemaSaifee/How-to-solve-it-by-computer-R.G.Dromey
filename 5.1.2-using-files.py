file1 = open("file1.txt", "w")

file1.write("1 2 3 4 5  89 102 112")

file1.close()

file2 = open("file2.txt", "w")

file2.write("-13 12 15 18 20 25 28 110 117 200")

file2.close()

def merge():
    with open('file1.txt', 'r') as f1:
        data = f1.read()
    a = map(int, data.split())
    
    with open('file2.txt', 'r') as f2:
        data = f2.read()
    b = map(int, data.split())    
    
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
    while i < len(l1):
        if l1[i] < l2[j]:
            c.append(l1[i])
            i+=1
        else:
            c.append(l2[j])
            j+=1
    return c,j


def copy(l1, n, c):
    for k in range(n,len(l1)):
        c.append(l1[k])
    return c
