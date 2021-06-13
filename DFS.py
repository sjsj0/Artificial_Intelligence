#!/usr/bin/env python
# coding: utf-8

# # Depth First Search(DFS)

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


initial_state = np.array([[1,2,3],[8,0,4],[7,6,5]])
final_state = np.array([[2,8,1],[0,4,3],[7,6,5]])


# In[3]:


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


# In[4]:


def check(ch_func, listToCheck):
    flag=True
    for x in listToCheck:
        if(ch_func==x).all():
            flag=False
            return flag
    return flag


# In[5]:


def DFS(in_state, fi_state):
    state_space=[]
    used_state=[]
    state_space.append(in_state)
    
    while True:        
        if (len(state_space)==0):
            print("Not found")
            break
        else:
            popped = state_space.pop(0)
            used_state.append(popped)
            
            if (fi_state == popped).all():
                print("Found")
                break
            
            subList = []
            
            temp = popped.copy()
            temp = left(temp)            
            if check(temp,used_state):
                subList.append(temp)
            
            temp = popped.copy()
            temp = right(temp)
            if check(temp,used_state):
                subList.append(temp)
                
            temp = popped.copy()
            temp = up(temp)
            if check(temp,used_state):
                subList.append(temp)
                
            temp = popped.copy()
            temp = down(temp)
            if check(temp,used_state):
                subList.append(temp)
                
            subList.extend(state_space)    
            state_space = subList.copy()
            
                
    return used_state


# In[6]:


result = DFS(initial_state, final_state)


# In[7]:


result


# In[ ]:




