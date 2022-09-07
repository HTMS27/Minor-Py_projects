import random

ct=0
d=0
dr=0
print("{} for rock// {} for scissor// {} for paper".format('r','s','p'))
while True:
    p=str(input("give ur choice: "))
    if p not in ['s','r','p']:
        print("-"*6,"give right choice\n")
    else:
        c=random.choice("rps")
        
        if p==c:
            print("computer choice:",c)
            print("no win or loss!")
            dr=dr+1
            print(" #LOSS {}\n".format(d),"#WINS {}\n".format(ct),"#DRAWS {}".format(dr))
            
        else:
            if (p=='s' and c=='p') or (p=='r' and c=='s') or (p=='p' and c=='r'):
                print("computer choice:",c)
                print("you win!!")
                ct=ct+1
                print(" #LOSS {}\n".format(d),"#WINS {}\n".format(ct),"#DRAWS {}".format(dr))
    
                st=str(input("press q for exit.. or any key for continue.."))
            else:
                print("computer choice:",c)
                d=d+1
                print("you loss!!")
                print(" #LOSS {}\n".format(d),"#WINS {}\n".format(ct),"#DRAWS {}".format(dr))

                st=str(input("press q for exit.. or any key for continue.."))

    
        if st=='q':
            print("bye..")
            break
