from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.web import WebSiteManagementClient
import time

# Define Azure Subscription ID
SUBSCRIPTION_ID = "adb0fd05-32d7-4708-b1ba-ff8d1b9a0ca8"
RESOURCE_GROUP_NAME = "myResourceGroup"
LOCATION = "centralus"  # ✅ Match with existing resource group
STORAGE_ACCOUNT_NAME = "naga1717"
APP_SERVICE_PLAN_NAME = "myAppServicePlan"

# Authenticate with Azure
credential = DefaultAzureCredential()
resource_client = ResourceManagementClient(credential, SUBSCRIPTION_ID)
storage_client = StorageManagementClient(credential, SUBSCRIPTION_ID)
web_client = WebSiteManagementClient(credential, SUBSCRIPTION_ID)

# Step 1: Ensure Resource Group Exists
print("🔹 Ensuring Resource Group Exists...")
resource_client.resource_groups.create_or_update(
    RESOURCE_GROUP_NAME, {"location": LOCATION}
)

# Step 2: Create Storage Account (if not exists)
print("🔹 Checking Storage Account...")
storage_accounts = list(storage_client.storage_accounts.list_by_resource_group(RESOURCE_GROUP_NAME))
existing_storage = any(acc.name == STORAGE_ACCOUNT_NAME for acc in storage_accounts)

if not existing_storage:
    print("✅ Creating Storage Account...")
    storage_client.storage_accounts.begin_create(
        RESOURCE_GROUP_NAME,
        STORAGE_ACCOUNT_NAME,
        {
            "location": LOCATION,
            "sku": {"name": "Standard_LRS"},  # ✅ Free-tier supported
            "kind": "StorageV2",
        },
    ).result()
    time.sleep(10)  # Allow some time for storage creation

# Step 3: Create App Service Plan (Consumption Plan)
print("✅ Creating App Service Plan...")
web_client.app_service_plans.begin_create_or_update(
    RESOURCE_GROUP_NAME,
    APP_SERVICE_PLAN_NAME,
    {
        "location": LOCATION,
        "sku": {"name": "Y1", "tier": "Dynamic"},  # ✅ Standard Consumption Plan
        "kind": "functionapp",
    },
).result()

print("✅ All Resources Created Successfully.")
