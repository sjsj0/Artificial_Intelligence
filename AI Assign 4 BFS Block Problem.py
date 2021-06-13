#!/usr/bin/env python
# coding: utf-8

# # BFS (Block World Problem)

# Name of Student: Sagar Jha

# Roll No: 102097008

# Branch: Computer Science & Engineering

# Sub Group: CSE6
## Nomenclature
#A->1
#B->2
#C->3
# In[8]:


import numpy as np


# In[9]:


initial_state = np.array([[0,0,0],
                          [3,0,0],
                          [2,1,0]])
final_state = np.array([[3,0,0],
                        [2,0,0],
                        [1,0,0]])


# In[10]:


def check(ch_func, listToCheck):
    flag=True
    for x in listToCheck:
        if(ch_func==x).all():
            flag=False
            return flag
    return flag


# In[11]:


def generator(in_state):
    output = []

    for y in range(3):                     # col 0,1,2
        for x in range(3):                 # row 0,1,2
            if in_state[x][y] != 0:
                temp_value = in_state[x][y]
                state = in_state.copy()
                state[x][y] = 0
                for j in range(3):
                    if j != y:
                        for i in reversed(range(3)):
                            if in_state[i][j]==0:
                                temp_state = state.copy()
                                temp_state[i][j] = temp_value
                                output.append(temp_state)
                                break
                break
    
    ### for arranging-->
    
    for x in output:
        for i in range(2):
            if(np.sum(x[:,i] != 0) < np.sum(x[:,i+1] != 0)):
                temp = x[:,i].copy()
                x[:,i] = x[:,i+1]
                x[:,i+1] = temp
                      
    return output
                


# In[12]:


def BFS(in_state, fi_state):
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
            
            temp = popped.copy()
            temp = generator(temp)
#             print("Temp: ")
#             print(temp)
            for x in temp:          
                if check(x,used_state):
                    state_space.append(x)
            
    return used_state


# In[13]:


result = BFS(initial_state, final_state)


# In[7]:


result

