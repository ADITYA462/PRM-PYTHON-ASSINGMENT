#!/usr/bin/env python
# coding: utf-8

# Python Candidates - Question 1
# 
# 
# 
# You will have a number of elements and in the next n lines element of a list. You have to create a list from the given strings. You have to sort the list based on 2nd last character of a string
# 
# 
# 
# For example: Given list = ['great','hello','hiyo','abc'] So your output_dictionary should be ['great','abc','hello','hiyo']
# 
# 
# 
# Input format:
# 
# 
# 
# At first-line it will have an integer (number of elements inside a list). In the second line it will have a string
# 
# 
# 
# Output Format:
# 
# 
# 
# A single line containing a sorted list

# In[1]:


n = int(input())
lst = []
for i in range(n):
    s = input()
    lst.append(s)

sorted_lst = sorted(lst, key=lambda x: x[-2])

print(sorted_lst)


# In[ ]:





# In[ ]:




