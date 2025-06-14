# Interoperability Demo

This document demonstrates how the Flask app hosted on AWS EC2 interacts with Azure Blob Storage.

## Overview

- Flask app receives a file upload
- Uses Azure SDK to authenticate and upload to Blob Storage

## Prerequisites

- Azure Blob Storage access key and connection string
- `azure-storage-blob` Python package installed

## Code Snippet

```python
from azure.storage.blob import BlobServiceClient

conn_str = "<AZURE_CONNECTION_STRING>"
blob_service = BlobServiceClient.from_connection_string(conn_str)

def upload_to_blob(file_data, filename):
    container_client = blob_service.get_container_client("mycontainer")
    container_client.upload_blob(name=filename, data=file_data)
```

## Execution

1. Start Flask app on AWS
2. Upload file via frontend or API
3. File is stored in Azure Blob and accessible via URL
