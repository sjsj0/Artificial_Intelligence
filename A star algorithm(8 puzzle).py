#!/usr/bin/env python
# coding: utf-8

# In[31]:

import numpy as np


# In[32]:


initial_state = np.array([[2,0,3],[1,8,4],[7,6,5]])
final_state = np.array([[1,2,3],[8,0,4],[7,6,5]])


# In[33]:


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

def check(ch_func, listToCheck):
    flag=True
    for x in listToCheck:
        if(ch_func==x).all():
            flag=False
            return flag
    return flag

# count of misplaced tiles...
def cal_heuristics(a,b):
    return np.sum(a != b)


# In[34]:


def A_star(in_state, fi_state):
    open_list=[]
    closed=[]
    
    g=0
    h = cal_heuristics(in_state, fi_state)
    f = g+h
    temp_list = [in_state, f]
    open_list.append(temp_list)
    print(open_list)
    
    
    while True:
        if (len(open_list)==0):
            print("Not found")
            break

        else:
            pop = open_list.pop(0)
            popped = pop[0]
            print("\nPopped:")
            print(popped)
            closed.append(popped)

            if (fi_state == popped).all():
                print("Found")
                break
            
            g=g+1
            
            temp = popped.copy()
            temp = left(temp)            
            if check(temp,closed):
                h = cal_heuristics(temp, fi_state)
                f = g+h
                temp_list = [temp, f]
                open_list.append(temp_list)
            
            temp = popped.copy()
            temp = right(temp)
            if check(temp,closed):
                h = cal_heuristics(temp, fi_state)
                f = g+h
                temp_list = [temp, f]
                open_list.append(temp_list)
            
            temp = popped.copy()
            temp = up(temp)
            if check(temp,closed):
                h = cal_heuristics(temp, fi_state)
                f = g+h
                temp_list = [temp, f]
                open_list.append(temp_list)
            
            temp = popped.copy()
            temp = down(temp)
            if check(temp,closed):
                h = cal_heuristics(temp, fi_state)
                f = g+h
                temp_list = [temp, f]
                open_list.append(temp_list) 
            
            
            open_list.sort(key = lambda x:x[1], reverse=False)
           
            print("Printing priority queued open_list")
            print(open_list)
                    
            
    print("Final Result is: ")    
    print(closed)


# In[35]:


A_star(initial_state, final_state)

