import sys
import random
from typing import List

lst = [

    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]

]

storage = [0]

def fory():
	global storage
	a=int(random.random()*10)
	if a  in storage:
		return fory()
	else:
	
		return a

#    for c in lst:
#        print(*c, sep='  ')

chance = 9

global c


def printer():
    print('--+---+---+')
    for c in lst:
        for m in c:
            print(m, end=' | ')
        print(end='\n')
        print('--+---+---+')
    print(' ')


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
    global storage

    printer()
    z = int(input('Enter the position player x:  '))
    if exe(z) == True:
        storage.append(z)
        print(' ')
        chance -= 1
        converter(z)
        lst[i][j] = 'x'
    elif exe(z) == False:
        print("\nEnter different number \n")
        cut()

    if checker() == True:
        printer()
        print(' ')
        print('x is winner')
        sys.exit()

    else:
        if chance == 0:
            print('game drawn')
            printer()
            sys.exit()
    def idk():


        global chance
        printer()
        print("Player o : ")
        y = fory()
     
        if exe(y) == True:
            storage.append(y)
            print(' ')
            chance -= 1
            converter(y)
            lst[i][j] = 'o'
        elif exe(y) == False:
         
            idk()

        if checker() == True:
            printer()
            print(' ')
            print('o is winner')
            sys.exit()
    idk()




def cut():
    while chance > 0:
        game()
    else:
        print('game drawn')
        printer()
        sys.exit()


def exe(gh):
    if gh in storage:

        return False

    else:
        return True


cut()
