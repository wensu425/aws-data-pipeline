import pandas as pd
import boto3

bucket = "sentiment-target"
file_name = "['realDonaldTrump']_sentiment.csv"

s3 = boto3.client('s3') 
# 's3' is a key word. create connection to S3 using default config and all buckets within S3

obj = s3.get_object(Bucket= bucket, Key= file_name) 
# get object and file (key) from bucket

initial_df = pd.read_csv(obj['Body']) # 'Body' is a key word
initial_df = initial_df.iloc[:,1:]
records = tuple(initial_df.to_records(index=False))
print(records)