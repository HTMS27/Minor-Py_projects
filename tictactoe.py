import random


def trap(p):
    r=[[p[j][i] for j in range(len(p))] for i in range(len(p[0]))]
    return r

print("1-Single player\n 2-multiplayer")


seq=["x","o"]
if input("enter no:")=="1":
    print("*"*20+"pick the choice x or o")
    print("-"*40)
    user=input("-"*20+"your choice:")
    seq.remove(user)
    print("py choice is {}".format(seq[0]))##pythohn choice
    choi=1
    

else:
    print("*"*20+"pick the choice x or o")
    print("-"*40)
    user=input("-"*20+"your choice:")
    seq.remove(user)
    user2=print("-"*20+"player2  is {}".format(seq[0]))
    choi=2
    


ct=0
ct2=0
ct3=0
while True:
    print(""" 00  | 01   | 02    
-----|------|----
 10  | 11   | 12  
-----|------|----
 20  | 21   | 22""")
    re=[['','',''],['','',''],['','','']]
    y=[user]*3
    b=[seq[0]]*3
    pycho=[]
    for i in range(3):
        for j in range(3):
            pycho.append([i]+[j])
    
    i=0
    while i<4:
        m=str(input("player1 no:"))
        try:
            ro=int(m[0])
            co=int(m[1])
            re[ro][co]=user
            pycho.remove([ro,co])
            if y in re or [re[0][0],re[1][1],re[2][2]]==y or [re[0][2],re[1][1],re[2][0]]==y or y in trap(re):
            #ct=ct+1
                print("-"*10+"you Win player2 loss")
                ct=ct+1
                break
        except Exception as e:
            print("not valid")
            continue
        if choi==1: 
            py=random.choice(pycho)
            re[py[0]][py[1]]=seq[0]
            pycho.remove([py[0],py[1]])
            
        
        for u in re:
            print(u)
            print(" \n")


        if choi==2:
            n=str(input("player2 no:"))
            ro1=int(n[0])
            co1=int(n[1])
            pycho.remove([ro1,co1])
            re[ro1][co1]=seq[0]

        
                                            
        
        for u in re:
            print(u)
            print(" \n")
        i=i+1


        if y in re or [re[0][0],re[1][1],re[2][2]]==y or [re[0][2],re[1][1],re[2][0]]==y or y in trap(re):
            #ct=ct+1
            print("-"*10+"you Win player2 loss")
            ct=ct+1
            break
        if b in re or [re[0][0],re[1][1],re[2][2]]==b or [re[0][2],re[1][1],re[2][0]]==b or b in trap(re):
            #ct=ct+1
            print("-"*10+"You loss player2 wins")
            ct2=ct2+1
            break
        
    else:
        print("-"*10+"DRAW")
        ct3=ct3+1

    print("""    PLAYER1 WINS:{}
    PLAYER2 WINS:{}
    DRAW        :{}
        """.format(ct,ct2,ct3))
    print("c-continue || q-quit")
    ui=input("c or q")
    if ui=='c':
        continue
    if ui=='q':
        break

        








        

