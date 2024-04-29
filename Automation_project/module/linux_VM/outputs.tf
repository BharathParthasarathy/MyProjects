output "Hostname" {
  value = azurerm_linux_virtual_machine.vmlinux[*].id
}

output "privateIP" {
  value = [azurerm_network_interface.NI[*].private_ip_address]
}

output "publicIP" {
  value = [azurerm_public_ip.pub_ip[*].ip_address]
}

output "linux-avs" {
  value = azurerm_availability_set.as-9484.name
}

output "Domain_namelinux" {
  value = [azurerm_public_ip.pub_ip[*].domain_name_label]
}

output "linux-nic" {
  value = azurerm_network_interface.NI[*].id
}

output "host" {
  value = azurerm_linux_virtual_machine.vmlinux[*].name
}

output "linux_vm_fqdn" {
  value = azurerm_public_ip.pub_ip[*].fqdn
}
