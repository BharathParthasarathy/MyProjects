resource "azurerm_availability_set" "windows_availability_set" {
  name                = "${var.windows_machine}_avs"
  resource_group_name = var.rg_name-9484
  location            = var.rg_location-9484
  tags                = var.common_tags
}

resource "azurerm_network_interface" "windows_nic" {
  count               = var.wvm_count
  name                = "${var.windows_machine}-nic-${format("%1d", count.index + 1)}"
  location            = var.rg_location-9484
  resource_group_name = var.rg_name-9484

  ip_configuration {
    name                          = "${var.windows_machine}-ipconfig-${format("%1d", count.index + 1)}"
    subnet_id                     = var.subnet_id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = element(azurerm_public_ip.windows_public_ip[*].id, count.index + 1)
  }
  tags = var.common_tags
}

resource "random_pet" "dns_suffix" {
  length    = 2
  separator = "-"
}

resource "azurerm_public_ip" "windows_public_ip" {
  count               = var.wvm_count
  name                = "${var.windows_machine}-pubip-${format("%1d", count.index + 1)}"
  location            = var.rg_location-9484
  resource_group_name = var.rg_name-9484
  allocation_method   = "Dynamic"
  domain_name_label   = "dns-${random_pet.dns_suffix.id}-${format("%1d", count.index + 1)}"
  tags                = var.common_tags
}

resource "azurerm_windows_virtual_machine" "windows_vm" {
  count                 = var.wvm_count
  name                  = "${var.windows_machine}-windowsvm-${format("%1d", count.index + 1)}"
  computer_name         = "win-comp-${format("%1d", count.index + 1)}"
  location              = var.rg_location-9484
  resource_group_name   = var.rg_name-9484
  availability_set_id   = azurerm_availability_set.windows_availability_set.id
  network_interface_ids = [element(azurerm_network_interface.windows_nic[*].id, count.index + 1)]
  size                  = var.vm_size
  admin_username        = var.admin_username
  admin_password        = var.admin_password

  os_disk {
    name                 = "osdisk-${format("%1d", count.index + 1)}"
    caching              = var.os_caching
    storage_account_type = var.os_type
  }

  source_image_reference {
    publisher = var.image_publisher
    offer     = var.image_offer
    sku       = var.image_sku
    version   = var.image_version
  }

  boot_diagnostics {
    storage_account_uri = var.storage_uri
  }
  tags = var.common_tags
}

resource "azurerm_virtual_machine_extension" "antimalware" {
  count                = var.wvm_count
  name                 = var.malware_name
  virtual_machine_id   = element(azurerm_windows_virtual_machine.windows_vm[*].id, count.index + 1)
  publisher            = var.malware_publisher
  type                 = var.malware_type
  type_handler_version = var.malware_version
  tags                 = var.common_tags
  settings             = <<SETTINGS
  {
    "AntimalwareEnabled": true,
    "RealtimeProtectionEnabled": "true",
    "ScheduledScanSettings": {
      "isEnabled": "true",
      "day": "1",
      "time": "120",
      "scanType": "Quick"
    }
  }
  SETTINGS
}

