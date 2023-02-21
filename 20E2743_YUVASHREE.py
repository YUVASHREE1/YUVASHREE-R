#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df=pd.read_csv('c:/Users/DGVC/Downloads/day_wise.csv',encoding='latin-1')
df.head()


# In[5]:


df.columns


# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


df.isnull().sum()


# In[11]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[13]:


Deaths_names=df.Deaths.value_counts().index
Recovered_val=df.Deaths.value_counts().values
## Pie Chart- Top 3 countries that uses zomato
plt.pie(Deaths_names[:3],labels=Recovered_val[:3],autopct='%1.2f%%')


# In[14]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (12, 6)
sns.barplot(x="Deaths",y="Recovered",data=df)


# In[17]:


sns.barplot(x="Deaths",y="Recovered",hue='No. of countries',data=df,palette=['blue','red','orange','yellow','green','green'])


# In[18]:


## Count plot
sns.countplot(x="No. of countries",data=df,palette=['blue','red','orange','yellow','green','green'])


# In[19]:


df.corr()


# In[20]:


sns.heatmap(df.corr())


# In[21]:


sns.jointplot(x='Deaths',y='Recovered',data=df,kind='hex')


# In[22]:


sns.pairplot(df)


# In[23]:


sns.distplot(df['Deaths'])


# In[24]:


## Count plot

sns.countplot('Deaths',data=df)


# In[25]:


## Bar plot
sns.barplot(x='Deaths',y='Recovered',data=df)


# In[26]:


sns.boxplot('Deaths','Recovered', data=df)


# In[27]:


sns.violinplot(x="Deaths", y="Recovered", data=df,palette='rainbow')


# In[28]:


import matplotlib.pyplot as plt
##can be used without using plot.show()
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
## Simple Examples

x=np.arange(0,10)
y=np.arange(11,21)
a=np.arange(40,50)
b=np.arange(50,60)
##plotting using matplotlib 

##plt scatter

plt.scatter(x,y,c='g')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Graph in 2D')
plt.savefig('Test.png')


# In[30]:


y=x*x
## plt plot

plt.plot(x,y,'r--',linestyle='dashed',linewidth=2, markersize=12)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('2d Diagram')


# In[31]:


## Creating Subplots

plt.subplot(2,2,1)
plt.plot(x,y,'r--')
plt.subplot(2,2,2)
plt.plot(x,y,'g*--')
plt.subplot(2,2,3)
plt.plot(x,y,'bo')
plt.subplot(2,2,4)
plt.plot(x,y,'go')


# In[32]:



# Compute the x and y coordinates for points on a sine curve 
x = np.arange(0, 4 * np.pi, 0.1) 
y = np.sin(x) 
plt.title("sine wave form") 

# Plot the points using matplotlib 
plt.plot(x, y) 
plt.show() 


# In[33]:


## Bar plot

x = [2,8,10] 
y = [11,16,9]  

x2 = [3,9,11] 
y2 = [6,15,7] 
plt.bar(x, y) 
plt.bar(x2, y2, color = 'g') 
plt.title('Bar graph') 
plt.ylabel('Y axis') 
plt.xlabel('X axis')  

plt.show()


# In[34]:


#Histograms
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27]) 
plt.hist(a) 
plt.title("histogram") 
plt.show()


# In[35]:


#Pie Chart
# Data to plot
labels = 'Python', 'C++', 'Ruby', 'Java'
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.4, 0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=False)

plt.axis('equal')
plt.show()


# In[ ]:




