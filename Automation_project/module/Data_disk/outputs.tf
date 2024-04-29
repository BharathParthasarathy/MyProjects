output "datadisk-op" {
  value = azurerm_managed_disk.data_disk[*].name
}
