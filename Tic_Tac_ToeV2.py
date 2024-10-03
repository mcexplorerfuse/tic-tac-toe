import random

A1="-"
A2="-"
A3="-"
B1="-"
B2="-"
B3="-"
C1="-"
C2="-"
C3="-"
coordinates=["A1","A2","A3","B1","B2","B3","C1","C2","C3"]

game_type=input("Play with computer:1, Play with friends:2\n")
if game_type=="1":
    Beginning=input("X mi O mu olmak istersin?")
    Beginning=Beginning.upper()
    if Beginning=="X":
        print("- - -")
        print("- - -")
        print("- - -")
        
        print("Karelerin koordinatlari aşağida verilmiştir..")
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
        
        number1=random.randint(0,8)
        coordinates.pop(number1)
        
        if number1==0:
            if not A1=="X":
                A1="O"
        elif number1==1:
            if not A2=="X":
                A2="O"
        elif number1==2:
            if not A3=="X":
                A3="O"
        elif number1==3:
            if not B1=="X":
                B1="O"
        elif number1==4:
            if not B2=="X":
                B2="O"
        elif number1==5:
            if not B3=="X":
                B3="O"
        elif number1==6:
            if not C1=="X":
                C1="O"
        elif number1==7:
            if not C2=="X":
                C2="O"
        elif number1==8:
            if not C3=="X":
                C3="O"
        print(f"{A1} {A2} {A3}")
        print(f"{B1} {B2} {B3}")
        print(f"{C1} {C2} {C3}")

        #--------------------------2-------------------------

        move2=input("koordinat: ")
        move2=move2.replace(' ','')
        move2=move2.upper()
        
        if move2=="A1":
            A1="X"
        elif move2=="A2":
            A2="X"
        elif move2=="A3":
            A3="X"
        elif move2=="B1":
            B1="X"
        elif move2=="B2":
            B2="X"
        elif move2=="B3":
            B3="X"
        elif move2=="C1":
            C1="X"
        elif move2=="C2":
            C2="X"
        elif move2=="C3":
            C3="X"
        
        number2=random.randint(0,8)
        coordinates.pop(number2)
        
        if number2==0:
            if not A1=="X":
                A1="O"
        elif number2==1:
            if not A2=="X":
                A2="O"
        elif number2==2:
            if not A3=="X":
                A3="O"
        elif number2==3:
            if not B1=="X":
                B1="O"
        elif number2==4:
            if not B2=="X":
                B2="O"
        elif number2==5:
            if not B3=="X":
                B3="O"
        elif number2==6:
            if not C1=="X":
                C1="O"
        elif number2==7:
            if not C2=="X":
                C2="O"
        elif number2==8:
            if not C3=="X":
                C3="O"
        print(f"{A1} {A2} {A3}")
        print(f"{B1} {B2} {B3}")
        print(f"{C1} {C2} {C3}")
        
#--------------------------3-------------------------

        move3=input("koordinat: ")
        move3=move3.replace(' ','')
        move3=move3.upper()
        
        if move3=="A1":
            A1="X"
        elif move3=="A2":
            A2="X"
        elif move3=="A3":
            A3="X"
        elif move3=="B1":
            B1="X"
        elif move3=="B2":
            B2="X"
        elif move3=="B3":
            B3="X"
        elif move3=="C1":
            C1="X"
        elif move3=="C2":
            C2="X"
        elif move3=="C3":
            C3="X"
        
        number3=random.randint(0,8)
        coordinates.pop(number3)
        
        if number3==0:
            if not A1=="X":
                A1="O"
        elif number3==1:
            if not A2=="X":
                A2="O"
        elif number3==2:
            if not A3=="X":
                A3="O"
        elif number3==3:
            if not B1=="X":
                B1="O"
        elif number3==4:
            if not B2=="X":
                B2="O"
        elif number3==5:
            if not B3=="X":
                B3="O"
        elif number3==6:
            if not C1=="X":
                C1="O"
        elif number3==7:
            if not C2=="X":
                C2="O"
        elif number3==8:
            if not C3=="X":
                C3="O"
        print(f"{A1} {A2} {A3}")
        print(f"{B1} {B2} {B3}")
        print(f"{C1} {C2} {C3}")
        
        
        
        #------------------------4------------------
        move4=input("koordinat: ")
        move4=move4.replace(' ','')
        move4=move4.upper()
        if move4=="A1":
            A1="X"
        elif move4=="A2":
            A2="X"
        elif move4=="A3":
            A3="X"
        elif move4=="B1":
            B1="X"
        elif move4=="B2":
            B2="X"
        elif move4=="B3":
            B3="X"
        elif move4=="C1":
            C1="X"
        elif move4=="C2":
            C2="X"
        elif move4=="C3":
            C3="X"
        number4=random.randint(0,8)
        coordinates.pop(number4)
        if number4==0:
            if not A1=="X":
                A1="O"
        elif number4==1:
            if not A2=="X":
                A2="O"
        elif number4==2:
            if not A3=="X":
                A3="O"
        elif number4==3:
            if not B1=="X":
                B1="O"
        elif number4==4:
            if not B2=="X":
                B2="O"
        elif number4==5:
            if not B3=="X":
                B3="O"
        elif number4==6:
            if not C1=="X":
                C1="O"
        elif number4==7:
            if not C2=="X":
                C2="O"
        elif number4==8:
            if not C3=="X":
                C3="O"
        print(f"{A1} {A2} {A3}")
        print(f"{B1} {B2} {B3}")
        print(f"{C1} {C2} {C3}")
        if (A1 and A2 and A3)=="X":
            print("X kazandi!")
        elif (A1 and B1 and C1)=="X":
            print("X kazandi!")
        elif (A2 and B2 and C2)=="X":
            print("X kazandi!")
        elif (A3 and B3 and C3)=="X":
            print("X kazandi!")
        elif (B1 and B2 and B3)=="X":
            print("X kazandi!")
        elif (C1 and C2 and C3)=="X":
            print("X kazandi!")
        elif (A1 and B2 and C3)=="X":
            print("X kazandi!")
        elif (A3 and B2 and C1)=="X":
            print("X kazandi!")
        else:
            if (A1 and A2 and A3)=="O":
                print("O kazandi!")
            elif (A1 and B1 and C1)=="O":
                print("O kazandi!")
            elif (A2 and B2 and C3)=="O":
                print("O kazandi!")
            elif (A3 and B3 and C3)=="O":
                print("O kazandi!")
            elif (B1 and B2 and B3)=="O":
                print("O kazandi!")
            elif (C1 and C2 and C3)=="O":
                print("O kazandi!")
            elif (A1 and B2 and C3)=="O":
                print("O kazandi!")
            elif (A3 and B2 and C1)=="O":
                print("O kazandi!")
            else:
                pass

        
        
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