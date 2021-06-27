variable "AWS_REGION"{
    default="ap-south-1"
}
variable "instance_type"{
    default="t2.micro"
}
variable "keypair"{
    default ="dockerdeployment"
}
variable "AMI_ID"{
    default="ami-0d18acc6e813fd2e0"
}
variable "AWS_ACCESS_KEY" {}
variable "AWS_SECRET_KEY"{}