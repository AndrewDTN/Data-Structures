max = 20
formula = ['']*max

def Convert():
    global max
    global formula
    
    top = i = 0
    symbol=['']*max
    
    bformula = str(input('Please enter formula:'))
    while i < len(bformula):
        formula[i] = bformula[i]
        i+=1

    formula[i+1] = '#'

    print('Ans:',end='')
    symbol[top] = '#'

    for j in range(i+2):
        if formula[j] == '+' or  formula[j] == '-' or formula[j] == '*' or formula[j] == '/' or formula[j] == '^' or formula[j] == '(':
            while compare(formula[j],symbol[top]) == 1:
                print(symbol[top],end='')
                top-=1
            top+=1
            symbol[top] = formula[j]
        elif formula[j] == ')' :
            while symbol[top] != '(':
                print(symbol[top],end='')
                top-=1
            top-=1
        elif formula[j] == '#':
            while symbol[top] != '#':
                print(symbol[top],end='')
                top-=1
        else:
            print(formula[j],end='')
def compare(formula,symbol):
    for_tem = []
    sym_tem = []
    count1 = 0
    count2 = 0

    for_tem.append('#')
    for_tem.append(')')
    for_tem.append('+')
    for_tem.append('-')
    for_tem.append('*')
    for_tem.append('/')
    for_tem.append('^')
    for_tem.append(' ')
    for_tem.append('(')

    sym_tem.append('#')
    sym_tem.append('(')
    sym_tem.append('+')
    sym_tem.append('-')
    sym_tem.append('*')
    sym_tem.append('/')
    sym_tem.append('^')
    sym_tem.append(' ')

    while for_tem[count1] != formula:
        count1+=1
        #print(count1)
    while sym_tem[count2] != symbol:
        #print(symbol)
        count2+=1
    
    if (count2 // 2) >= (count1 // 2):
        return 1
    else:
        return 0

def main(): # 主函數
    print('\n***************************')
    print('       -- 有效運算子 --       ')
    print(' ^：次方')
    print(' *：成       	/：除')
    print(' +：加       	-：減')
    print(' (：左括號    	)：右括號')
    print('*****************************')
    
    Convert()
main()