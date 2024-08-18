#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
data={'name':['jai','anuj'],'age':[24,26],'address':['delhi','jaipur']}
df=pd.DataFrame(data)
print(df)
df.rename(columns={'address':'place'},inplace=True)
df


# In[23]:


import pandas as pd

df = pd.DataFrame([[5,6],[7,4]], columns=['a','b'])
df2 = pd.DataFrame([[5,6],[7,4]], columns=['a','b'])

# Using pd.concat() instead of append
df = pd.concat([df, df2], ignore_index=True)
df
print()
df.drop(0,axis=0,inplace=True)
df


# In[40]:


import pandas as pd
data={'Name':['jai','anuj'],'age':[24,26],'address':['delhi','jaipur']}
df=pd.DataFrame(data)
print(df[['Name','age']])


# In[47]:


import pandas as pd
data={'Name':['jai','anuj'],'age':[24,26],'address':['delhi','jaipur'],'height':[1.54,3.55]}
df=pd.DataFrame(data)
df.filter(items=['Name','age'])


# In[46]:


import pandas as pd
data={'Name':['jai','anuj'],'age':[24,26],'address':['delhi','jaipur'],'height':[1.54,3.55]}
df=pd.DataFrame(data)

df.filter(like='eigh')


# In[48]:


import pandas as pd
data={'Name':['jai','anuj'],'age':[24,26],'address':['delhi','jaipur'],'height':[1.54,3.55]}
df=pd.DataFrame(data)
df.filter(regex='e|a',axis=1)


# In[54]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Mano'],'age':[24,26,24,24],'address':['delhi','jaipur','Chennai','Chennai'],'height':[1.54,3.55,4.2,4.2]}
df=pd.DataFrame(data)
df=df.drop_duplicates()
print()
df


# In[56]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Mano'],'age':[24,26,24,24],'address':['delhi','jaipur','Chennai','rajasthan'],'height':[1.54,3.55,4.2,4.5]}
df=pd.DataFrame(data)
df=df.drop_duplicates(subset=['Name','age'],keep='last')
print()
df


# In[62]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Mano','Nan'],'age':[24,26,24,24,20],'address':['delhi','jaipur','Chennai','rajasthan','Switz'],'height':[1.54,3.55,4.2,4.5,5]}
df=pd.DataFrame(data)
df_sample=df.sample(frac=0.2)
print(df_sample)


# In[4]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Mano','Nan'],'age':[24,26,24,24,20],'salary':[2000,3688,5666,1888,7000]}
df=pd.DataFrame(data)
top_salaries=df.nlargest(2,columns='salary')
print(top_salaries)
print()
bottom_salaries=df.nsmallest(2,columns='salary')
print(bottom_salaries)


# In[10]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Mano'],'age':[24,26,24,32],'address':['delhi','jaipur','Chennai','rajasthan'],'height':[1.54,3.55,4.2,4.5]}
df=pd.DataFrame(data)
df=df.query('age>=30')
df


# In[12]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Mano'],'age':[24,26,24,32],'address':['delhi','jaipur','Chennai','rajasthan'],'height':[1.54,3.55,4.2,4.5]}
df=pd.DataFrame(data)
df=df.query('Name.str.contains("a")')
df


# In[14]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Mano'],'age':[24,26,24,32],'address':['delhi','jaipur','Chennai','rajasthan'],'height':[1.54,3.55,4.2,4.5],'gender':['M','F','M','F']}
df=pd.DataFrame(data)
df.query('gender == ["M"] and age<25')
df


# In[17]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Mano'],'age':[24,26,24,32],'address':['delhi','jaipur','Chennai','rajasthan'],'height':[1.54,3.55,4.2,4.5],'gender':['M','F','M','F']}
df=pd.DataFrame(data)
df.loc[:,'age']


# In[18]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Mano'],'age':[24,26,24,32],'address':['delhi','jaipur','Chennai','rajasthan'],'height':[1.54,3.55,4.2,4.5],'gender':['M','F','M','F']}
df=pd.DataFrame(data)
df.iloc[:,3]


# In[20]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Mano'],'age':[24,26,24,32],'address':['delhi','jaipur','Chennai','rajasthan'],'height':[1.54,3.55,4.2,4.5],'gender':['M','F','M','F']}
df=pd.DataFrame(data)
df.loc[:,['Name','age']]


# In[21]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Mano'],'age':[24,26,24,32],'address':['delhi','jaipur','Chennai','rajasthan'],'height':[1.54,3.55,4.2,4.5],'gender':['M','F','M','F']}
df=pd.DataFrame(data)
df.iloc[:,0]


# In[23]:


import pandas as pd
data={'Name':['jai','anuj','Mano','nandu'],'age':[24,26,24,32],'address':['delhi','jaipur','Chennai','rajasthan'],'height':[1.54,3.55,4.2,4.5],'gender':['M','F','M','F']}
df=pd.DataFrame(data)
df_filtered = df[df['age'] > 30]
print(df_filtered)


# In[24]:


import pandas as pd
data={'Name':['jai','anuj','Mano','nandu'],'age':[24,26,24,32],'address':['delhi','jaipur','Chennai','rajasthan'],'height':[1.54,3.55,4.2,4.5],'gender':['M','F','M','F']}
df=pd.DataFrame(data)
df_filtered = df[df['age'] > 30 & (df['height'] > 1.7)]
print(df_filtered)


# In[26]:


import pandas as pd
data={'Name':['jai','anuj','Mano','nandu'],'age':[24,26,24,32],'address':['delhi','jaipur','Chennai','rajasthan'],'height':[1.54,3.55,4.2,4.5],'gender':['M','F','M','F']}
df=pd.DataFrame(data)
df_filtered = df[df['Name'].str.startswith('a')]
print(df_filtered)


# In[28]:


import pandas as pd
data={'Name':['jai','anuj','Mano','nandu'],'age':[24,26,24,32],'address':['delhi','jaipur','Chennai','rajasthan'],'height':[1.54,3.55,4.2,4.5],'gender':['M','F','M','F']}
df=pd.DataFrame(data)
print(df.tail(2))
print()
print(df.head(1))
print()
df.info()


# In[29]:


import pandas as pd
data={'Name':['jai','anuj','Mano','nandu'],'age':[24,26,24,32],'address':['delhi','jaipur','Chennai','rajasthan'],'height':[1.54,3.55,4.2,4.5],'gender':['M','F','M','F']}
df=pd.DataFrame(data)
print(df.describe())


# In[4]:


import pandas as pd
data = {'name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Emily', 'Frank'],
        'gender': ['F', 'M', 'M', 'M', 'F', 'M'],
        'age': [25, 35, 40, 28, 30, 45],
        'salary': [50000, 70000, 60000, 80000, 65000, 90000]}
df = pd.DataFrame(data)
grouped = df.groupby('gender').mean()['salary']
print(grouped)


# In[ ]:





# In[ ]:




