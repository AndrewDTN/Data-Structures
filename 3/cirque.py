#back=前面(-) , front=後面(+) 
max = 5
tag = 0
front = max-1
back = max-1
queue = ['']*max
def add():
    global queue
    global back
    global tag
    global front
    global max
    if tag == 1 and front == back:
        print('\nqueue is full')
    else:
        front = (front+1) % max
        queue[front] = input('\nenter something:')
        if front == back:
            tag = 1
def dele():
    global queue
    global back
    global tag
    global front
    global max
    if tag == 0 and front == back:
        print('\nqueue is null')
    else:
        back = (back+1) % max
        print('\n  %s is delete'%queue[back])
        if back == front:
            tag = 0
def show():
    global queue
    global front
    global back
    global tag
    global max
    count = 0
    if tag == 0 and front == back:
        print('\nqueue is null')
    else:
        i = (back+1) % max
        print('-----------')
        while i != front:
            print('\n  %s'%queue[i])
            i = (i+1) % max
            count+=1
        print('\n  %s'%queue[i])
        print('-----------')
        count+=1
        print('total %d data'%count)
def main():
    while True:
        print('    Choose')
        print('    1.insert')
        print('    2.delete')
        print('    3.List')
        print('    4.exit')
        cho = int(input('\nEnter your choose:'))
        if cho == 1:
            add()
        elif cho == 2:
            dele()
        elif cho == 3:
            show()
        elif cho == 4:
            break
        else:
            print('\nPlease enter the coorect number')
main()