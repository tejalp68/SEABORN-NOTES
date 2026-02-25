#!/usr/bin/env python
# coding: utf-8

# # SEABORN

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# sns.get_dataset_names()


# In[2]:


df = sns.load_dataset("penguins")
df.head(10)


# In[3]:


df.info()


# In[4]:


df.describe()


# In[5]:


df.isnull().sum()


# In[6]:


df.columns


# In[7]:


df.dtypes


# In[8]:


df[df.isnull().any(axis=1)]


# #### Line plot

# In[9]:


sns.lineplot(x="bill_length_mm", y="flipper_length_mm", data=df)
sns.set_style("whitegrid")


# In[10]:


sns.lineplot(x="bill_length_mm", y="flipper_length_mm", data=df)
sns.set_style("ticks")


# In[11]:


sns.lineplot(x="bill_length_mm", y="flipper_length_mm", data=df)
sns.set_style("dark")


# #### Violin plot

# In[12]:


sns.violinplot(x="island", y="bill_depth_mm", data=df)
sns.set_theme("notebook")


# In[13]:


sns.violinplot(x="island", y="bill_depth_mm", data=df)
sns.set_theme("paper")


# In[14]:


sns.violinplot(x="island", y="bill_depth_mm", data=df)
sns.set_theme("talk")


# In[15]:


sns.violinplot(x="island", y="bill_depth_mm", data=df)
sns.set_theme("poster")


# In[16]:


# Another dataset


# In[17]:


dp = sns.load_dataset("exercise")
dp


# In[18]:


dp.info()


# In[19]:


dp.describe()


# In[20]:


dp.columns


# In[21]:


dp.dtypes


# In[22]:


dp.isnull().sum()


# In[23]:


dp.drop("Unnamed: 0",axis =1,inplace=True)


# In[24]:


dp


# In[25]:


dp.index = dp.index -1


# In[26]:


dp


# In[27]:


dp.nunique()


# In[28]:


print(dp["id"].unique())
print()
print(dp["diet"].unique())
print(dp["diet"].value_counts())
print()
print(dp["pulse"].unique())
print()
print(dp["time"].unique())
print(dp["time"].value_counts())
print()
print(dp["kind"].unique())
print(dp["kind"].value_counts())


# In[29]:


pd.unique(dp.values.ravel())


# In[30]:


dp


# #### Line plot

# In[31]:


sns.lineplot(data=dp, x='id', y='pulse',
             linewidth=2,
             linestyle='-',

            errorbar=None)
sns.set_style("darkgrid")
sns.set_theme("notebook")
plt.show()


# In[32]:


sns.lineplot(data=dp, x='id', y='pulse',
             linewidth=2,
             linestyle='-',

            errorbar=None,
            hue="kind")
sns.set_style("whitegrid")
plt.show()


# In[33]:


sns.lineplot(data=dp, x='id', y='pulse',
             linewidth=2,
             linestyle='-',

            errorbar=None,
            hue="diet")

plt.show()


# In[34]:


sns.lineplot(data=dp, x='id', y='pulse',
             linewidth=2,
             linestyle='-',
             palette ="plasma",
            errorbar=None,
            hue="time")
sns.set_style("whitegrid")
plt.title("ID graph related to Pulse")
plt.show()


# #### Bar plot

# In[35]:


sns.barplot(x='island', y='bill_depth_mm', data=df)
plt.show()


# In[36]:


df[df["island"] == "Dream"].count()


# In[37]:


df["island"].value_counts()


# In[38]:


df[df["island"]== "Dream"].value_counts()


# In[39]:


df[df['island'] == 'Dream']['bill_depth_mm'].mean()


# In[40]:


sns.barplot(x="diet",y="pulse",data = dp)
plt.show()


# In[41]:


sns.barplot(x="diet",y="pulse",hue="time",data = dp)
plt.show()


# In[42]:


## used estimator as sum


# In[43]:


sns.barplot(x="diet",y="pulse",hue="time",estimator=sum,errorbar=None,data = dp)
plt.show()


# In[44]:


sns.barplot(x="diet",y="pulse",hue="time",estimator='median' ,errorbar=None,data = dp,palette="plasma")
plt.show()


# In[45]:


sns.barplot(x=dp.diet ,y=dp.pulse ,estimator ='mean',hue=dp.time,errorbar= None,palette="Accent")
plt.show()


# #### Histogram

# In[56]:


sns.histplot(df['bill_depth_mm'], bins=20,color="green")
plt.show()


# In[57]:


sns.displot(df['bill_depth_mm'], bins=20,color="green")
plt.show()


# In[61]:


sns.displot(df['bill_depth_mm'], bins=[14,15,16,17,18,19,20],color="green")
plt.show()


# In[66]:


sns.displot(df['bill_depth_mm'], bins=20,color="green",kde=True)
plt.show()


# In[68]:


sns.displot(df['bill_depth_mm'], bins=20,color="green",kde=True)
plt.show()


# In[70]:


sns.histplot(df['bill_depth_mm'], color="green",kde=True)
plt.show()


# #### KDE plot

# In[83]:


sns.kdeplot(x="bill_length_mm",hue="sex",data=df,color="blue")
plt.show()


# #### Scatter plot

# In[84]:


df


# In[218]:


sns.scatterplot(x='bill_length_mm',y='bill_depth_mm',data=df,color='g',marker='o',  sizes=(60, 500),   )
plt.style.use('default')
sns.reset_defaults()
plt.show()


# #### Count plot

# In[129]:


sns.countplot(x="kind",hue="diet",data=dp)
plt.show()


# In[135]:


sns.countplot(x="island",hue="sex",data=df,hue_order=["Female","Male"])
plt.show()


# In[136]:


df


# #### Violin plot

# In[152]:


sns.violinplot(x='island', y='bill_length_mm',data=df)
plt.show()


# In[154]:


sns.violinplot(x='island', y='bill_length_mm',data=df, inner='box',color="g")
plt.show()


# In[153]:


sns.violinplot(x='island', y='bill_length_mm',data=df,split=True, inner='box')
plt.show()


# #### Strip plot

# In[155]:


sns.stripplot(x='island', y='bill_length_mm', data=df)
plt.show()


# In[157]:


sns.stripplot(x='island', y='bill_length_mm',hue='sex', data=df)
plt.show()


# In[160]:


sns.stripplot(x='island', y='bill_length_mm',hue='sex',jitter=True, data=df)
plt.show()


# #### Swarm plot

# In[161]:


sns.swarmplot(x='island', y='bill_length_mm', data=df)
plt.show()


# In[163]:


sns.swarmplot(x='island', y='bill_length_mm',hue="sex" ,data=df)
plt.show()


# #### Pair plot

# In[165]:


sns.pairplot(df)
plt.show()


# In[167]:


sns.pairplot(df, hue='sex')
plt.show()


# In[169]:


sns.pairplot(df, kind='scatter', diag_kind='kde')
plt.show()


# #### Heatmap

# In[176]:


corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()


# In[177]:


corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm',linewidths=15)
plt.show()


# #### Regression plot

# In[185]:


sns.regplot(x='flipper_length_mm', y='bill_depth_mm' ,data=df)
plt.show()


# In[187]:


sns.regplot(x='flipper_length_mm', y='body_mass_g' ,data=df)
plt.show()


# In[188]:


sns.regplot(x='body_mass_g', y='flipper_length_mm' ,data=df)
plt.show()


# #### Joint plot

# In[193]:


sns.jointplot(x='body_mass_g', y='flipper_length_mm', data=df, kind='hex')
plt.show()


# In[194]:


sns.jointplot(x='body_mass_g', y='flipper_length_mm', data=df, kind='scatter')
plt.show()


# In[195]:


sns.jointplot(x='body_mass_g', y='flipper_length_mm', data=df, kind='kde')
plt.show()


# #### Categorical plot

# In[201]:


sns.catplot(
    x='island', y='flipper_length_mm',
    col='sex',
    kind='violin',
    data=df
)
plt.show()


# In[204]:


sns.catplot(
    x='island', y='flipper_length_mm',
    col='sex',
    kind='swarm',
    data=df
)
plt.show()


# In[219]:


sns.catplot(
    x='island', y='flipper_length_mm',
    col='species',
    kind='box',
    data=df
)
plt.show()


# In[212]:


sns.color_palette()
sns.set_palette("pastel")
sns.reset_defaults()
sns.color_palette()


# In[229]:


sns.get_dataset_names()


# In[231]:


df1=sns.load_dataset( 'tips')
df1


# In[239]:


g = sns.FacetGrid(df1, col='sex', row='time')
g.map(sns.lineplot, 'total_bill', 'tip')
plt.show()


# In[236]:


df1['time'].value_counts()


# In[ ]:




