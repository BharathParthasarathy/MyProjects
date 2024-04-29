variable "rg_name-9484" {
  type = string
}

variable "rg_location-9484" {
  type = string
}

variable "vnet" {
  default = "n01609484-vnet"
}

variable "subnet" {
  default = "n01609484-subnet"
}

variable "vnet_space" {
  default = ["10.0.0.0/16"]
}

variable "subnet_space" {
  default = ["10.0.0.0/24"]
}

variable "network_sg" {
  default = "n01609484-security_group"
}

variable "common_tags" { }

