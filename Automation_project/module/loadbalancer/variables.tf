variable "rg_location-9484" {
}
variable "rg_name-9484" {
}
variable "linuxvm_ids" {
}

variable "linux_vm_name" {
}

variable "common_tags" {}

variable "pubip_name" {
  default = "LB-pub_ip"
}
variable "alloc_method" {
  default = "Static"
}

variable "pub_sku" {
  default = "Basic"
}

variable "lb_name" {
  default = "assignment-lb"
}

variable "lb_sku" {
  default = "Basic"
}

variable "lb-configip" {
  default = "assignment-lb-ipconfig"
}

variable "lb_poolname" {
  default = "assignment-lb-addrpool"
}

