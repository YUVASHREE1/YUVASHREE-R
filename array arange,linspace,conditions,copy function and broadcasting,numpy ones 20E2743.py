#!/usr/bin/env python
# coding: utf-8

# In[1]:


#array arange,linspace,conditions,copy function and broadcasting,numpy ones
import numpy as np
a=[1,2,3,4,5]
b=[3,4,5,6,7]
c=[6,7,8,9,1]
arr=np.array([a,b,c])


# In[2]:


arr


# In[4]:


np.linspace(1,20,50)  #linspace


# In[6]:


np.arange(1,20)     #arange


# In[7]:


np.linspace(2.0,3.0,5)


# In[9]:


np.linspace(2.0,3.0,5,endpoint=False)


# In[10]:


#conditions
arr=([1,2,3,4,5,6,7])
arr2=np.array(arr)


# In[11]:


value=2
arr2<5


# In[28]:


value=2
arr2*5


# In[29]:


value=2
arr2[arr2<500]


# In[22]:


#numpy ones
np.ones(5)


# In[23]:


#copy function and broadcasting
arr=([40,60,33,44,85,92])
arr2=np.array(arr)


# In[24]:


arr2


# In[25]:


arr2[3:]=100


# In[26]:


arr2


# In[20]:


arr2[:5]=100


# In[21]:


arr2


# In[30]:


np.ones(5)


# In[31]:


np.random.rand(3,3)


# In[33]:


arr_ex=np.random.randn(4,4)


# In[34]:


arr_ex


# In[ ]:




