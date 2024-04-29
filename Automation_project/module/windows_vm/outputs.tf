output "Hostname" {
  value = azurerm_windows_virtual_machine.windows_vm[*].id
}

output "privateIP-windows" {
  value = [azurerm_network_interface.windows_nic[*].private_ip_address]
}

output "publicIP-windows" {
  value = [azurerm_public_ip.windows_public_ip[*].ip_address]
}

output "Domain_namelinux" {
  value = [azurerm_public_ip.windows_public_ip[*].domain_name_label]
}

output "host" {
  value = azurerm_windows_virtual_machine.windows_vm[*].name
}

output "windows_vm_fqdn" {
  value = azurerm_public_ip.windows_public_ip[*].fqdn
}

output "windows_nic_id" {
  value = azurerm_network_interface.windows_nic[*].id
}
