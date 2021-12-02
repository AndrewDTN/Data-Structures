#由大到小的環狀鏈結串列 1insert 2del 3modfy 4show 5exit
class Node:
    def __init__(self):
        self.name = ''
        self.point = 0
        self.next = None

head = Node()
head.next = head

pre = None
now = None
beh = None

def insert():
    global head
    global pre
    global now
    global beh

    now = Node()
    now.name = input('Write name : ')
    now.point = eval(input('Write socre : '))

    pre = head
    beh = head.next
    while beh != head and now.point <= beh.point:
        pre = beh
        beh = pre.next
    pre.next = now
    now.next = beh

def dele():
    global head
    global pre
    global beh

    del_name = ''
    if head.next == head:
        print("No data")
    else:
        pre = head
        beh = head.next
        del_name = input('Who you want delete : ')
        while beh.name != del_name and beh != head:
            pre = beh
            beh = pre.next
        if beh.name == del_name:
            pre.next = beh.next
        else:
            print("No one called here")

def modify():
    global head
    global pre
    global beh
    global now

    if head.next == head:
        print("No data")
    else:
        pre = head
        beh = pre.next
        mo_name = input('Who you want modify : ')
        while beh.name != mo_name and beh != head:
            pre = beh
            beh = pre.next
        if beh != head:
            pre.next = beh.next
            now = Node()
            now.name = mo_name
            now.point = eval(input('Enter new point : '))
            pre = head
            beh = head.next
            while beh != head and now.point <= beh.point:
                pre = beh
                beh = pre.next
            pre.next = now
            now.next = beh
        else:
            print("No one called here")

def show():
    global head
    global beh

    beh = head.next
    while beh != head:
        print("%-17s %-15d" %(beh.name,beh.point))
        beh = beh.next            

def main():
    option = 0
    while True:
        print('    Choose')
        print('    1.insert')
        print('    2.delete')
        print('    3.modify')
        print('    4.show')
        print('    5.exit')
    
        try:
            option = int(input('chose : '))
        except:
            print("No number in here.\n")

        if option == 1:insert()
        elif option == 2:dele()
        elif option == 3:modify()
        elif option == 4:show()
        elif option == 5:break
main()