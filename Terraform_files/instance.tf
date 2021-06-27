resource "aws_instance" "example" {
    ami           = "${var.AMI_ID}"
    instance_type = "${var.instance_type}"
    key_name      = "${var.keypair}"

    provisioner "file" {
        source = "script.sh"
        destination = "/tmp/script.sh"
    }
    provisioner "remote-exec"{
        inline = [
            "chmod +x /tmp/script.sh",
            "sudo /tmp/script.sh"
        ]
    }
}
