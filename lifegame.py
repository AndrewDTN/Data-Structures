def Count(a,i,j):
    count = 0
    for n in range(i-1,i+2):
        for m in range(j-1,j+2):
            #print(n,m)
            if n < 0 or m < 0:
                continue
            if n > len(a)-1 or m > len(a[0])-1:
                continue
            if a[n][m] == '@':
                count+=1
    if a[i][j] == '@':
        count-=1
    #print(count)
    return count
def rule(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            count = Count(a,i,j)
            if count <= 1 or count >= 4:
                a[i][j] = '-'
            if count == 2 :
                if a[i][j] == '@':
                    a[i][j] = '@'
                elif a[i][j] == '-':
                    a[i][j] = '-'
            if count == 3:
                a[i][j] = '@'
def main():
    a = [[0, 1, 0, 1, 0, 0, 0, 0, 1, 1],
        [0, 1, 0, 1, 0, 0, 0, 0, 1, 1],
        [0, 1, 0, 1, 0, 0, 0, 0, 1, 1],
        [0, 1, 1, 1, 0, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 0, 1, 0, 0, 1, 1],
        [0, 1, 0, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
        [0, 1, 0, 1, 0, 0, 1, 0, 1, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
        [0, 1, 0, 1, 1, 0, 0, 0, 1, 1]]
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 1:
                a[i][j] = '@'
            else:
                a[i][j] = '-'
    for i in range(len(a)):
        for j in range(len(a[0])):
            if j != len(a[0])-1:
                print(a[i][j],end='')
            else:
                print(a[i][j])
    while True:
        wish = input('\nWant to continue(y/n):')
        if wish == 'y':
            rule(a)
            for i in range(len(a)):
                for j in range(len(a[0])):
                    if j != len(a[0])-1:
                        print(a[i][j],end='')
                    else:
                        print(a[i][j])
        else:
            break
main()