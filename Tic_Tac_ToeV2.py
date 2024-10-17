import random

won=False
wonText=""


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
    # winCheck'den dönen değerlerr true ise X yada O kazandı diye burada yaz.
    #hamle 3 ve 3'ten büyükse çalıştır (wincheck'i)
    isWin=winCheck()
    print(isWin)
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
    else:#-----------------------
        if selectedCoordinate=="A1":
            coordA1="O"
            coordinates[0]="O"
            print(coordA1)
        elif selectedCoordinate=="A2":
            coordA2="O"
            coordinates[1]="O"
            print(coordA2)
        elif selectedCoordinate=="A3":
            coordA3="O"
            coordinates[2]="O"
            print(coordA3)
        elif selectedCoordinate=="B1":
            coordB1="O"
            coordinates[3]="O"
            print(coordB1)
        elif selectedCoordinate=="B2":
            coordB2="O"
            coordinates[4]="O"
            print(coordB2)
        elif selectedCoordinate=="B3":
            coordB3="O"
            coordinates[5]="O"
            print(coordB3)
        elif selectedCoordinate=="C1":
            coordC1="O"
            coordinates[6]="O"
            print(coordC1)
        elif selectedCoordinate=="C2":
            coordC2="O"
            coordinates[7]="O"
            print(coordC2)
        elif selectedCoordinate=="C3":
            coordC3="O"
            coordinates[8]="O"
            print(coordC3)
    

    
def userChoice():
    move=input("koordinat: ")
    move=move.replace(' ','')
    move=move.upper()
    if not move in coordinates:
        print("Burası önceden seçilmiş.")
        userChoice()
    #kontrolü yapılcak (try except ile yapılacak)
    else:
        if move=="A1":
            coordA1="X"
            coordinates[0]="X"
            print(coordA1)
        elif move=="A2":
            coordA2="X"
            coordinates[1]="X"
            print(coordA2)
        elif move=="A3":
            coordA3="X"
            coordinates[2]="X"
            print(coordA3)
        elif move=="B1":
            coordB1="X"
            coordinates[3]="X"
            print(coordB1)
        elif move=="B2":
            coordB2="X"
            coordinates[4]="X"
            print(coordB2)
        elif move=="B3":
            coordB3="X"
            coordinates[5]="X"
            print(coordB3)
        elif move=="C1":
            coordC1="X"
            coordinates[6]="X"
            print(coordC1)
        elif move=="C2":
            coordC2="X"
            coordinates[7]="X"
            print(coordC2)
        elif move=="C3":
            coordC3="X"
            coordinates[8]="X"
            print(coordC3)
        setRandomCoordinates()

def winCheck():
    won=False
    wonText = ""
    if lineA == ["X","X","X"]:
        wonText = "X"
        won = True
    elif lineB==["X","X","X"]:
        wonText="X"
        won=True
    elif lineC==["X","X","X"]:
        wonText="X"
        won=True
    elif column1==["X","X","X"]:
        wonText="X"
        won=True
    elif column2==["X","X","X"]:
        wonText="X"
        won=True
    elif column3==["X","X","X"]:
        wonText="X"
        won=True
    elif cross1==["X","X","X"]:
        wonText="X"
        won=True
    elif cross2==["X","X","X"]:
        wonText="X"
        won=True
    else:
        if lineA==["O","O","O"]:
            wonText="X"
            won=True
        elif lineB==["O","O","O"]:
            wonText="X"
            won=True
        elif lineC==["O","O","O"]:
            wonText="X"
            won=True
        elif column1==["O","O","O"]:
            wonText="X"
            won=True
        elif column2==["O","O","O"]:
            wonText="X"
            won=True
        elif column3==["O","O","O"]:
            wonText="X"
            won=True
        elif cross1==["O","O","O"]:
            wonText="X"
            won=True
        elif cross2==["O","O","O"]:
            wonText="X"
            won=True
        else:
            pass
    result=[won,wonText]
    return result



game_type=input("Play with computer:1, Play with friends:2\n")
if game_type=="1":
    
    print("- - -")
    print("- - -")
    print("- - -")
    
    print("Karelerin koordinatlari aşağida verilmiştir.")
    print("A1 A2 A3")
    print("B1 B2 B3")
    print("C1 C2 C3")
    
    moved=0
    while moved<4:
        userChoice()
        #setRandomCoordinates()
        printBoard()
    
        winCheck()
        moved=moved+1
    

    #--------------------
        
