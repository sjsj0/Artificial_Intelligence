#!/usr/bin/env python
# coding: utf-8

# # Hill Climbing (8 puzzle)

# In[9]:


import numpy as np
import pandas as pd
import random


# In[10]:


initial_state = np.array([[2,8,3],[1,5,4],[7,6,0]])
final_state = np.array([[1,2,3],[8,0,4],[7,6,5]])

# initial_state = np.array([[1,4,2],[0,3,5],[6,7,8]])
# final_state = np.array([[1,0,2],[3,4,5],[6,7,8]])


# In[11]:


def left(arr_in):
    coord = np.argwhere(arr_in == 0)
    x_coord = coord[0][0]
    y_coord = coord[0][1]
#     print(x_coord)
#     print(y_coord)
    if(y_coord!=0):
        arr_in[x_coord][y_coord]=arr_in[x_coord][y_coord-1]
        arr_in[x_coord][y_coord-1]=0
    return arr_in



def right(arr_in):
    coord = np.argwhere(arr_in == 0)
    x_coord = coord[0][0]
    y_coord = coord[0][1]
#     print(x_coord)
#     print(y_coord)
    if(y_coord!=2):
        arr_in[x_coord][y_coord]=arr_in[x_coord][y_coord+1]
        arr_in[x_coord][y_coord+1]=0
    return arr_in


def up(arr_in):
    coord = np.argwhere(arr_in == 0)
    x_coord = coord[0][0]
    y_coord = coord[0][1]
#     print(x_coord)
#     print(y_coord)
    if(x_coord!=0):
        arr_in[x_coord][y_coord]=arr_in[x_coord-1][y_coord]
        arr_in[x_coord-1][y_coord]=0
    return arr_in


def down(arr_in):
    coord = np.argwhere(arr_in == 0)
    x_coord = coord[0][0]
    y_coord = coord[0][1]
#     print(x_coord)
#     print(y_coord)
    if(x_coord!=2):
        arr_in[x_coord][y_coord]=arr_in[x_coord+1][y_coord]
        arr_in[x_coord+1][y_coord]=0
    return arr_in


# count of misplaced tiles...
def cal_heuristics(a,b):
    return np.sum(a != b)


# In[12]:


def HillClimbing(in_state, fi_state):
    used_states=[]
    old_heuristics = cal_heuristics(in_state,fi_state)

    while True:
        print("Old Heuristics")
        print(old_heuristics)
        used_states.append(in_state)
        flag = False
        if (fi_state == in_state).all():
            print(" Path Found!!")
            return used_states
            break

        if (flag == False):
            temp = in_state.copy()
            temp = left(temp)
            new_heuristics = cal_heuristics(temp,fi_state)
            print(new_heuristics)
            if ( new_heuristics < old_heuristics):
                old_heuristics = new_heuristics
                in_state = temp.copy()
                flag = True

        if (flag == False):        
            temp = in_state.copy()
            temp = right(temp)
            new_heuristics = cal_heuristics(temp,fi_state)
            print(new_heuristics)
            if ( new_heuristics < old_heuristics):
                old_heuristics = new_heuristics
                in_state = temp.copy()
                flag = True

        if (flag == False):
            temp = in_state.copy()
            temp = up(temp)
            new_heuristics = cal_heuristics(temp,fi_state)
            print(new_heuristics)
            if ( new_heuristics < old_heuristics):
                old_heuristics = new_heuristics
                in_state = temp.copy()
                flag = True

        if (flag == False):
            temp = in_state.copy()
            temp = down(temp)
            new_heuristics = cal_heuristics(temp,fi_state)
            print(new_heuristics)
            if ( new_heuristics < old_heuristics):
                old_heuristics = new_heuristics
                in_state = temp.copy()
                flag = True


        if (flag == False):
            print("NO FURTHER HEURISTICS AVAILABLE with LESS VALUE. NO PATH FOUND!!")
            break

        print("Cycle repeat following next node..............")


    print(used_states)


# In[13]:


HillClimbing(initial_state, final_state)


# In[ ]:





# In[14]:


initial_state = np.array([[1,4,2],[0,3,5],[6,7,8]])
final_state = np.array([[1,0,2],[3,4,5],[6,7,8]])


# In[15]:


HillClimbing(initial_state, final_state)

