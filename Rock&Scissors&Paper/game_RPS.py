#user WINS when he choose 1.(paper and pc take rock)
#2.(user= rock , pc= scissors)
#3.(user= scissors , pc = paper)
#else pc= wins!
# if two of them choose the same choice it's a TIE!

import random

options=['p', 'r','s']
user=input("choose one : p for paper , s for scissors , r for rock  \n")

if (user not in options):
    print ("invalid choice , please choose from the available options")
else:
    print("you choose : " + user)
    pc= random.choice(['p', 'r','s'])
    print ("pc choose: " + pc)

    if (user== pc):
        print ("TIE! No one won..")
    elif(user=='p' and pc=='r') or (user=='r' and pc=='s') or (user=='s' and pc=='p'):
        print ("YOU WIN!..")
    else:
        print ("YOU LOSE , PC WIN!..")

