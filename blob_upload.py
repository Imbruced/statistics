import os
from azure.storage.blob import BlobServiceClient


files_to_upload = [
    "functions/__init__.py",
    "functions/stats.py",
   # "main.py"
]

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
env = os.getenv('SECRET')

blob_service_client = BlobServiceClient.from_connection_string(connect_str)

for file in files_to_upload:
    blob_client = blob_service_client.get_blob_client(container="stats", blob=file)
    with open(file, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
