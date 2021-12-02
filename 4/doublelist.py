#由大到小的雙向鏈結串列 1insert 2del 3modfy 4show 5exit

class Node:
    def __init__(self):
        self.name = ''
        self.point = 0
        self.Lnode = None
        self.Rnode = None

head = Node()
head.Lnode = head
head.Rnode = head

pre = None
now = None
beh = None

def insert():
    global head
    global pre
    global now
    global beh

    pre = head
    beh = pre.Rnode
    now = Node()
    now.name = input("Write name : ")
    now.point = eval(input("Write point : "))

    while beh != head and beh.point >= now.point:
        pre = beh
        beh = pre.Rnode
    pre.Rnode = now
    now.Lnode = pre
    now.Rnode = beh
    beh.Lnode = now

def dele():
    global head
    global pre
    global beh

    if head.Rnode == head:
        print("There is no data")
    else:
        pre = head
        beh = pre.Rnode
        del_name = input("Who you want delete : ")
        while del_name != beh.name and beh != head:
            pre = beh
            beh = pre.Rnode
        if del_name == beh.name:
            pre.Rnode = beh.Rnode
            beh.Rnode.Lnode = pre
        else:
            print("No one called here")

def modify():
    global head
    global pre
    global beh
    global now

    if head.Rnode == head:
        print("There is no data")
    else:
        pre = head
        beh = pre.Rnode
        now = Node()
        mod_name = input("Who you want modify : ")
        while mod_name != beh.name and beh != head:
            pre = beh
            beh = pre.Rnode
        if mod_name == beh.name:
            pre.Rnode = beh.Rnode
            beh.Rnode.Lnode = pre
            now.name = mod_name
            now.point = eval(input("Your new point : "))
            pre = head
            beh = pre.Rnode
            while beh != head and beh.point >= now.point:
                pre = beh
                beh = pre.Rnode
            pre.Rnode = now
            now.Lnode = pre
            now.Rnode = beh
            beh.Lnode = now
        else:
            print("No one clled here") 

def show():
    global head
    global beh

    beh = head.Rnode
    while beh != head:
        print("%-17s %-15d" %(beh.name,beh.point))
        beh = beh.Rnode

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