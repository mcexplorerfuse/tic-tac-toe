import random
koordinatlar=["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
xo_list=["x","o"]
board=[
    [0,0,0],
    [0,0,0],
    [0,0,0],
]


def koordinat(koordinat1):
    koordinatlar.remove(koordinat1)
    xo1=input("x mi o mu\n")
    xo(xo1)
def xo(xo1):
    if koordinat1=="A1":
        if xo1=="x":    
            board=[
                ["X",0,0],
                [0,0,0],
                [0,0,0],
            ]
        elif xo1=="o":    
            board=[
                ["O",0,0],
                [0,0,0],
                [0,0,0],
            ]
    elif koordinat1=="A2":
        if xo1=="x":    
            board=[
                [0,"X",0],
                [0,0,0],
                [0,0,0],
            ]
        elif xo1=="o":    
            board=[
                [0,"O",0],
                [0,0,0],
                [0,0,0],
            ]
    elif koordinat1=="A3":
        if xo1=="x":    
            board=[
                [0,0,"X"],
                [0,0,0],
                [0,0,0],
            ]
        elif xo1=="o":    
            board=[
                [0,0,"O"],
                [0,0,0],
                [0,0,0],
            ]
    elif koordinat1=="B1":
        if xo1=="x":    
            board=[
                [0,0,0],
                ["X",0,0],
                [0,0,0],
            ]
        elif xo1=="o":    
            board=[
                [0,0,0],
                ["O",0,0],
                [0,0,0],
            ]
    elif koordinat1=="B2":
        if xo1=="x":    
            board=[
                [0,0,0],
                [0,"X",0],
                [0,0,0],
            ]
        elif xo1=="o":    
            board=[
                [0,0,0],
                [0,"O",0],
                [0,0,0],
            ]
    elif koordinat1=="B3":
        if xo1=="x":    
            board=[
                [0,0,0],
                [0,0,"X"],
                [0,0,0],
            ]
        elif xo1=="o":    
            board=[
                [0,0,0],
                [0,0,"O"],
                [0,0,0],
            ]
    elif koordinat1=="C1":
        if xo1=="x":    
            board=[
                [0,0,0],
                [0,0,0],
                ["X",0,0],
            ]
        elif xo1=="o":    
            board=[
                [0,0,0],
                [0,0,0],
                ["O",0,0],
            ]
    elif koordinat1=="C2":
        if xo1=="x":    
            board=[
                [0,0,0],
                [0,0,0],
                [0,"X",0],
            ]
        elif xo1=="o":    
            board=[
                [0,0,0],
                [0,0,0],
                [0,"O",0],
            ]
    elif koordinat1=="C3":
        if xo1=="x":    
            board=[
                [0,0,0],
                [0,0,0],
                [0,0,"X"],
            ]
        elif xo1=="o":    
            board=[
                [0,0,0],
                [0,0,0],
                [0,0,"O"],
            ]
    



def ai_coords_result(ai_coords):
    if ai_coords=="A1":
        if ai_move=="x":    
            board=[
                ["X",0,0],
                [0,0,0],
                [0,0,0],
            ]
        elif ai_move=="o":    
            board=[
                ["O",0,0],
                [0,0,0],
                [0,0,0],
            ]
    elif ai_coords=="A2":
        if ai_move=="x":    
            board=[
                [0,"X",0],
                [0,0,0],
                [0,0,0],
            ]
        elif ai_move=="o":    
            board=[
                [0,"O",0],
                [0,0,0],
                [0,0,0],
            ]
    elif ai_coords=="A3":
        if ai_move=="x":    
            board=[
                [0,0,"X"],
                [0,0,0],
                [0,0,0],
            ]
        elif ai_move=="o":    
            board=[
                [0,0,"O"],
                [0,0,0],
                [0,0,0],
            ]
    elif ai_coords=="B1":
        if ai_move=="x":    
            board=[
                [0,0,0],
                ["X",0,0],
                [0,0,0],
            ]
        elif ai_move=="o":    
            board=[
                [0,0,0],
                ["O",0,0],
                [0,0,0],
            ]
    elif ai_coords=="B2":
        if ai_move=="x":    
            board=[
                [0,0,0],
                [0,"X",0],
                [0,0,0],
            ]
        elif ai_move=="o":    
            board=[
                [0,0,0],
                [0,"O",0],
                [0,0,0],
            ]
    elif ai_coords=="B3":
        if ai_move=="x":    
            board=[
                [0,0,0],
                [0,0,"X"],
                [0,0,0],
            ]
        elif ai_move=="o":    
            board=[
                [0,0,0],
                [0,0,"O"],
                [0,0,0],
            ]
    elif ai_coords=="C1":
        if ai_move=="x":    
            board=[
                [0,0,0],
                [0,0,0],
                ["X",0,0],
            ]
        elif ai_move=="o":    
            board=[
                [0,0,0],
                [0,0,0],
                ["O",0,0],
            ]
    elif ai_coords=="C2":
        if ai_move=="x":    
            board=[
                [0,0,0],
                [0,0,0],
                [0,"X",0]
            ]
        elif ai_move=="o":    
            board=[
                [0,0,0],
                [0,0,0],
                [0,"O",0],
            ]
    elif ai_coords=="C3":
        if ai_move=="x":    
            board=[
                [0,0,0],
                [0,0,0],
                [0,0,"X"],
            ]
        elif ai_move=="o":    
            board=[
                [0,0,0],
                [0,0,0],
                [0,0,"O"],
            ]

print("Tic Tac Toe Multishot Sürümü'ne hoş geldiniz.")
print("A1  A2  A3\nB1  B2  B3\nC1  C2  C3")
koordinat1=input("koordinat:\n")
if not koordinat1 in koordinatlar:
    print("Hatalı koordinat!")
    exit(0)
koordinat(koordinat1)
#bilgisayar---------------------------------
ai_coords=random.choice(koordinatlar)
ai_move=random.choice(xo_list)
ai_coords_result(ai_coords)
print(board)