# Azure Service Demo

This document explains how to configure Azure Blob Storage and upload files to it.

## Requirements
- Azure Account
- Storage account and container created
- Azure CLI or Portal access

## Steps

1. **Create Resource Group**
   ```bash
   az group create --name MultiCloudGroup --location eastus
   ```

2. **Create Storage Account**
   ```bash
   az storage account create --name mystorageacct --resource-group MultiCloudGroup --location eastus --sku Standard_LRS
   ```

3. **Create Blob Container**
   ```bash
   az storage container create --account-name mystorageacct --name mycontainer --public-access blob
   ```

4. **Upload File**
   ```bash
   az storage blob upload --account-name mystorageacct --container-name mycontainer --file example.txt --name example.txt
   ```

5. **Access File**
   Visit: `https://mystorageacct.blob.core.windows.net/mycontainer/example.txt`
