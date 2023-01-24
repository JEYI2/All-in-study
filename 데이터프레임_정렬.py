#!/usr/bin/env python
# coding: utf-8

# #  '행 인덱스'를 기준으로 데이터프레임 정렬
# * 행 인덱스 기준 정렬: DataFrame 객체.sort_index()
# * 내림차순: ascending=False 오름차순: ascending=True

# ###예제 1-19###

# In[7]:


import pandas as pd
dic_data= {'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],'c3':[10,11,12],'c4':[13,14,15]}
df = pd.DataFrame(dic_data,index=['r0','r1','r2'])
print(df)


# #내림차순으로 행 인덱스 정렬

# In[5]:


ndf = df.sort_index(ascending=False)
print(ndf)


# #오름차순으로 행 인덱스 정렬

# In[9]:


ndf2 = df.sort_index(ascending=True)
print(ndf2)


# # 열을 기준으로 데이터프레임 정렬
# * 열 인덱스 기준 정렬: DataFrame 객체.sort_values()

# In[15]:


dic_data = {'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],'c3':[10,11,12],'c4':[13,14,15]}
df = pd.DataFrame(dic_data,index=['r0','r1','r2'])
print(df)


# In[ ]:


#내림차순으로 열 기준 정렬 


# In[17]:


ndf = df.sort_values(by='c1', ascending=False)
print(ndf)


# In[ ]:


#오름차순으로 열 기준 정렬


# In[22]:


ndf2 = df.sort_values(by='c1', ascending=True)
print(ndf2)

