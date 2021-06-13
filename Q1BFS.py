import numpy as np

# import pandas as pd

initial_state = np.array([[2, 0, 3], [1, 8, 4], [7, 6, 5]])
final_state = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])


def left(arr_in):
    coord = np.argwhere(arr_in == 0)
    x_coord = coord[0][0]
    y_coord = coord[0][1]
    #     print(x_coord)
    #     print(y_coord)
    if (y_coord != 0):
        arr_in[x_coord][y_coord] = arr_in[x_coord][y_coord - 1]
        arr_in[x_coord][y_coord - 1] = 0
    return arr_in


def right(arr_in):
    coord = np.argwhere(arr_in == 0)
    x_coord = coord[0][0]
    y_coord = coord[0][1]
    #     print(x_coord)
    #     print(y_coord)
    if (y_coord != 2):
        arr_in[x_coord][y_coord] = arr_in[x_coord][y_coord + 1]
        arr_in[x_coord][y_coord + 1] = 0
    return arr_in


def up(arr_in):
    coord = np.argwhere(arr_in == 0)
    x_coord = coord[0][0]
    y_coord = coord[0][1]
    #     print(x_coord)
    #     print(y_coord)
    if (x_coord != 0):
        arr_in[x_coord][y_coord] = arr_in[x_coord - 1][y_coord]
        arr_in[x_coord - 1][y_coord] = 0
    return arr_in


def down(arr_in):
    coord = np.argwhere(arr_in == 0)
    x_coord = coord[0][0]
    y_coord = coord[0][1]
    #     print(x_coord)
    #     print(y_coord)
    if (x_coord != 2):
        arr_in[x_coord][y_coord] = arr_in[x_coord + 1][y_coord]
        arr_in[x_coord + 1][y_coord] = 0
    return arr_in


def check(ch_func, listToCheck):
    flag = True
    for x in listToCheck:
        if (ch_func == x).all():
            flag = False
            return flag
    return flag


def BFS(in_state, fi_state):
    state_space = []
    used_state = []
    state_space.append(in_state)

    while True:
        if (len(state_space) == 0):
            print("Not found")
            break
        else:
            popped = state_space.pop(0)
            #             print(popped)
            used_state.append(popped)
            #             print(used_state)

            if (fi_state == popped).all():
                print("Found")
                break

            temp = popped.copy()
            temp = left(temp)
            if check(temp, used_state):
                state_space.append(temp)

            temp = popped.copy()
            temp = right(temp)
            if check(temp, used_state):
                state_space.append(temp)

            temp = popped.copy()
            temp = up(temp)
            if check(temp, used_state):
                state_space.append(temp)

            temp = popped.copy()
            temp = down(temp)
            if check(temp, used_state):
                state_space.append(temp)

    return used_state


result = BFS(initial_state, final_state)

print(result)
