#!/usr/bin/env python
# coding: utf-8

# In[7]:


# libraries and data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 


# In[8]:


df = pd.read_csv('spacestocksinfo.csv', skipinitialspace=True) 

df['Date']= pd.to_datetime(df['Date'])  


ax = sns.lineplot(data=df, x='Date',y='High', hue='company')  
plt.title("Top Ten Space Stocks") 
# Put the legend out of the figure
plt.legend(bbox_to_anchor=(1.0, 1), loc=2, borderaxespad=0.)
ax.set(ylim=(1, 100))
plt.show()     

