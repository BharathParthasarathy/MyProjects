module "resource_group" {
  source      = "./module/resource_group"
  rg_name     = "n01609484-RG"
  rg_location = "CanadaCentral"
  common_tags = local.common_tags
}

module "networking" {
  source           = "./module/networking"
  rg_name-9484     = module.resource_group.rg_output.name
  rg_location-9484 = module.resource_group.rg_output.location
  common_tags      = local.common_tags
}

module "common_services" {
  source           = "./module/common_services"
  rg_name-9484     = module.resource_group.rg_output.name
  rg_location-9484 = module.resource_group.rg_output.location
  common_tags      = local.common_tags
}

module "linux_vm" {
  source           = "./module/linux_VM"
  rg_name-9484     = module.resource_group.rg_output.name
  rg_location-9484 = module.resource_group.rg_output.location
  subnet_id        = module.networking.subnet_name-op.id
  storage_uri      = module.common_services.storage_account-primary_blob_endpoint
  common_tags      = local.common_tags
}

module "windows_vm" {
  source           = "./module/windows_vm"
  rg_name-9484     = module.resource_group.rg_output.name
  rg_location-9484 = module.resource_group.rg_output.location
  subnet_id        = module.networking.subnet_name-op.id
  storage_uri      = module.common_services.storage_account-primary_blob_endpoint
  common_tags      = local.common_tags
}

module "data_disk" {
  source           = "./module/Data_disk"
  rg_name-9484     = module.resource_group.rg_output.name
  rg_location-9484 = module.resource_group.rg_output.location
  vm_ids           = concat(module.windows_vm.Hostname, module.linux_vm.Hostname)
  common_tags      = local.common_tags
}

module "loadbalancer" {
  source           = "./module/loadbalancer"
  rg_name-9484     = module.resource_group.rg_output.name
  rg_location-9484 = module.resource_group.rg_output.location
  linuxvm_ids      = module.linux_vm.linux-nic
  linux_vm_name    = module.linux_vm.host
  common_tags      = local.common_tags
}

locals {
  common_tags = {
    Assignment : "CCGC 5502 Automation Assignment"
    Name : "Bharath Parthasarathy"
    ExpirationDate : "2024-12-31"
    Environment : "Learning"
  }
}
