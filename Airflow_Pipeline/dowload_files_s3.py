#!/usr/bin/env python
# coding: utf-8

# In[89]:


import logging
import boto3
from botocore.exceptions import ClientError
import os
import glob
import pandas as pd


# In[87]:


my_bucket= 'train.data.bucket'


# In[60]:


def download_file(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
     
    if object_name is None:
        object_name = file_name
    
    s3_client = boto3.client('s3')
    #s3 = boto3.resource('s3')
    #your_bucket = s3.Bucket(bucket)

    try:
        response = s3_client.download_file(bucket,  object_name, file_name)
    except ClienteError as e:
        logging.error(e)
        return False
    return True
     


# In[86]:



s3_client = boto3.client('s3')
s3_content = s3_client.list_objects(Bucket=my_bucket)['Contents']

x=0
for i in s3_content:
    if s3_content[x]['Key'][-4:] == '.csv':
        my_object=s3_content[x]['Key']
        file_name = my_object[5:]
        download_file(file_name, my_bucket, my_object)
    x=x+1
    


# In[94]:


extension='csv'
os.getcwd()
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
combined_csv.to_csv( "train.csv", index=False, encoding='utf-8-sig')

