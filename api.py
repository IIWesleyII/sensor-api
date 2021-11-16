import os
from google.cloud import storage
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service_key.json'
storage_client = storage.Client()

'''
Create New Bucket
'''
def create_bucket(name):
    # 'bucket_ws8910'
    bucket_name = name
    bucket = storage_client.bucket(bucket_name)
    bucket.location = 'US'
    storage_client.create_bucket(bucket)

'''
Upload File
'''
def upload_to_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False

'''
Download File
'''
def download_file_from_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        
        with open(file_path, 'wb') as f:
            storage_client.download_blob_to_file(blob,f)
        
        return True
    except Exception as e:
        print(e)
        return False






file_path = r'C:\Users\Sunny\Desktop\kernel'
filename = 'data_11-16-2021_10-45-29.csv'

upload_to_bucket(f'{filename}', os.path.join(file_path,f'{filename}'),'bucket_ws8910')

#bucket_name = 'bucket_ws8910'
#download_file_from_bucket('filename', os.path.join( os.getcwd(), 'filename'),  bucket_name)
