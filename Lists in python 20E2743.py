#!/usr/bin/env python
# coding: utf-8

# In[1]:


# creating list
a=[]
b=[1,2,3,4,5,6]
c=["Apple","Orange","Banana","Kiwi","Mango"]


# In[2]:


#Add 2 lists
# Append
d=b+c
print(d) 


# In[3]:


# Append(for and in)
sum=0
for num in a:
 sum=sum+a
print(sum) 


# In[19]:


#Add items into the list
#Appending(range)
s=[]
for i in range(3,15,2):
 s.append(i)
print(s)


# In[20]:


#Appending
p=["a","b","c"]
p.append("G")
print(p)


# In[22]:


#inserting
o=[12,1,45,78]
t=[]
o.insert(5,88)
t.insert(0,23.5)
print(o)
print(t)


# In[23]:


#Displaying the List
print(a)
print(b)
print(c)
print(d)
print(sum)
print(s)
print(p)
print(t)





# In[24]:


#Accessing Elements in Lists
Q=[1,2,3,4,5,6,7]
print("Original list is : " + str(Q))
print("List index-value are : ")
for i in range(len(Q)):
    print(i, end=" ")
    print(Q[i])


# In[25]:


#Accessing Elements in Lists
E=[1,2,3,4,5,6,7]
print("Original list is : " + str(E))
print("List index-value are : ")
print([list((i, E[i])) for i in range(len(E))])


# In[26]:


#Accessing elements
programming_lang = ['P','Y','T','H','O','N']

print(programming_lang)

print("At index 0:", programming_lang[0])
print("At index 3:",programming_lang[3])


# In[28]:


#Length of List
programming_lang = ['P','Y','T','H','O','N']
print("Length of the List:",len(programming_lang))


# In[33]:


#Length of Particular item in list
programming_lang = ['P','Y','T','H','O','N']
print("Length of the letter P is:",len(programming_lang))


# In[39]:


#Assignment operator in list
list1 = [1,2,3,4,5]
list2 = [6,7,8,9]
list3 = list1
list4 = [1,2,3,4,5]
list4 += [45,78,90]
print(list1)
print(list2)
print(list3)
print(list4)


# In[41]:


a = ["apple", "banana", "cherry"]
i = 0
while i < len(a):
  print(a[i])
  i = i + 1


# In[ ]:




