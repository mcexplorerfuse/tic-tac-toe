print("Wincheck yapıldı.")
    if (coordA1 and coordA2 and coordA3)=="X":           
        wonText="X"
        won=True
    elif (coordA1 and coordB1 and coordC1)=="X":
        wonText="X"
        won=True
    elif (coordA2 and coordB2 and coordC2)=="X":
        wonText="X"
        won=True
    elif (coordA3 and coordB3 and coordC3)=="X":
        wonText="X"
        won=True
    elif (coordB1 and coordB2 and coordB3)=="X":
        wonText="X"
        won=True
    elif (coordC1 and coordC2 and coordC3)=="X":
        wonText="X"
        won=True
    elif (coordA1 and coordB2 and coordC3)=="X":
        wonText="X"
        won=True
    elif (coordA3 and coordB2 and coordC1)=="X":
        wonText="X"
        won=True
    else:
        if (coordA1 and coordA2 and coordA3)=="O":
            wonText="O"
            won=True
        elif (coordA1 and coordB1 and coordC1)=="O":
            wonText="O"
            won=True
        elif (coordA2 and coordB2 and coordC3)=="O":
            wonText="O"
            won=True
        elif (coordA3 and coordB3 and coordC3)=="O":
            wonText="O"
            won=True
        elif (coordB1 and coordB2 and coordB3)=="O":
            wonText="O"
            won=True
        elif (coordC1 and coordC2 and coordC3)=="O":
            wonText="O"
            won=True
        elif (coordA1 and coordB2 and coordC3)=="O":
            wonText="O"
            won=True
        elif (coordA3 and coordB2 and coordC1)=="O":
            wonText="O"
            won=True
        else:
            won=False
            wonText=""