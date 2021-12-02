#由大到小的單向鏈結串列 1insert 2del 3modfy 4show 5exit
import sys
class Node:
    def __init__(self):
        self.name = ''
        self.point = 0
        self.next = None

head = Node()

pre = None
now = None
beh = None

def insert():
    global pre
    global now
    global beh
    global head
    
    now = Node()
    now.name = input('Write name : ')
    now.point = eval(input('Write socre : '))
    
    pre = head
    beh = head.next
    while beh != None and beh.point >= now.point:
        pre = beh
        beh = pre.next
    now.next = beh
    pre.next = now

def dele():
    global head
    global pre
    global beh
 
    del_name = ''
    if head.next == None:
        print("No data")
    else:
        pre = head
        beh = head.next
        del_name = input('Who you want delete : ')
        while beh != None and beh.name != del_name:
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

    if head.next == None:
        print("No data")
    else:
        pre = head
        beh = head.next
        mo_name = input('Who you wnat modify : ')
        while beh != None and beh.name != mo_name:
            pre = beh
            beh = pre.next
        if beh != None:
            pre.next = beh.next
            newpo = eval(input('Enter new point : '))
            now = Node()
            now.name = mo_name
            now.point = newpo
            pre = head
            beh = head.next
            while beh != None and beh.point >= newpo:
                pre = beh
                beh = pre.next
            pre.next = now
            now.next = beh
            print("Success")
        else:    
            print("No one called here")

def show():
    global head
    global beh

    beh = head.next
    while beh != None:
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