provider "azurerm" {
  features {}

  subscription_id = "adb0fd05-32d7-4708-b1ba-ff8d1b9a0ca8"
  use_cli         = true
}

variable "resource_group_name" {
  default = "DefaultResourceGroup-CCAN"
}

variable "storage_account_name" {
  default = "nagasampleacct"
}

resource "azurerm_storage_container" "containers" {
  count                 = 100
  name                  = "container-${count.index}"
  storage_account_name  = var.storage_account_name
  container_access_type = "private"
}
