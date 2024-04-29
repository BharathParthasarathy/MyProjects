output "lb-op" {
  value = azurerm_lb.bharath-lb.name
}

output "lb-public-ip" {
  value = azurerm_public_ip.lb_public_ip.ip_address
}
