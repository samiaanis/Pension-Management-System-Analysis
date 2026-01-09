#!/usr/bin/env python
# coding: utf-8

# ## Setup

# In[97]:


get_ipython().system('pip install pandas numpy seaborn matplotlib')


# In[98]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt


# In[100]:


df=pd.read_csv(r'C:\Users\LENOVO\Desktop\da\workshop\Pension_Management_System\pension_dataset_20000.csv')


# ## Data exploration

# In[101]:


df.shape


# In[102]:


df.head()


# In[103]:


df.info()


# In[104]:


df.isnull().sum()


# In[105]:


df.duplicated().sum()


# ## Cleaning & Standardization

# In[106]:


# formatting dates


# In[107]:


date_col=['dob','join_date','retirement_date','last_contribution','created_at']


# In[108]:


df[date_col]=df[date_col].apply(pd.to_datetime,errors='coerce')


# In[109]:


df.info()


# In[110]:


df[date_col].isnull().sum()


# In[111]:


# correcting numerical errors


# In[112]:


num_col=['years_of_service','monthly_pension','lump_sum','spouse_count','inflation_index']


# In[113]:


for c in num_col:
    df[c] = pd.to_numeric(df[c], errors='coerce')


# In[114]:


df.loc[df['monthly_pension'] < 0, 'monthly_pension'] = pd.NA
df.loc[df['lump_sum'] < 0, 'lump_sum'] = pd.NA
df.loc[df['years_of_service'] < 0, 'years_of_service'] = pd.NA
df.loc[df['spouse_count'] < 0, 'spouse_count'] = pd.NA

df.loc[df['years_of_service'] > 60, 'years_of_service'] = pd.NA
df.loc[df['spouse_count'] > 5, 'spouse_count'] = pd.NA

df.loc[(df['inflation_index'] < 0.5) | (df['inflation_index'] > 2.0), 'inflation_index'] = pd.NA


# In[115]:


df[num_col].describe()


# In[116]:


# standardizing text fields


# In[117]:


text_col= ['name','gender','pension_type','region','payment_method','beneficiary_name']


# In[118]:


df['beneficiary_name'] = df['beneficiary_name'].replace(
    {'NaN': pd.NA, 'None': pd.NA, '': pd.NA}
)


# In[119]:


for c in text_col:
    df[c] = df[c].astype('string').str.strip().str.title()


# ##	Data Consistency & Derivation

# In[120]:


# Deriving age at retirement


# In[121]:


df['age_at_retirement']=df['retirement_date'].dt.year - df['dob'].dt.year


# In[122]:


df['age_at_retirement'].describe()


# In[123]:


# Deriving pension status


# In[124]:


df['pension_status'] = df['active_flag'].map({
    1: 'Active',
    0: 'Retired'
})


# In[125]:


# Re-calculating the years_of_service field 


# In[126]:


df['calculated_years_of_service']=df['retirement_date'].dt.year - df['join_date'].dt.year


# In[127]:


df['service_years_diff'] = (
    df['years_of_service'] - df['calculated_years_of_service']
)


# In[128]:


df[df['service_years_diff'] != 0][
    ['name','join_date', 'retirement_date', 'years_of_service',
     'calculated_years_of_service', 'service_years_diff']
].head()


# ## 	Privacy Protection

# In[129]:


df1=df.copy()

df1.drop(
    columns=['name', 'beneficiary_name', 'bank_account_mask'],
    inplace=True
)


# In[130]:


df1.head()


# In[131]:


get_ipython().system('pip install pymysql sqlalchemy')


# In[132]:


from sqlalchemy import create_engine

# MySQL connection
username = "root"
password = "Bismillah_786"
host = "localhost"
port = "3306"
database = "pension_management"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

# Write DataFrame to MySQL
table_name = "pension"

df1.to_sql(
    table_name,
    engine,
    if_exists="replace",
    index=False
)

# Read back sample
pd.read_sql("SELECT * FROM pension LIMIT 5;", con=engine)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




