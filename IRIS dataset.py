#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[10]:


""" importing dataset from git hub """
""" And dropping the index 0 column as we dont need that"""

iris_data = pd.read_csv("https://raw.githubusercontent.com/utkarshg0102/Iris_sample_data/main/Iris_data_sample.csv", index_col = 0)
iris_data.head(10)


# In[18]:


"""Removing junk values such as ?? ### using na_values"""

iris_data = pd.read_csv("https://raw.githubusercontent.com/utkarshg0102/Iris_sample_data/main/Iris_data_sample.csv",                        index_col = 0, na_values = ["??","###"])

iris_data.head()


# In[19]:


""" Creating copy of the dataset"""
# Shallow Copy
data1 = iris_data.copy(deep = False)


# In[31]:


""" Creating copy of the dataset"""
# deep Copy
data2 = iris_data.copy(deep = True)


# In[24]:


"""To check the number of rows"""

data2.index


# In[22]:


"""To check the name of all columes"""

data2.columns


# In[26]:


"""Shape"""

data2.shape


# In[27]:


"""Size"""

data2.size


# In[28]:


"""Memory usage"""

data2.memory_usage()


# In[29]:


"""Dimension"""

data2.ndim


# In[30]:


"""To get the detailed information of the dataset"""

data2.info()


# In[ ]:




