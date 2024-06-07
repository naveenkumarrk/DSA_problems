# snake , water , gun game 

import random


def swg_win(mine, comp):
    if mine == comp:
        return None
    if mine == 's' and comp == 'w':
        return True
    elif mine == 'w' and comp == 'g':
        return True
    elif mine== 'g' and comp == 's':
        return True
    else:
        return False

def swg(boundry_score):
    choices = ('s', 'w', 'g')
    my_win = 0
    comp_win = 0
    
    for i in range(boundry_score):
        comp = random.choice(choices)
        mine = input("enter s, g, or w:")
        win = swg_win(mine, comp)

        if win == None:
            print(f"player entered {mine} and comp entered {comp}. It is a tie\n")
            
        elif win:
            print(f"player entered {mine} and pc entered {comp}. Player wins this round\n")
            my_win +=1
            
        else:
            print(f"player entered {mine} and pc entered {comp}. PC wins this round\n")
            comp_win+=1
            
        print(f" The total score is player : {my_win}, PC : {comp_win}\n")
        print("--" * 50)
        
    if my_win > comp_win:
        res = f"Player wins with a score of {my_win} : {comp_win}"
    elif comp_win > my_win:
        res = f"PC wins with a score of {comp_win} : {my_win}"
    else:
        res = f"It's a tie with a score of {my_win} : {comp_win}"
         
    return "The winner is " + res  

print(swg(3)) 
