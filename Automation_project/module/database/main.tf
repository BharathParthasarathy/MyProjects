resource "azurerm_postgresql_server" "database_9484" {
  name                = "n01609484-database"
  resource_group_name = var.rg_name-9484
  location            = var.rg_location-9484
  sku_name            = var.sku_name
  version             = var.postgresql_version

  administrator_login          = var.admin_login
  administrator_login_password = var.admin_password
  ssl_enforcement_enabled      = true
  tags                         = var.common_tags
}
