#row=列 column=行
source = [[0,15,0,0,-8,0],
          [0,0,6,0,0,0],
          [0,0,0,-6,0,0],
          [0,0,18,0,0,0],
          [0,0,0,0,0,16],
          [72,0,0,0,20,0]]
sm = [['']*3 for i in range(10)]
height=6#行
length=6#列
total = 0
sm_row=1
sm_col=1
row=0
col=0
def sm_count():
    global sm
    global total
    global row
    global col
    global sm_col
    global sm_row
    while row<=length and col<=height:
        #print("0")
        if source[row][col]!=0:
            total+=1
            sm[sm_row][0]=row+1
            sm[sm_row][1]=col+1
            sm[sm_row][2]=source[row][col]
            #print(sm[sm_row][2])
            sm_row+=1
        if col == height-1:
            if row == length-1:
                break
            row+=1
            col=0
            #print("2")
        else:
            col+=1
    sm[0][0]=length
    sm[0][1]=height
    sm[0][2]=total
def main():
    global total
    sm_count()
    #print(row)
    for i in range(total+1):
        print('1:',sm[i][0],'2:',sm[i][1],'3:',sm[i][2])
main()