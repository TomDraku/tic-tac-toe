import os

game_on=True
right_sign=False

clear = lambda: os.system('cls')
dic = {'A1':' ', 'B1':' ','C1':' ', 'A2':' ', 'B2':' ','C2':' ','A3':' ', 'B3':' ','C3':' '}

def board():
    header1 = "  A "
    header2 = " B  "
    header3 = "C"
    print(header1, header2, header3)

    print(1, dic['A1'],"|", dic['B1'],"|", dic['C1'])
    print("  ----------")
    print(2, dic['A2'],"|", dic['B2'],"|", dic['C2'])
    print("  ----------")
    print(3, dic['A3'],"|", dic['B3'],"|", dic['C3'])


while game_on==True:
    
    board()
    p1 = input("Zawodnik nr 1 wybirerz pole, gdzie chcesz postawić X: ")
    
    
    while right_sign==False:
        if p1 in dic and dic[p1]==" " and dic[p1]!="O":
            dic[p1]='X'
            break
        else:
            clear()
            board()
            print('Nieprawidłowe oznaczenie pola, wybierz jeszcze raz')
            p1 = input("Zawodnik nr 1 wybirerz pole, gdzie chcesz postawić X: ")
            
    clear()
    board()
    if dic['A1']==dic['B1']==dic['C1']=='X':
        print('Wygrywa zawodnik nr 1, ktory ma krzyżyk X')
        break
        
    elif dic['A2']==dic['B2']==dic['C2']=='X':
        print('Wygrywa zawodnik nr 1, ktory ma krzyżyk X')
        break
    elif dic['A3']==dic['B3']==dic['C3']=='X':
        print('Wygrywa zawodnik nr 1, ktory ma krzyżyk X')
        break
    elif dic['A1']==dic['A2']==dic['A3']=='X':
        print('Wygrywa zawodnik nr 1, ktory ma krzyżyk X')
        break
    elif dic['B1']==dic['B2']==dic['B3']=='X':
        print('Wygrywa zawodnik nr 1, ktory ma krzyżyk X')
        break
    elif dic['C1']==dic['C2']==dic['C3']=='X':
        print('Wygrywa zawodnik nr 1, ktory ma krzyżyk X')
        break
    elif dic['A1']==dic['B2']==dic['C3']=='X':
        print('Wygrywa zawodnik nr 1, ktory ma krzyżyk X')
        break
    elif dic['C1']==dic['B2']==dic['A3']=='X':
        print('Wygrywa zawodnik nr 1, ktory ma krzyżyk X')
        break    


    p2 = input("Zawodnik nr 2 wybirerz pole, gdzie chcesz postawić O: ")
    
    while right_sign==False:
        if p2 in dic and dic[p2]==" " and dic[p2]!="X":

            dic[p2]='O'
            
            break
        else:
            clear()
            board()
            print('Nieprawidłowe oznaczenie pola,wybierz jeszcze raz')
            p2 = input("Zawodnik nr 2 wybirerz pole, gdzie chcesz postawić O: ") 
            
    clear()

    if dic['A1']==dic['B1']==dic['C1']=='O':
        board()
        print('Wygrywa zawodnik nr 1, ktory ma kółko O')
        break
    elif dic['A2']==dic['B2']==dic['C2']=='O':
        board()
        print('Wygrywa zawodnik nr 1, ktory ma kółko O')
        break
    elif dic['A3']==dic['B3']==dic['C3']=='O':
        board()
        print('Wygrywa zawodnik nr 1, ktory ma kółko O')
        break
    elif dic['A1']==dic['A2']==dic['A3']=='O':
        board()
        print('Wygrywa zawodnik nr 1, ktory ma kółko O')
        break
    elif dic['B1']==dic['B2']==dic['B3']=='O':
        board()
        print('Wygrywa zawodnik nr 1, ktory ma kółko O')
        break
    elif dic['C1']==dic['C2']==dic['C3']=='O':
        board()
        print('Wygrywa zawodnik nr 1, ktory ma kółko O')
        break
    elif dic['A1']==dic['B2']==dic['C3']=='O':
        board()
        print('Wygrywa zawodnik nr 1, ktory ma kółko O')
        break
    elif dic['C1']==dic['B2']==dic['A3']=='O':
        board()
        print('Wygrywa zawodnik nr 1, ktory ma kółko O')
        break









