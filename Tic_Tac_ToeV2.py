import random

won=False


coordA1="-"
coordA2="-"
coordA3="-"
coordB1="-"
coordB2="-"
coordB3="-"
coordC1="-"
coordC2="-"
coordC3="-"

lineA=[coordA1,coordA2,coordA3]
lineB=[coordB1,coordB2,coordB3]
lineC=[coordC1,coordC2,coordC3]
column1=[coordA1,coordB1,coordC1]
column2=[coordA2,coordB2,coordC2]
column3=[coordA3,coordB3,coordC3]
cross1=[coordA1,coordB2,coordC3]
cross2=[coordC1,coordB2,coordA3]

coordinates=["A1","A2","A3","B1","B2","B3","C1","C2","C3"]

def printBoard():

    print(f"{coordinates[0]} {coordinates[1]} {coordinates[2]}")
    print(f"{coordinates[3]} {coordinates[4]} {coordinates[5]}")
    print(f"{coordinates[6]} {coordinates[7]} {coordinates[8]}")


def setRandomCoordinates():
    selectedCoordinate=random.choice(coordinates)
    print(selectedCoordinate)
    valueOfCoord=coordinates.index(selectedCoordinate)
    print(valueOfCoord)
    if not coordinates[valueOfCoord]==selectedCoordinate:
        setRandomCoordinates()
    else:
        if selectedCoordinate=="A1":
            A1="O"
            coordinates[0]="O"
            print(A1)
        elif selectedCoordinate=="A2":
            A2="O"
            coordinates[1]="O"
            print(A2)
        elif selectedCoordinate=="A3":
            A3="O"
            coordinates[2]="O"
            print(A3)
        elif selectedCoordinate=="B1":
            B1="O"
            coordinates[3]="O"
            print(B1)
        elif selectedCoordinate=="B2":
            B2="O"
            coordinates[4]="O"
            print(B2)
        elif selectedCoordinate=="B3":
            B3="O"
            coordinates[5]="O"
            print(B3)
        elif selectedCoordinate=="C1":
            C1="O"
            coordinates[6]="O"
            print(C1)
        elif selectedCoordinate=="C2":
            C2="O"
            coordinates[7]="O"
            print(C2)
        elif selectedCoordinate=="C3":
            C3="O"
            coordinates[8]="O"
            print(C3)
    

    
def userChoice():
    move=input("koordinat: ")
    move=move.replace(' ','')
    move=move.upper()
    moveIndex=coordinates.index(move)
    if not coordinates[moveIndex]==move:
        userChoice()
    else:
        if move=="A1":
            A1="X"
            coordinates[0]="X"
            print(A1)
        elif move=="A2":
            A2="X"
            coordinates[1]="X"
            print(A2)
        elif move=="A3":
            A3="X"
            coordinates[2]="X"
            print(A3)
        elif move=="B1":
            B1="X"
            coordinates[3]="X"
            print(B1)
        elif move=="B2":
            B2="X"
            coordinates[4]="X"
            print(B2)
        elif move=="B3":
            B3="X"
            coordinates[5]="X"
            print(B3)
        elif move=="C1":
            C1="X"
            coordinates[6]="X"
            print(C1)
        elif move=="C2":
            C2="X"
            coordinates[7]="X"
            print(C2)
        elif move=="C3":
            C3="X"
            coordinates[8]="X"
            print(C3)

def winCheck():
    if (coordA1 and coordA2 and coordA3)=="X":
        print("X kazandi!")
        
        exit(0)
    elif (coordA1 and coordB1 and coordC1)=="X":
        print("X kazandi!")
        
        exit(0)
    elif (coordA2 and coordB2 and coordC2)=="X":
        print("X kazandi!")
        
        exit(0)
    elif (coordA3 and coordB3 and coordC3)=="X":
        print("X kazandi!")
        
        exit(0)
    elif (coordB1 and coordB2 and coordB3)=="X":
        print("X kazandi!")
        
        exit(0)
    elif (coordC1 and coordC2 and coordC3)=="X":
        print("X kazandi!")
        
        exit(0)
    elif (coordA1 and coordB2 and coordC3)=="X":
        print("X kazandi!")
        
        exit(0)
    elif (coordA3 and coordB2 and coordC1)=="X":
        print("X kazandi!")
        
        exit(0)
    else:
        if (coordA1 and coordA2 and coordA3)=="O":
            print("O kazandi!")
            
            exit(0)
        elif (coordA1 and coordB1 and coordC1)=="O":
            print("O kazandi!")
            
            exit(0)
        elif (coordA2 and coordB2 and coordC3)=="O":
            print("O kazandi!")
            
            exit(0)
        elif (coordA3 and coordB3 and coordC3)=="O":
            print("O kazandi!")
            
            exit(0)
        elif (coordB1 and coordB2 and coordB3)=="O":
            print("O kazandi!")
            
            exit(0)
        elif (coordC1 and coordC2 and coordC3)=="O":
            print("O kazandi!")
            
            exit(0)
        elif (coordA1 and coordB2 and coordC3)=="O":
            print("O kazandi!")
            
            exit(0)
        elif (coordA3 and coordB2 and coordC1)=="O":
            print("O kazandi!")
            
            exit(0)
        else:
            pass




game_type=input("Play with computer:1, Play with friends:2\n")
if game_type=="1":
    
    print("- - -")
    print("- - -")
    print("- - -")
    
    print("Karelerin koordinatlari aşağida verilmiştir.")
    print("A1 A2 A3")
    print("B1 B2 B3")
    print("C1 C2 C3")
    
    userChoice()
    
    setRandomCoordinates()
    
    printBoard()
    
    #--------------------------2-------------------------
    userChoice()
    setRandomCoordinates()
    
    printBoard()
    
#-------------------------3-------------------------
    userChoice()
    setRandomCoordinates()
    printBoard()
    
    winCheck()
    if not won==True:
        while not won==True:
            userChoice()
            setRandomCoordinates()
            printBoard()
            winCheck()
    else:
        exit(0)

        
        
elif game_type=="2":
    xyz=0
    while xyz<9:
        print("- - -")
        print("- - -")
        print("- - -")

        print("Karelerin koordinatlari aşağida verilmiştir.")
        print("A1 A2 A3")
        print("B1 B2 B3")
        print("C1 C2 C3")
        move1=input("koordinat: ")
        move1=move1.replace(' ','')
        move1=move1.upper()

        if move1=="A1":
            A1="X"
        elif move1=="A2":
            A2="X"
        elif move1=="A3":
            A3="X"
        elif move1=="B1":
            B1="X"
        elif move1=="B2":
            B2="X"
        elif move1=="B3":
            B3="X"
        elif move1=="C1":
            C1="X"
        elif move1=="C2":
            C2="X"
        elif move1=="C3":
            C3="X"
#2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2--2-2-2-2-2
        
        print(f"{A1} {A2} {A3}")
        print(f"{B1} {B2} {B3}")
        print(f"{C1} {C2} {C3}")
        move1=input("koordinat: ")
        move1=move1.replace(' ','')
        move1=move1.upper()

        if move1=="A1":
            A1="O"
        elif move1=="A2":
            A2="O"
        elif move1=="A3":
            A3="O"
        elif move1=="B1":
            B1="O"
        elif move1=="B2":
            B2="O"
        elif move1=="B3":
            B3="O"
        elif move1=="C1":
            C1="O"
        elif move1=="C2":
            C2="O"
        elif move1=="C3":
            C3="O"

        if A1=="X":
            if B1=="X":
                if C1=="X":
                   print("X kazandi!")
                else:
                    pass
            elif A2=="X":
                if A3=="X":
                    print("X kazandi!") 
                else:
                    pass
            
            else:
                pass
        else:
            pass
    


#recursion fonksiyonları (recursive)