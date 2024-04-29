output "common_service-op" {
  value = azurerm_log_analytics_workspace.common-9484
}

output "recovery_vault-op" {
  value = azurerm_recovery_services_vault.recovery_vault-9484
}

output "standard_storage-op" {
  value = azurerm_storage_account.standard_storage-9484
}

output "storage_account-primary_blob_endpoint" {
  value = azurerm_storage_account.standard_storage-9484.primary_blob_endpoint
}
