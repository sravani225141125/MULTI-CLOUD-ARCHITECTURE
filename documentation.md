## Multi-Cloud Architecture Overview

This architecture uses:
- AWS EC2 to host a Python Flask app
- Azure Blob Storage to store files
- A shared API where AWS interacts with Azure using REST APIs

### Key Components

#### AWS
- EC2 (app host)
- IAM (for permissions)

#### Azure
- Blob Storage
- Azure App Service (optional)

### Interoperability Flow

1. User sends data to Flask app (hosted on AWS EC2).
2. Flask app sends file/data to Azure Blob Storage using Azure SDK or REST API.
3. Confirmation returned to user.

### Benefits
- Redundancy and flexibility
- Leverage best features of both cloud providers
