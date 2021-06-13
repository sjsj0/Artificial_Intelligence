#!/usr/bin/env python
# coding: utf-8

# # Depth Limited(=1) (Block World Problem)

## Nomenclature
A->1
B->2
C->3
# In[50]:


import numpy as np


# In[51]:


initial_state = np.array([[0,0,0],
                          [3,0,0],
                          [2,1,0]])
final_state = np.array([[3,0,0],
                        [2,0,0],
                        [1,0,0]])


# In[52]:


def check(ch_func, listToCheck):
    flag=True
    for x in listToCheck:
        if(ch_func==x).all():
            flag=False
            return flag
    return flag


# In[53]:


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
                


# In[54]:


def DFS_Limited(in_state, fi_state, depth):
    state_space=[]
    used_state=[]
    level = 0
    state_space.append([in_state,level])
    
    while True:        
        if (len(state_space)==0):
            print("Not found")
            break
        else:
            popped = state_space.pop(0)
            used_state.append(popped[0])
#             print("Used state: ")
#             print(used_state)
            
            if (fi_state == popped[0]).all():
                print("Found")
                break
            
            level = popped[1]
#             print("Level Popped:")
#             print(level)
            
            if(level<depth):
                subList = []

                temp = popped[0].copy()
                level = level + 1
#                 print("Level inside: ")
#                 print(level)
                temp = generator(temp)
#                 print("Temp: ")
#                 print(temp)
                for x in temp:          
                    if check(x,used_state):
                        subList.append([x,level])

                subList.extend(state_space)    
                state_space = subList.copy()
    #             print("State space: ")
    #             print(state_space)
            
                
    return used_state


# In[55]:


result = DFS_Limited(initial_state, final_state, 1)


# In[56]:


result

