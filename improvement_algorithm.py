i = 0
nodes = []
node = 1
# in competition, robot will take the inputs from virtual map and motor.
"""
if there are 3 or 4 open paths:
    nodes.append(a, b)
    node = 1

else:
    node = 0
"""
inp = int(input("1-2-3-4"))
moves = []
def fwd(a):
    a += 1
    return "fwd"

def back(a):
    a -= 1
    return "back"

def right(a):
    a += 1
    return "right"

def left(a):
    a -= 1
    return "left"



if node == 0:
    """
    
    
    """

elif node == 1:

    if inp == 1:
        fwd(i)
        moves.append(fwd(i))

    elif inp == 2:
        right(i)
        moves.append(right(i))

    elif inp == 3:
        back(i)
        moves.append(back(i))

    elif inp == 3:
        left(i)
        moves.append(left(i))

    


    if (i == 0) and ("fwd" in moves and "right in moves" and "left" in moves and "back" in moves):
        leng = len(moves)
        important_move = moves[int((leng / 4) + 1)]
        other_move = moves[int(((leng / 4) + 1) + 1)]
        
        if (important_move, other_move) == ("right", "left") or ("left", "right") or ("fwd", "back") or ("back", "fwd"):
            print("don't remove the node")
        
        else:
            hr = moves[0]

            if hr == "fwd":
                back(i)

            elif hr == "back":
                fwd(i)

            elif hr == "right":
                left(i)

            elif hr == "left":
                right(i)

            nodes.remove(node)











