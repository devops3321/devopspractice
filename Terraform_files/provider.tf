terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "3.47.0"
    }
  }
}

provider "aws"{
    AWS_ACCESS_KEY = ${var.AWS_ACCESS_KEY}
    AWS_SECRET_KEY = ${var.AWS_SECRET_KEY}
}