N = 4
M = 4
A = [ ["-"]*M for i in range(N) ]
A[0] = (' ', 1, 2, 3)
A[1][0] = 1
A[2][0] = 2
A[3][0] = 3

result = False
L = ('X', '0')
xy = '-'
i = 0

def Print_A():
    global A
    for row in A:
        for elem in row:
            print(elem, end = ' ')
        print()

def Add_XY():
    global A
    global xy
    Print_A()
    print('Укажите номер строки для', xy,'(1, 2, 3):')
    stroka = int(input())
    print('Укажите номер столбца для', xy,'(1, 2, 3):')
    stolbec = int(input())
    if 1 <= stroka < 4 and 1 <= stolbec < 4:
        if A[stroka][stolbec] == '-':
            A[stroka][stolbec] = xy
        else:
            print('Эта ящейка занята, выбирете другую')
            Add_XY()
    else:
        print("Не корректно указа позиция")
        Add_XY()
    return

def Analiz():
    global result
    global xy
    for i in 1, 2, 3:
        if A[i][1] == A[i][2] == A[i][3] == xy:
            Print_A()
            print('ПОБЕДИЛ', xy, '!!!')
            result = True
            break
        if A[1][i] == A[2][i] == A[3][i] == xy:
            Print_A()
            print('ПОБЕДИЛ', xy, '!!!')
            result = True
            break
        if A[1][1] == A[2][2] == A[3][3] == xy:
            Print_A()
            print('ПОБЕДИЛ', xy, '!!!')
            result = True
            break
        if A[1][3] == A[2][2] == A[1][3] == xy:
            Print_A()
            print('ПОБЕДИЛ', xy, '!!!')
            result = True
            break
    return

while i <= 9:
    if result:
        break
    for j in L:
        i += 1
        if result:
            break
        if i > 9:
            print('Ходы закончились - Ничья')
            break
        xy = j
        Add_XY()
        if i >= 5:
            Analiz()


