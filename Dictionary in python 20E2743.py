#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Dictionary
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict)


# In[3]:


#Dictionary Items
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict["brand"])


# In[4]:


#Duplicates Not Allowed
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(dict)


# In[5]:


#Dictionary Length
print(len(dict))


# In[6]:


#type()
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(dict))


# In[15]:


dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(dict))


# In[17]:


#Accessing Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)


# In[18]:


#Get the value of the "model" key:
x = thisdict.get("model")
print(x)


# In[19]:


#Get Keys
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change


# In[20]:


#Get Values
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change


# In[21]:


#Get Items
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change


# In[ ]:




