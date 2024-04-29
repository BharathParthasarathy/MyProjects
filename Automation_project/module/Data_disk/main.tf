resource "azurerm_managed_disk" "data_disk" {
  count                = length(var.vm_ids)
  name                 = "${count.index}-data-disk"
  location             = var.rg_location-9484
  resource_group_name  = var.rg_name-9484
  storage_account_type = var.storage-type
  create_option        = "Empty"
  disk_size_gb         = var.data_disk_attr
  tags                 = var.common_tags
}

resource "azurerm_virtual_machine_data_disk_attachment" "data_disk_attach" {
  count              = length(var.vm_ids)
  virtual_machine_id = var.vm_ids[count.index]
  managed_disk_id    = element(azurerm_managed_disk.data_disk[*].id, count.index + 1)
  lun                = count.index
  caching            = var.caching-type
}
