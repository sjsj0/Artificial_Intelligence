#!/usr/bin/env python
# coding: utf-8

# # Uniform Cost Search(Graph)

# Name of Student: Sagar Jha

# Roll No: 102097008

# Branch: Computer Science & Engineering

# Sub Group: CSE6

# In[1]:


import numpy as np


# In[2]:


# Graph
# Vertex numbered as:-
# S-> 0
# A-> 1
# B-> 2
# C-> 3
# G-> 4
my_graph = np.array([[0,1,5,15,0],
                     [0,0,0,0,10],
                     [0,0,0,0,5],
                     [0,0,0,0,5],
                     [0,0,0,0,0]])


# In[3]:


initial_state = 0
goal_state = 4


# In[4]:


def Uniform_Search():
    open_list=[]
    open_list.append([[initial_state],0])
    print(open_list)
    
    while True:
        if (len(open_list)==0):
            print("Not found")
            break

        else:
            popped = open_list.pop(0)
            print("\nPopped:")
            print(popped)
            
            vertex = popped[0][-1]
            till_cost = popped[1]
            
            if (goal_state == vertex):
                print("Found")
                print(popped)
                break
            
            
            for x in range(5):
                if (my_graph[vertex][x] != 0):
                    temp = popped[0].copy()
                    temp.append(x)
                    new_cost = till_cost + my_graph[vertex][x]
                    new_set = [temp, new_cost]
                    
                    open_list.append(new_set)
                

            open_list.sort(key = lambda x:x[1], reverse=False)
            print("Printing priority queued open_list")
            print(open_list)


# In[5]:


Uniform_Search()

