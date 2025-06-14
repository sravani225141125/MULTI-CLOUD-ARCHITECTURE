# Example Azure Python script
from azure.storage.blob import BlobServiceClient

conn_str = "<Your_Connection_String>"
blob_service = BlobServiceClient.from_connection_string(conn_str)
container_name = "my-container"

for blob in blob_service.get_container_client(container_name).list_blobs():
    print(blob.name)
