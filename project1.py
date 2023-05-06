#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd


# In[11]:


df1=pd.read_csv("Desktop\L0509WellData.csv")
print(df1.head())


# In[18]:


df1.replace(-999,np.nan,inplace =True)
print (df1.head())


# In[19]:


df1.describe()


# In[20]:


df1.plot(x="GR",y="DEPTH")
plt.show()


# In[22]:


df1.plot(kind="scatter",x="DT" ,y="RHOB" , color="red")


# In[29]:


df1.plot(kind="scatter",x="RHOB",y="DRHO", c="NPHI" , colormap="jet")


# In[38]:


df1.hist( figsize=(40,40) ,bins=50 , color="red")


# In[39]:


df1.skew()


# In[53]:


df1["GR"].hist(figsize=(15,10),color="red",bins=60)


# In[56]:


df1["DEPTH"].plot(kind="kde",color="green")
plt.show()


# In[69]:


x = ['A','B','C']

for a , b in enumerate(x):
    print(a)


# In[ ]:




