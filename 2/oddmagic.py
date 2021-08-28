def define (a):
    k = len(a[0])
    m = 0
    n = k // 2
    a[m][n] = 1
    m-=1
    n-=1
    for i in range(2,k*k+1):
        if a[m][n] == 0:
            if m < 0 and n < 0:
                m+=2
                n+=1
                a[m][n] = i
                #print(a[m][n],m,n)
            elif m < 0 and n >= 0:
                m = k-1
                a[m][n] = i
                #print(a[m][n],m,n)
            elif m >= 0 and n < 0:
                n = k-1
                a[m][n] = i
                #print(a[m][n],m,n)
            elif m >= 0 and n >= 0:
                a[m][n] = i
                #print(a[m][n],m,n)
            m-=1
            n-=1
        elif a[m][n] > 0:
            m+=2
            n+=1
            a[m][n] = i
            #print(a[m][n],m,n)
            m-=1
            n-=1
def main():
    num = 0
    while True:
        num = int(input('\nEnter odd matrix number:'))
        if num % 2 == 0:
            print('Please enter odd number') 
        else:
            break
    a = [[0]*num for i in range(num)]
    define(a)
    for i in range(num):
        for j in range(num):
            if j == num-1:
                print(a[i][j])
            else:
                print('%-4d'%a[i][j],end='')

main()