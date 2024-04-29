variable "rg_name-9484" {
}

variable "rg_location-9484" {
}

variable "common_tags" {}

variable "windows_machine" {
  default = "windows-9484vm"
}

variable "windows_avs" {
  default = "win_avs-9484"
}

variable "wvm_count" {
  default = "1"
}

variable "subnet_id" {
}

variable "vm_size" {
  default = "Standard_DS1_v2"
}

variable "admin_username" {
  default = "w_n01609484"
}

variable "admin_password" {
  default = "bharath@123"
}

variable "storage_uri" {
}

variable "os_caching" {
  default = "ReadWrite"
}
variable "os_type" {
  default = "Standard_LRS"
}

variable "image_publisher" {
  default = "MicrosoftWindowsServer"
}

variable "image_offer" {
  default = "WindowsServer"
}

variable "image_sku" {
  default = "2016-Datacenter"
}

variable "image_version" {
  default = "latest"
}
variable "malware_name" {
  default = "Antimalware"
}

variable "malware_publisher" {
  default = "Microsoft.Azure.Security"
}

variable "malware_type" {
  default = "IaaSAntimalware"
}
variable "malware_version" {
  default = "1.5"
}



