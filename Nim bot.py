#From wikipedia:

#Nim is a mathematical combinatorial game in which two players take turns removing (or "nimming") objects from distinct heaps or piles. On each turn, a player must remove at least one object, and may remove any number of objects provided they all come from the same heap or pile. Depending on the version being played, the goal of the game is either to avoid taking the last object or to take the last object. "

#The goal of this version is to take the last object.

#Every nim position is either "winning" in that the player going next can force a win, or "losing" in that the player going next will always lose if their opponent doesn't make a mistake. In my personal experience, it's not that hard to learn the winning strategy if someone explains it, but it's extremely difficult to work out the strategy just by watching someone play optimally. See if you can figure out how the bot plays before reading the code!

#This is a bot that plays nim "well". That is to say it will always win a winning position, and in a losing position it will "try its best" to let its human opponent make a mistake, where "try its best" means keep as many objects in the game as possible to make calculations harder for the human. 

#Maybe some improvement could be made in losing positions. Currently it picks a random pile to remove one object from, but it could maybe pick the pile more cleverly or consider more than just maximising the number of objects left, such as trying to disguise when it knows it has a losing position.

#The bot will automatically remove heaps of size 0 if you input them.

#To input a position where there are n heaps of size x_1, x_2, ... , x_n, please enter the numbers separated by a space, i.e. "x_1 x_2 ... x_n"

#At the start and after the bot has taken its turn, it will ask you to input the position after your turn.

#In a sense this bot always plays first, but if you would like to play first, choose your initial setup then, as your first input, enter the setup that the game is in after your first move 

import secrets

def nim_sum(x):
    x = [i for i in x if i != 0]
    ans = 0
    for i in x:
        ans = ans^i
    
    return (ans)


def nim_move(x):
    x = [i for i in x if i != 0]
    s = nim_sum(x)
    if s == 0:
        heap = secrets.randbelow(len(x))
        x[heap]-=1
    else:
        for i in range(len(x)):
            if nim_sum([s,x[i]]) < x[i]:
                x[i] = nim_sum([s,x[i]])
                break

    return(x)
    
def main():
    li = list(map(int, input("Welcome to the nim bot. To start, please enter the starting setup: ").split()))
    items_left = sum(li)
    while items_left > 0:
        li = list(map(int, input("I made my move, the piles now look like this: " + str(nim_move(li)) + " your turn!").split()))         
        items_left = sum(li)

main()


#stop invalidinputs
#change message at end of game

#add comments to functions
