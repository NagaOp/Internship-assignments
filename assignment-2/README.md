## Task:
Using Terraform to create 100 containers in one storage account and writing a Python function that creates 1000 txt files in each container.

## Steps:

1. Created an Azure Storage Account manually named nagasampleacct.
2. Wrote a Terraform configuration file (main.tf) to create 100 containers (container-0 to container-99) in the storage account.
3. Ran the following Terraform commands:
   - terraform init
   - terraform apply
4. Wrote a Python script using the azure-storage-blob library.
5. The script connects to the storage account using a connection string.
6. For each container, the script uploads 1000 empty text files (file-0.txt to file-999.txt).
7. Ran the script once to upload all files across all containers.

