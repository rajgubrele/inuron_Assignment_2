#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
# 2. Write a Python program to reverse a word after accepting the input from the user.
# Input word: ineuron
# Output: norueni


# Answer

# In[110]:


k = 4
for i in range(7):
    if i <=5:
        print("* "*i)
    else:
        for j in range(5):
            print("* "*k)
            k-=1


# In[111]:


a = input()            
if a == "ineuron":
    print(a[::-1])

