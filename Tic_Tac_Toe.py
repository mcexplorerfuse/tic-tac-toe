A={"A1":"O","A2":"O","A3":"O"}
B={"B1":"O","B2":"O","B3":"O"}
C={"C1":"O","C2":"O","C3":"O"}
X=["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
game_type=input("Play with computer:1, Play with friends:2\n")
if game_type=="1":
    Beginning=input("X mi O mu olmak istersin?")
    Beginning=Beginning.upper()
    if Beginning=="X":
        print("O O O")
        print("O O O")
        print("O O O")
        
        print("Karelerin koordinatlari aşağida verilmiştir.")
        print("A1 A2 A3")
        print("B1 B2 B3")
        print("C1 C2 C3")
        move1=input("koordinat: ")
        move1=move1.replace(' ','')
        move1=move1.upper()
        
        A=A["A1"].replace("O","X", 0)
        print(A)
        print(A["A1"] + A["A2"] + A["A3"])
        print(A["A1"] + A["A2"] + A["A3"])
        print(A["A1"] + A["A2"] + A["A3"])
        print(A["A1"])
elif game_type=="2":
    print