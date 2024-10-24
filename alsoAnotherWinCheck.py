coordinates=["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
lineA=[coordinates[0],coordinates[1],coordinates[2]]
lineB=[coordinates[3],coordinates[4],coordinates[5]]
lineC=[coordinates[6],coordinates[7],coordinates[8]]
column1=[coordinates[0],coordinates[3],coordinates[6]]
column2=[coordinates[1],coordinates[4],coordinates[7]]
column3=[coordinates[2],coordinates[5],coordinates[8]]
cross1=[coordinates[0],coordinates[4],coordinates[8]]
cross2=[coordinates[2],coordinates[4],coordinates[3]]
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