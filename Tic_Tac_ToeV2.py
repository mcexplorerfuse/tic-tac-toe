import random

won=False
wonText=""


coordinateArray=["A1","A2","A3","B1","B2","B3","C1","C2","C3"]

coordinates=["A1","A2","A3","B1","B2","B3","C1","C2","C3"]




def printBoard():
    # winCheck'den dönen değerlerr true ise X yada O kazandı diye burada yaz.
    #hamle 3 ve 3'ten büyükse çalıştır (wincheck'i)
    print(f"{coordinates[0]} {coordinates[1]} {coordinates[2]}")
    print(f"{coordinates[3]} {coordinates[4]} {coordinates[5]}")
    print(f"{coordinates[6]} {coordinates[7]} {coordinates[8]}")
    


def setRandomCoordinates():
    selectedCoordinate=random.choice(coordinates)
    valueOfCoord=coordinates.index(selectedCoordinate)
    if not selectedCoordinate in coordinateArray:
        return setRandomCoordinates()
    else:#-----------------------
        if selectedCoordinate=="A1":
            coordinates[0]="O"
        elif selectedCoordinate=="A2":
            coordinates[1]="O"
        elif selectedCoordinate=="A3":
            coordinates[2]="O"
        elif selectedCoordinate=="B1":
            coordinates[3]="O"
        elif selectedCoordinate=="B2":
            coordinates[4]="O"
        elif selectedCoordinate=="B3":
            coordinates[5]="O"
        elif selectedCoordinate=="C1":
            coordinates[6]="O"
        elif selectedCoordinate=="C2":
            coordinates[7]="O"
        elif selectedCoordinate=="C3":
            coordinates[8]="O"
    


def userChoice(userType="X"):
    move=input(f"move {userType}, koordinat: ")
    move=move.replace(' ','')
    move=move.upper()
    if not move in coordinates:
        print("Burası önceden seçilmiş.")
        userChoice()
    #kontrolü yapılcak (try except ile yapılacak)
    else:
        if move=="A1":
            coordinates[0]=userType
        elif move=="A2":
            coordinates[1]=userType
        elif move=="A3":
            coordinates[2]=userType
        elif move=="B1":
            coordinates[3]=userType
        elif move=="B2":
            coordinates[4]=userType
        elif move=="B3":
            coordinates[5]=userType
        elif move=="C1":
            coordinates[6]=userType
        elif move=="C2":
            coordinates[7]=userType
        elif move=="C3":
            coordinates[8]=userType
            

            

def winCheck():
    
    lineA=[coordinates[0],coordinates[1],coordinates[2]]
    lineB=[coordinates[3],coordinates[4],coordinates[5]]
    lineC=[coordinates[6],coordinates[7],coordinates[8]]
    column1=[coordinates[0],coordinates[3],coordinates[6]]
    column2=[coordinates[1],coordinates[4],coordinates[7]]
    column3=[coordinates[2],coordinates[5],coordinates[8]]
    cross1=[coordinates[0],coordinates[4],coordinates[8]]
    cross2=[coordinates[2],coordinates[4],coordinates[6]]

    won=False
    wonText=""
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
            wonText="O"
            won=True
        elif lineB==["O","O","O"]:
            wonText="O"
            won=True
        elif lineC==["O","O","O"]:
            wonText="O"
            won=True
        elif column1==["O","O","O"]:
            wonText="O"
            won=True
        elif column2==["O","O","O"]:
            wonText="O"
            won=True
        elif column3==["O","O","O"]:
            wonText="O"
            won=True
        elif cross1==["O","O","O"]:
            wonText="O"
            won=True    
        elif cross2==["O","O","O"]:
            wonText="O"
            won=True
        else:
            won=False
    wonArray=[won,wonText]
    return(wonArray)






game_type=input("Play with computer:1, Play with friends:2\n")

print("Karelerin koordinatlari aşağida verilmiştir.")
print("A1 A2 A3")
print("B1 B2 B3")
print("C1 C2 C3")
    
if game_type=="1":
    
    
    
    moved=0
    while moved<4:
        userChoice()

        setRandomCoordinates()
        
        printBoard()
    
        wonArray=winCheck()
        moved=moved+1

        if wonArray[0]==True:
            print(f"{wonArray[1]} oyunu kazandı!")
            exit(0)
        else:
            pass
    print("Berabere!")
    exit(0)
    

    #--------------------
        
elif game_type=="2":

    moved = 0

    while moved<4:


        userChoice("X")

        printBoard()

        wonArray=winCheck()
        if wonArray[0]==True:
            print(f"{wonArray[1]} oyunu kazandı!")
            exit(0)
        else:
            pass

        userChoice("O")

        printBoard()
        
        
        wonArray=winCheck()
        moved=moved+1

        if wonArray[0]==True:
            print(f"{wonArray[1]} oyunu kazandı!")
            exit(0)
        else:
            pass

    print("Berabere!")
    exit(0)

else:
    print("Hatalı giriş!")
    exit(0)