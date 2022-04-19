import numpy as np
#This array is a visual simulation for tracking our location and movements.
array = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# This section includes movements of the maze robot.
def right(x, y):
    y = y + 1
    array[x][y] = 1 + array[x][y]
    print(array)
    return x, y

def back(x, y):
    x = x + 1
    array[x][y] = 1 + array[x][y]

    print(array)
    return x, y

def forward(x, y):

    x = x - 1
    array[x][y] = 1 + array[x][y]

    print(array)
    return x, y

def left(x, y):
    y = y - 1
    array[x][y] = 1 + array[x][y]

    print(array)
    return x, y


#This parameters will give us the info about our location.
a = 0
b = 0

#The first tile will be 1, because we will be on [0][0] initially.
array[0][0] = 1
while True:
    iterator = int(input("forward:0, back:1, right:2, left:3, minVal:4 "))
    #With the real robot, I will also add the availability of the movement. Such as barrier info..
    ilist = [array[a][b+1], array[a][b-1], array[a+1][b], array[a-1][b]]
    mini = ilist.index(min(ilist))


    if iterator == 0:
        a, b = forward(a, b)

    elif iterator == 1:
        a, b = back(a, b)

    elif iterator == 2:
        a, b = right(a, b)

    elif iterator == 3:
        a, b = left(a, b)

    elif iterator == 4:
        if mini == 0:
            a, b = right(a, b)
        elif mini == 1:
            a, b = left(a, b)
        elif mini == 2:
            a, b = back(a, b)
        elif mini == 3:
            a, b = forward(a, b)

    else:
        print("Please enter a valid number.")



