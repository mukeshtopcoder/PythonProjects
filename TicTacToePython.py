# TIC_TAC_TOE

li = [1,2,3,4,5,6,7,8,9]
choice = []
win = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
player = 'X'
flag = 1
# Playboard
while(True):
    print("\n\t      ***** TIC-TAC-TOE *****\n")
    print("\t\t",li[0]," | ",li[1]," | ",li[2])
    print("\t\t----------------")
    print("\t\t",li[3]," | ",li[4]," | ",li[5])
    print("\t\t----------------")
    print("\t\t",li[6]," | ",li[7]," | ",li[8])
    if(flag == 0):
        break
    print("\n\t\tPlayer :",player)
    if(len(choice)==9):
        print("\n\n\t\tMATCH DRAW!")
        break
    ch = int(input("\t\tEnter Choice : "))
    if(ch not in choice):
        choice.append(ch)
        li[ch-1] = player
        for place in win:
            if(li[place[0]] == li[place[1]] and li[place[1]] == li[place[2]] ):
                print("\n\n\t\tPLAYER ",player,"WINS!")
                flag = 0
        if(player == 'X'):
            player = '0'
        else:
            player = 'X'
    else:
        input("\t\tPlace Already Occupied!")
    
