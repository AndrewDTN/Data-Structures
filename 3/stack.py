max = 3
stack = [''] * max
count = -1
def Insert():
    global max
    global stack
    global count
    if count >= max-1:
        print('\nstack is full')
    else:
        count+=1
        stack[count] = input('\nenter something:')
def Delete():
    global stack
    global count
    if count < 0:
        print('\nstack is null')
    else:
        print('\n  %s is delete'%stack[count])
        count-=1
def Show():
    global stack
    global count
    if count<0:
        print('\nstack is null')
    else: 
        i = count
        num = 0
        print('-----------')
        while i>=0:
            print('\n  %s'%stack[i])
            i-=1
            num+=1
        print('-----------')
        print('total %d data'%num)
def main():
    while True:
        print('    Choose')
        print('    1.insert')
        print('    2.delete')
        print('    3.List')
        print('    4.exit')
        cho = int(input('\nEnter your choose:'))
        if cho == 1:
            Insert()
        elif cho == 2:
            Delete()
        elif cho == 3:
            Show()
        elif cho == 4:
            break
        else:
            print('\nPlease enter the coorect number')
main()