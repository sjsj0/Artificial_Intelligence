#!/usr/bin/env python
# coding: utf-8

# # Best First Search(Graph)

# In[8]:


# graph
my_graph = { "S" : ["A","B"],
          "A" : ["C", "D"],
          "B" : ["E", "F"],
          "E" : ["H","I"],
          "F" : ["J", "G"],
          "C" : [],
         "D" : [],
         "J" : [],
         "G" : []
        } 


# In[9]:


# heuristics
h = {"A":11,
     "B":5,
     "C":9,
     "D":9,
     "E":4,
     "F":2,
     "G":0,
     "H":7,
     "I":3,
     "J":3,
     "S":15}


# In[10]:


initial_state='S'
goal_state='G'


# In[11]:


def Best_First_Search():
    open_list=[]
    closed=[]
    open_list.append(initial_state)
    print(open_list)
    
    while True:
        if (len(open_list)==0):
            print("Not found")
            break

        else:
            popped = open_list.pop(0)
            print("\nPopped:")
            print(popped)
            closed.append(popped)

            if (goal_state == popped):
                print("Found")
                break
            
            
            for key, value in my_graph.items():
                if(key == popped):
                    temp = value
            
            print("Successor of popped:")
            print(temp)
            open_list.extend(temp)
            print("Printing open_list before priority queue")
            print(open_list)
            
            length = len(open_list)
            
            for i in range(length-1):
                for j in range(length-1):
                    
                    for key, value in h.items():
                        if(key == open_list[j]):
                            p = value
                        if(key == open_list[j+1]):
                            q = value
                    
                    if(p>q):
                        temp = open_list[j]
                        open_list[j] = open_list[j+1]
                        open_list[j+1] = temp
            
            print("Printing open_list")
            print(open_list)
                    
            
        
    print(closed)
    
    


# In[12]:


Best_First_Search()

