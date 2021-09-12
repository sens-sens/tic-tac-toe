import sys
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
chance=9

global c
#for c in lst:
#   print(*c, sep='  ')


def converter(t):
    global i
    global j
    if t == 1:
        i = 0
        j = 0
        return i, j
    elif t == 2:
        i = 0
        j = 1
        return i, j
    elif t == 3:
        i = 0
        j = 2
        return i, j
    elif t == 4:
        i = 1
        j = 0
        return i, j
    elif t == 5:
        i = 1
        j = 1
        return i, j
    elif t == 6:
        i = 1
        j = 2
        return i, j
    elif t == 7:
        i = 2
        j = 0
        return i, j
    elif t == 8:
        i = 2
        j = 1
        return i, j
    elif t == 9:
        i = 2
        j = 2
        return i, j


def checker():
    if (lst[0][0] == lst[0][1] == lst[0][2] == 'x') or (lst[1][0] == lst[1][1] == lst[1][2] == 'x') or (
            lst[2][0] == lst[2][1] == lst[2][2] == 'x') or (lst[0][0] == lst[1][0] == lst[2][0] == 'x') or (
            lst[0][1] == lst[1][1] == lst[2][1] == 'x') or (lst[0][2] == lst[1][2] == lst[2][2] == 'x') or (
            lst[0][2] == lst[1][1] == lst[2][0] == 'x') or (lst[0][0] == lst[1][1] == lst[2][2] == 'x'):
        return True
    elif (lst[0][0] == lst[0][1] == lst[0][2] == 'o') or (lst[1][0] == lst[1][1] == lst[1][2] == 'o') or (
            lst[2][0] == lst[2][1] == lst[2][2] == 'o') or (lst[0][0] == lst[1][0] == lst[2][0] == 'o') or (
            lst[0][1] == lst[1][1] == lst[2][1] == 'o') or (lst[0][2] == lst[1][2] == lst[2][2] == 'o') or (
            lst[0][2] == lst[1][1] == lst[2][0] == 'o') or (lst[0][0] == lst[1][1] == lst[2][2] == 'o'):
        return True
    else:
        return False


def game():
    global chance
    for c in lst:
        print(*c, sep="  ")
    z = int(input('enter the position x '))
    chance-=1
    converter(z)
    lst[i][j] = 'x'
#    for c in lst:
#        print(*c, sep='  ')
    if checker() == True:
        print('x is winner')
        for c in lst:
            print(*c, sep='  ')
        sys.exit()
    else:
        if chance==0:
            print('game drawn')
            for c in lst:
                print(*c, sep='  ')
            sys.exit()

        for c in lst:
            print(*c, sep='  ')
        y = int(input('enter the position o '))
        chance-=1
        converter(y)
        lst[i][j] = 'o'
        if checker() == True:
            print('o is winner')
            for c in lst:
                print(*c, sep='  ')
            sys.exit()
        else:
            pass


while chance>0:
    game()
else:
    print('game drawn')
    sys.exit()