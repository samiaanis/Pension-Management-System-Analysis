#!/usr/bin/env python
# coding: utf-8

# # Extraction

# In[7]:


import os
os.chdir(r"C:\Users\LENOVO\Desktop\da\workshop\Pension_Management_System")



# In[8]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt


# In[9]:


import pandas as pd

df = pd.read_csv("pension_dataset_20000.csv")



# ## Data exploration

# In[10]:


df.shape


# In[11]:


df.head()


# In[12]:


df.info()


# In[13]:


df.isnull().sum()


# In[14]:


df.duplicated().sum()


# ## Cleaning & Standardization

# In[15]:


# formatting dates


# In[16]:


date_col=['dob','join_date','retirement_date','last_contribution','created_at']


# In[17]:


df[date_col]=df[date_col].apply(pd.to_datetime,errors='coerce')


# In[18]:


df.info()


# In[19]:


df[date_col].isnull().sum()


# In[20]:


# correcting numerical errors


# In[21]:


num_col=['years_of_service','monthly_pension','lump_sum','spouse_count','inflation_index']


# In[22]:


for c in num_col:
    df[c] = pd.to_numeric(df[c], errors='coerce')


# In[23]:


df.loc[df['monthly_pension'] < 0, 'monthly_pension'] = pd.NA
df.loc[df['lump_sum'] < 0, 'lump_sum'] = pd.NA
df.loc[df['years_of_service'] < 0, 'years_of_service'] = pd.NA
df.loc[df['spouse_count'] < 0, 'spouse_count'] = pd.NA

df.loc[df['years_of_service'] > 60, 'years_of_service'] = pd.NA
df.loc[df['spouse_count'] > 5, 'spouse_count'] = pd.NA

df.loc[(df['inflation_index'] < 0.5) | (df['inflation_index'] > 2.0), 'inflation_index'] = pd.NA


# In[24]:


df[num_col].describe()


# In[25]:


# standardizing text fields


# In[26]:


text_col= ['name','gender','pension_type','region','payment_method','beneficiary_name']


# In[27]:


for c in text_col:
    df[c] = df[c].astype('string').str.strip().str.title()


# In[28]:


df['beneficiary_name'] = df['beneficiary_name'].replace(
    {'NaN': pd.NA, 'None': pd.NA, '': pd.NA}
)


# ##	Data Consistency & Derivation

# In[29]:


# Deriving age at retirement


# In[30]:


df['age_at_retirement']=df['retirement_date'].dt.year - df['dob'].dt.year


# In[31]:


df['age_at_retirement'].describe()


# In[32]:


# Deriving pension status


# In[33]:


df['pension_status'] = df['active_flag'].map({
    1: 'Active',
    0: 'Retired'
})


# In[34]:


# Re-calculating the years_of_service field 


# In[35]:


df['calculated_years_of_service']=df['retirement_date'].dt.year - df['join_date'].dt.year


# In[36]:


df['service_years_diff'] = (
    df['years_of_service'] - df['calculated_years_of_service']
)


# In[37]:


df[df['service_years_diff'] != 0][
    ['name','join_date', 'retirement_date', 'years_of_service',
     'calculated_years_of_service', 'service_years_diff']
].head()


# ## 	Privacy Protection

# In[38]:


df1=df.copy()

df1.drop(
    columns=['name', 'beneficiary_name', 'bank_account_mask'],
    inplace=True
)


# In[39]:


df1.head()


# In[42]:


from dotenv import load_dotenv

load_dotenv()
print(os.getenv("DB_USER"))


# In[43]:


from sqlalchemy import create_engine

# MySQL connection
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT", "3306")
db   = os.getenv("DB_NAME")


engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{db}"
                      )


# In[44]:


# Write DataFrame to MySQL
table_name = "pension"

df1.to_sql(
    table_name,
    engine,
    if_exists="append",
    index=False
)


# Read back sample
pd.read_sql("SELECT * FROM pension LIMIT 5;", con=engine)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




