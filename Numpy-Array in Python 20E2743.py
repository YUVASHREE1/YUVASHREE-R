#!/usr/bin/env python
# coding: utf-8

# In[5]:


#NUMPY
#Array
import numpy as np
a=[1,2,3,4,5,6,7]   #one Dimensional Array
arr=np.array(a)


# In[6]:


print(arr)


# In[7]:


type(arr)


# In[8]:


arr.shape #No. of ELEMENTS 


# In[11]:


arr.reshape(1,2)


# In[12]:


#Multinested array
a=[1,2,3,4,5]
b=[3,4,5,6,7]
c=[6,7,8,9,1]
arr=np.array([a,b,c])


# In[13]:


arr


# In[14]:


type(arr)


# In[15]:


arr.shape


# In[16]:


arr.reshape(1,15)


# In[17]:


arr.reshape(5,3)


# In[26]:


#Indexing
arr=np.array([1,2,3,4,5,6,7])   #one Dimensional Array


# In[27]:


#accessing the array elements
arr


# In[28]:


arr[3]


# In[29]:


arr[6]


# In[30]:


arr[0]


# In[32]:


arr[2]


# In[33]:


arr


# In[34]:


#Multinested array
a=[1,2,3,4,5] # row 0
b=[3,4,5,6,7] # row 1
c=[6,7,8,9,1] # row 2
arr=np.array([a,b,c])


# In[36]:


arr


# In[37]:


#Array slicing[start,stop,incerement]
#array[start:stop,   start:stop]
#        row   row    col  col
arr[:,:]


# In[38]:


arr[1:,:]


# In[39]:


arr[:,:2]


# In[40]:


arr[1:,:2]


# In[41]:


arr[:,3:]


# In[42]:


arr[2:,2:]


# In[43]:


arr[1:,2:]


# In[56]:


#Activity
#creating array in numpy
#multinested array
a=[1,2,3,4,5] # row 0
b=[7,8,9,0,1] # row 1
c=[1,3,4,5,6] # row 2
d=[7,7,2,3,4] # row 3
arr=np.array([a,b,c,d])


# In[57]:


arr


# In[59]:


#array slicing
arr[2:,1:3]


# In[60]:


arr[1:,1:]


# In[61]:


arr[1:3,:2]


# In[ ]:




