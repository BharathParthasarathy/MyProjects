resource "azurerm_network_interface" "NI" {
  count               = var.lvm_count
  name                = "${var.linux_machine}-nic-${format("%1d", count.index + 1)}"
  location            = var.rg_location-9484
  resource_group_name = var.rg_name-9484

  ip_configuration {
    name                          = "${var.linux_machine}-ipconfig-${format("%1d", count.index + 1)}"
    subnet_id                     = var.subnet_id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = element(azurerm_public_ip.pub_ip[*].id, count.index + 1)
  }
  tags = var.common_tags
}

resource "azurerm_public_ip" "pub_ip" {
  count               = var.lvm_count
  name                = "${var.linux_machine}-pip-${format("%1d", count.index + 1)}"
  resource_group_name = var.rg_name-9484
  location            = var.rg_location-9484
  allocation_method   = "Dynamic"
  domain_name_label   = "${var.linux_machine}-dns-${format("%1d", count.index + 1)}"
  tags                = var.common_tags
}

resource "azurerm_linux_virtual_machine" "vmlinux" {
  count               = var.lvm_count
  name                = "${var.linux_machine}-${format("%1d", count.index + 1)}"
  resource_group_name = var.rg_name-9484
  location            = var.rg_location-9484
  size                = var.size
  admin_username      = var.Admin_user
  availability_set_id = azurerm_availability_set.as-9484.id
  network_interface_ids = [
    element(azurerm_network_interface.NI[*].id, count.index + 1)
  ]

  admin_ssh_key {
    username   = var.Admin_user
    public_key = file(var.pub_key)
  }

  source_image_reference {
    publisher = var.pub
    offer     = var.offer
    sku       = var.sku_image
    version   = var.version_image
  }

  os_disk {
    name                 = "${var.linux_machine}-osdisk-${format("%1d", count.index + 1)}"
    storage_account_type = var.os_type
    caching              = var.os_caching
    disk_size_gb         = var.os_disk_size
  }

  boot_diagnostics {
    storage_account_uri = var.storage_uri
  }
  tags = var.common_tags
}
resource "azurerm_availability_set" "as-9484" {
  name                         = var.linux_avs
  resource_group_name          = var.rg_name-9484
  location                     = var.rg_location-9484
  platform_fault_domain_count  = 2
  platform_update_domain_count = 5
  tags                         = var.common_tags
}

resource "azurerm_virtual_machine_extension" "network_watcher" {
  count                = var.lvm_count
  name                 = "${var.linux_machine}-network_watcher-${format("%1d", count.index + 1)}"
  virtual_machine_id   = element(azurerm_linux_virtual_machine.vmlinux[*].id, count.index + 1)
  publisher            = var.vm_publisher
  type                 = var.vm_nwtype
  type_handler_version = var.nw_version
  tags                 = var.common_tags
}

resource "azurerm_virtual_machine_extension" "azure_monitor" {
  count                      = var.lvm_count
  name                       = "${var.linux_machine}-azuremonitor-${format("%1d", count.index + 1)}"
  virtual_machine_id         = element(azurerm_linux_virtual_machine.vmlinux[*].id, count.index + 1)
  publisher                  = var.az_monitor_pub
  type                       = var.az_monitor_type
  type_handler_version       = var.az_monitor_version
  auto_upgrade_minor_version = true
  tags                       = var.common_tags
}
