#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import pandas as pd


# ### Load iris Dataset

# In[3]:


iris_dict = pd.read_csv('train.csv')
X = iris_dict.iloc[:,0:4]
y = iris_dict.iloc[:,4]


# In[4]:


# shuffle arrays since y values are in order

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)


# #### Fit logistic regression model

# In[9]:


clf = LogisticRegression(max_iter=500)
clf.fit(X_train, y_train)


# In[10]:


y_pred = clf.predict(X_test)


# #### Metrics

# In[11]:


from sklearn.metrics import accuracy_score


# In[12]:


accuracy_score(y_test, y_pred)


# #### Save Model

# In[13]:


import pickle


# In[14]:


with open('iris_trained_model.pkl', 'wb') as f:
    pickle.dump(clf, f)


# In[15]:


with open('iris_trained_model.pkl', 'rb') as f:
    clf_loaded = pickle.load(f)


# In[16]:


clf_loaded

