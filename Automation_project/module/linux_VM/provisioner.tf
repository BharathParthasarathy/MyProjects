resource "null_resource" "vmlinux-provisioner-linux" {
  count      = var.lvm_count
  depends_on = [azurerm_linux_virtual_machine.vmlinux]
  provisioner "remote-exec" {
    inline = ["echo Hostname: $(hostname)"]
  }

  connection {
    type        = "ssh"
    user        = var.Admin_user
    private_key = file(var.private_key)
    host        = element(azurerm_linux_virtual_machine.vmlinux[*].public_ip_address, count.index + 1)
  }
}
