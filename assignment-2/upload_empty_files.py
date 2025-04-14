from azure.storage.blob import BlobServiceClient

# Your connection string
connection_string = "DefaultEndpointsProtocol=https;AccountName=nagasampleacct;AccountKey=vSJFdjSZ9/mHhkdNTWu88/DpT9DQKOYwUlIKpcMDr6M9bCy+QO74Wq3wjiT2TYYzpP7TVjtec+oF+AStVqkOvA==;EndpointSuffix=core.windows.net"

# Create the BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Loop through 100 containers
for i in range(100):
    container_name = f"container-{i}"
    print(f"Uploading to {container_name}...")

    # Get container client
    container_client = blob_service_client.get_container_client(container_name)

    # Upload 1,000 empty .txt files
    for j in range(1000):
        blob_name = f"file_{j}.txt"
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(b"", overwrite=True)

    print(f"Uploaded 1000 files to {container_name}")
