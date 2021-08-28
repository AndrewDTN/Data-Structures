def compare(a,b):
    if a == b:
        return '='
    elif a < b:
        return '<' 
    elif a > b:
        return '>'

def padd(a,b,c):
    m = a[0]
    n = b[0]
    r = p = q = 1
    while r < 2*m and p < 2*n:
        res = compare(a[r],b[p]) 
        if res == '=':
            c[q+1] = a[r+1]+b[p+1]
            c[q] = a[r]
            q+=2
            r+=2
            p+=2
            print("1")
        elif res == '<':
            c[q+1] = b[p+1]
            c[q] = b[p]
            q+=2
            p+=2
            print("2")
        elif res == '>':
            c[q+1] = a[r+1]
            c[q] = a[r]
            q+=2
            r+=2
            print("3")
    while r < 2*m:
        c[q+1] = a[r+1]
        c[q] = a[r]
        q+=2
        r+=2
        print("4")
    while p < 2*n:
        c[q+1] = b[p+1]
        c[q] = b[p]
        q+=2
        p+=2
        print("5")
    c[0] = q //2

def main():
    A=[]
    B=[]
    A.append(3)
    A.append(4)
    A.append(5)
    A.append(2)
    A.append(3)
    A.append(0)
    A.append(2)

    B.append(3)
    B.append(6)
    B.append(6)
    B.append(4)
    B.append(2)
    B.append(0)
    B.append(1)

    C = [0]*10

    padd(A,B,C)
    print(A)
    print(B)
    print('[',end='')
    for i in range(C[0]*2+1):
        if i == C[0]*2:
            print(C[i],end='')
        else:
            print(C[i],',',end='')
    print(']')
main()