variable "rg_name-9484" {
}
variable "rg_location-9484" {
}
variable "subnet_id" {
}

variable "linux_machine" {
  default = "linux-9484vm01"
}

variable "size" {
  default = "Standard_B1s"
}

variable "Admin_user" {
  default = "bharath-n01609484"
}

variable "pub_key" {
  default = "~/.ssh/id_rsa.pub"

}

variable "private_key" {
  default = "~/.ssh/id_rsa"

}

variable "linux_avs" {
  default = "linux-availability-set"
}

variable "lvm_count" {
  default = 3
}

variable "storage_uri" {}

variable "common_tags" {}

variable "pub" {
  default = "OpenLogic"
}

variable "offer" {
  default = "CentOS"
}

variable "sku_image" {
  default = "8_2"
}

variable "version_image" {
  default = "latest"
}

variable "os_type" {
  default = "Standard_LRS"
}

variable "os_caching" {
  default = "ReadWrite"
}
variable "os_disk_size" {
  default = "32"
}

variable "vm_publisher" {
  default = "Microsoft.Azure.NetworkWatcher"
}

variable "vm_nwtype" {
  default = "NetworkWatcherAgentLinux"
}

variable "nw_version" {
  default = "1.4"
}

variable "az_monitor_pub" {
  default = "Microsoft.Azure.Monitor"
}

variable "az_monitor_type" {
  default = "AzureMonitorLinuxAgent"
}

variable "az_monitor_version" {
  default = "1.0"
}

