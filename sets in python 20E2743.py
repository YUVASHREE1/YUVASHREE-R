#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sets in python
#craeting sets
a = {"apple", "banana", "cherry"}
print(a)


# In[2]:


#Duplicates Not Allowed
b = {"apple", "banana", "cherry", "apple"}

print(b)


# In[4]:


c = {1,2,3,4,5,6,7}

print(len(c))


# In[5]:


#type()
myset = {"apple", "banana", "cherry"}
print(type(myset))


# In[6]:


#union
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z)


# In[8]:


#update
   s = {1, 2, 3}
s.update({4, 5})
print(s)


# In[9]:


#intersection
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)


# In[10]:


#intersection_update
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x.intersection_update(y, z)

print(x)


# In[16]:


#difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference(y)

print(x)


# In[15]:


#difference update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)


# In[ ]:




