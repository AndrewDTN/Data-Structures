N = 5
c = [[0]*N for i in range(N)]
def access_matrix(a,b):
    global N
    global c
    for i in range(N):
        for j in range(N):
            tem = 0
            for k in range(N):
                tem += a[i][k]*b[k][j]
                #print(a[i][k], b[k][j])
            c[i][j] = tem
def main():
    global N
    a = [[0]*N for i in range(N)]
    b = [[0]*N for i in range(N)]

    for i in range(N):
        for j in range(N):
            a[i][j] = j + 1

    for i in range(N):
        for j in range(N):
            b[i][j] = 5 - j
    print(a)
    print(b)
    access_matrix(a,b)
    print(c)

main()     