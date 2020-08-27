#!/usr/bin/env python
# coding: utf-8

# In[121]:

import pandas as pd
import mysql.connector
import pickle

cnx = mysql.connector.connect(user='admin', password='password',
                              host='mydb.coz5sga2vbtt.us-east-1.rds.amazonaws.com',
                              port=3306,
                              database='innodb')
cursor = cnx.cursor()


# In[122]:


query = ("SELECT SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm FROM predict;")
cursor.execute(query)
table_rows = cursor.fetchall()
X=pd.DataFrame(table_rows)


# In[123]:


with open('iris_trained_model.pkl', 'rb') as f:
    clf_loaded = pickle.load(f)


# In[124]:


y=clf_loaded.predict(X)


# In[125]:


for i in range(0,len(y)):
    update_data = ("UPDATE predict SET prediction = '{}' WHERE ID={};".format(str(y[i]), int(i+1)))
    cursor.execute(update_data)

query = ("SELECT * FROM predict;")
cursor.execute(query)
table_rows = cursor.fetchall()
print(table_rows)

# In[112]:


cnx.close()

