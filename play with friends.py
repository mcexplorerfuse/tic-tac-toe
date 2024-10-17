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